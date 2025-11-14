# Forzar la política de ejecución solo para esta sesión
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

# Obtene la ruta actual del script
$PSScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition

#Tarea 1
Write-Host "`n=========================" -ForegroundColor Blue
Write-Host "Iniciando TAREA 1: Lectura y registro de cambios" -ForegroundColor Blue
Write-Host "=========================`n" -ForegroundColor Blue

$t1 = Join-Path $PSScriptRoot "../src/acquisition/lectura_y_registro_de_cambios.psm1"
Import-Module $t1 -Force
$config1 = Join-Path $PSScriptRoot "../prompts/prompt_V1.json"
Invoke-LecturaRegistro -ConfigPath $config1

#Tarea adiciona(depende de la tarea1)
Write-Host "`n=========================" -ForegroundColor Blue
Write-Host "Ejecutando TAREA ADICIONAL: Graficos" -ForegroundColor Blue
Write-Host "=========================`n" -ForegroundColor Blue

$tad = Join-Path $PSScriptRoot "../src/reporting/graficos_cambio_de_archivos.py"
python $tad


#tarea 2
Write-Host "`n=========================" -ForegroundColor Blue
Write-Host "Ejecutando TAREA 2: Deteccion de acceso sospechosos" -ForegroundColor Blue
Write-Host "=========================`n" -ForegroundColor Blue

$t2 = Join-Path $PSScriptRoot "../src/Tarea_2.py"
python $t2


#tarea 3
Write-Host "`n=========================" -ForegroundColor Blue
Write-Host "Ejecutando TAREA 3: Monitoreo de Procesos Sospechosos" -ForegroundColor Blue
Write-Host "=========================`n" -ForegroundColor Blue
$t3 = Join-Path $PSScriptRoot "../src/tarea3_ia.py"
python $t3

#tarea 4
Write-Host "`n=========================" -ForegroundColor Blue
Write-Host "Ejecutando TAREA 4: Analisis de espacio en disco y almacenamiento" -ForegroundColor Blue
Write-Host "=========================`n" -ForegroundColor Blue

# Importar módulo correctamente usando ruta absoluta
$modulePath = Join-Path $PSScriptRoot "../src/acquisition/analisis_espacio_disco.psm1"
Import-Module $modulePath -Force
# Construir ruta completa al archivo de configuración
$configPath = Join-Path $PSScriptRoot "../prompts/prompt_V1.json"

# Ejecutar análisis
Invoke-AnalisisEspacioDisco -ConfigPath $configPath
