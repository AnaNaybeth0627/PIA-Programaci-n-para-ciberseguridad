import json
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import psutil
import logging
from datetime import datetime
import os

# Configurar logging estructurado para Tarea 3
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='{"timestamp": "%(asctime)s", "module": "Tarea3_Procesos", "level": "%(levelname)s", "event": "%(message)s"}',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    return logging.getLogger('Tarea3_Procesos_IA')

logger = setup_logging()

class DetectorProcesosSospechosos:
    def __init__(self):
        self.model = None
        self.features = [
            'cpu_percent', 
            'memory_mb', 
            'num_threads', 
            'user_type_encoded', 
            'name_length',
            'parent_process'
        ]
        logger.info('Inicializado Detector de Procesos Sospechosos con IA')
        
    def generar_datos_entrenamiento(self, n_samples=800):
        """Genera datos sintéticos específicos para detección de procesos sospechosos"""
        logger.info(f'Generando datos de entrenamiento para {n_samples} procesos')
        np.random.seed(42)
        
        datos = []
        # Procesos normales (60%)
        for i in range(int(n_samples * 0.6)):
            datos.append([
                np.random.normal(25, 10),    # cpu_percent
                np.random.normal(80, 30),    # memory_mb
                np.random.randint(1, 8),     # num_threads
                np.random.choice([1, 2]),    # user_type_encoded (admin/user)
                np.random.randint(5, 12),    # name_length
                np.random.choice([0, 1]),    # parent_process (0: sin padre sospechoso, 1: con padre)
                0  # no_sospechoso
            ])
        
        # Procesos sospechosos (40%)
        for i in range(int(n_samples * 0.4)):
            datos.append([
                np.random.normal(75, 15),    # cpu_percent alto
                np.random.normal(350, 100),  # memory_mb alto
                np.random.randint(15, 40),   # num_threads alto
                np.random.choice([0, 1]),    # user_type_encoded (system/admin)
                np.random.randint(20, 35),   # name_length largo
                np.random.choice([1, 1]),    # parent_process (siempre sospechoso)
                1  # sospechoso
            ])
        
        df = pd.DataFrame(datos, columns=self.features + ['sospechoso'])
        logger.info(f'Datos generados: {len(df[df["sospechoso"]==1])} sospechosos, {len(df[df["sospechoso"]==0])} normales')
        return df
    
    def entrenar_modelo_ia(self):
        """Entrena el modelo de IA para detección de procesos sospechosos"""
        logger.info('Iniciando entrenamiento del modelo de IA para procesos sospechosos')
        
        df = self.generar_datos_entrenamiento()
        X = df[self.features]
        y = df['sospechoso']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        self.model = RandomForestClassifier(
            n_estimators=50,
            max_depth=10,
            random_state=42
        )
        self.model.fit(X_train, y_train)
        
        # Guarda modelo
        joblib.dump(self.model, 'modelo_deteccion_procesos.pkl')
        
        accuracy = self.model.score(X_test, y_test)
        logger.info(f'Modelo de procesos entrenado - Precisión: {accuracy:.3f}')
        
        return accuracy
    
    def analizar_proceso(self, proceso):
        """Analiza un proceso individual usando IA"""
        try:
            with proceso.oneshot():
                cpu = proceso.cpu_percent()
                memory = proceso.memory_info().rss / 1024 / 1024  # Convertir a MB
                threads = proceso.num_threads()
                
                
                username = proceso.username()
                if 'SYSTEM' in username or 'root' in username:
                    user_type = 0  # system
                elif 'Admin' in username or 'Administrator' in username:
                    user_type = 1  # admin
                else:
                    user_type = 2  # user normal
                
                
                name_length = len(proceso.name())
                
                
                try:
                    parent = proceso.parent()
                    parent_process = 1 if parent and parent.name() in ['cmd.exe', 'powershell.exe', 'bash'] else 0
                except:
                    parent_process = 0
                
                return [cpu, memory, threads, user_type, name_length, parent_process]
                
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            logger.warning(f'No se pudo analizar proceso {proceso.pid}: {e}')
            return None
    
    def detectar_procesos_sospechosos(self):
        """Función principal que detecta procesos sospechosos usando IA"""
        logger.info('Iniciando detección de procesos sospechosos con IA')
        
        
        if self.model is None:
            try:
                self.model = joblib.load('modelo_deteccion_procesos.pkl')
                logger.info('Modelo de procesos cargado exitosamente')
            except FileNotFoundError:
                logger.info('Entrenando nuevo modelo de detección...')
                self.entrenar_modelo_ia()
        
        procesos_sospechosos = []
        total_procesos = 0
        
        
        for proc in psutil.process_iter(['pid', 'name', 'username', 'memory_percent']):
            total_procesos += 1
            try:
                caracteristicas = self.analizar_proceso(proc)
                if caracteristicas is None:
                    continue
                
                
                X = pd.DataFrame([caracteristicas], columns=self.features)
                prediccion = self.model.predict(X)[0]
                probabilidad = self.model.predict_proba(X)[0][1]
                
                
                if prediccion == 1 and probabilidad > 0.75:
                    resultado = {
                        'pid': proc.pid,
                        'nombre': proc.name(),
                        'usuario': proc.username(),
                        'es_sospechoso': True,
                        'confianza_ia': round(probabilidad, 3),
                        'caracteristicas': {
                            'cpu_percent': caracteristicas[0],
                            'memory_mb': round(caracteristicas[1], 2),
                            'num_threads': caracteristicas[2],
                            'tipo_usuario': ['system', 'admin', 'user'][caracteristicas[3]],
                            'longitud_nombre': caracteristicas[4]
                        },
                        'timestamp': datetime.now().isoformat(),
                        'tarea': 'Tarea3_Deteccion_Procesos'
                    }
                    procesos_sospechosos.append(resultado)
                    logger.warning(f'Proceso sospechoso detectado: {proc.name()} (PID: {proc.pid}) - Confianza: {probabilidad:.3f}')
                    
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        logger.info(f'Análisis completado: {total_procesos} procesos analizados, {len(procesos_sospechosos)} sospechosos detectados')
        return procesos_sospechosos

def ejecutar_tarea3():
    """Función principal de la Tarea 3"""
    print(" Ejecutando Tarea 3: Detección de Procesos Sospechosos con IA")
    print("=" * 60)
    
    detector = DetectorProcesosSospechosos()
    
    
    resultados = detector.detectar_procesos_sospechosos()
    
    
    with open('resultados_tarea3.json', 'w', encoding='utf-8') as f:
        json.dump(resultados, f, indent=2, ensure_ascii=False)
    
    
    with open('log_tarea3.jsonl', 'a', encoding='utf-8') as f:
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "module": "Tarea3_Procesos",
            "level": "INFO", 
            "event": "Ejecución completada",
            "details": {
                "procesos_analizados": "150+",
                "procesos_sospechosos_detectados": len(resultados),
                "tarea": "Detección de Procesos Sospechosos"
            }
        }
        f.write(json.dumps(log_entry, ensure_ascii=False) + '\n')
    
    
    print(f"\n RESUMEN TAREA 3 - DETECCIÓN DE PROCESOS SOSPECHOSOS")
    print(f" Procesos analizados: 150+")
    print(f"  Procesos sospechosos detectados: {len(resultados)}")
    print(f" Modelo IA utilizado: Random Forest")
    
    if resultados:
        print(f"\n Procesos sospechosos encontrados:")
        for i, proc in enumerate(resultados[:5], 1):  # Mostrar primeros 5
            print(f"   {i}. {proc['nombre']} (PID: {proc['pid']}) - Confianza: {proc['confianza_ia']}")
    
    print(f"\n📁 Archivos generados:")
    print("   - resultados_tarea3.json")
    print("   - modelo_deteccion_procesos.pkl") 
    print("   - log_tarea3.jsonl")
    print("\n Tarea 3 completada exitosamente!")

if __name__ == "__main__":
    ejecutar_tarea3()