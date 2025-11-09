# Forzar la política de ejecución solo para esta sesión
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

# Obtene la ruta actual del script
$PSScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition

# Importar módulo correctamente usando ruta absoluta
$modulePath = Join-Path $PSScriptRoot "../src/acquisition/analisis_espacio_disco.psm1"
Import-Module $modulePath -Force

# Construir ruta completa al archivo de configuración
$configPath = Join-Path $PSScriptRoot "../prompts/prompt_V1.json"

# Ejecutar análisis
Invoke-AnalisisEspacioDisco -ConfigPath $configPath
