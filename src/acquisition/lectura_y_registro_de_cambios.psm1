function Invoke-LecturaRegistro { 
    $watcher = New-Object System.IO.FileSystemWatcher
    $watcher.Path = "$env:USERPROFILE"
    $watcher.EnableRaisingEvents = $true
    $watcher.IncludeSubdirectories = $true

    $action =
    {
        $logObj = [PSCustomObject]@{
            timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
            run_id    = [guid]::NewGuid().ToString()
            module    = "FileWatcher"
            level     = "INFO"
            event     = $event.SourceEventArgs.ChangeType
            details   = $event.SourceEventArgs.FullPath
        }

        # Mostrar en consola
        Write-Host ("{0,-20} {1,-10} {2}" -f $logObj.timestamp, $logObj.event, $logObj.details)


        $linea = "{0,-20} {1,-10} {2}" -f $logObj.timestamp, $logObj.event, $logObj.details
        Add-Content -Path "$env:USERPROFILE\reporte_de_cambios.txt" -Value $linea

        $json = $logObj | ConvertTo-Json -Compress
        Add-Content -Path "$env:USERPROFILE\reporte_de_cambios.json" -Value $json
    }

    #Registrar eventos
    $createdEvent = Register-ObjectEvent $watcher 'Created' -Action $action
    $changedEvent = Register-ObjectEvent $watcher 'Changed' -Action $action
    $deletedEvent = Register-ObjectEvent $watcher 'Deleted' -Action $action
    $renamedEvent = Register-ObjectEvent $watcher 'Renamed' -Action $action

    Write-Host "Watcher iniciado. Presiona enter para detenerlo..."

    #Esperar a que se presione el enter
    [void][System.Console]::ReadLine()

    #liberar watch y desregistar los eventos
    Unregister-Event -SubscriptionId $createdEvent.Id
    Unregister-Event -SubscriptionId $changedEvent.Id
    Unregister-Event -SubscriptionId $deletedEvent.Id
    Unregister-Event -SubscriptionId $renamedEvent.Id
    $watcher.Dispose()

    Write-Host "Watcher detenido."
    Write-Host "Reporte TXT generado."
    Write-Host "Log JSON generado."


}

