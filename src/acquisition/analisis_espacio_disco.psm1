function Invoke-AnalisisEspacioDisco {
    param(
        [Parameter(Mandatory=$true)]
        [string]$ConfigPath
    )

    # 1. Resolver ruta base
    $RepoRoot = Split-Path (Split-Path (Split-Path $PSScriptRoot)) -Parent
    
    # Cargar configuración JSON
    $configFullPath = Join-Path $RepoRoot $ConfigPath
    try {

        $config = Get-Content $configPath -Raw | ConvertFrom-Json -ErrorAction Stop
    }
    catch {
        Write-Host "CRÍTICO: Error al cargar la configuración desde $ConfigPath." -ForegroundColor Red
        Write-Host $_.Exception.Message -ForegroundColor Red
        return
    }

    # 1. Extraer parámetros de configuración
    $directorio = $config.instrucciones.directorio_base
    $umbral = $config.instrucciones.umbral_alerta_porcentaje
    $nombreEstadoPrevio = $config.rutas_control.archivo_estado_previo
    $nombreLogSalida = $config.rutas_control.archivo_log_salida

    # 2. Construir rutas completas
    $RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "../..") | Select-Object -ExpandProperty Path

    $rutaEstadoPrevio = Join-Path $RepoRoot "examples\$nombreEstadoPrevio"
    $rutaLogSalida = Join-Path $RepoRoot "examples\$nombreLogSalida"
    $rutaPythonScript = Join-Path $RepoRoot "src\utils\analisis_espacio_disco.py"

    Write-Host "Iniciando analisis de espacio en disco..." -ForegroundColor Yellow
    Write-Host "Ruta del script Python: $rutaPythonScript"
    Write-Host "Directorio a monitorear: $directorio"

    # 3. Ejecutar el script de Python con los argumentos necesarios
    $pythonArgs = @(
        $rutaPythonScript
        "--path", $directorio
        "--prev", $rutaEstadoPrevio
        "--threshold", $umbral
        "--output", $rutaLogSalida
    )
    

    & python $pythonArgs

    if ($LASTEXITCODE -eq 0) {
        Write-Host "Analisis completado exitosamente. Revisar $rutaLogSalida"
    } else {
        Write-Host "Error durante la ejecucion del analisis (Código de salida: $LASTEXITCODE)." -ForegroundColor Red
    }
}
Export-ModuleMember -Function Invoke-AnalisisEspacioDisco