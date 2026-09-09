function Show-Menu {
    param([string]$AbaName, [array]$Commands)

    Clear-Host
    Write-Host "========================================"
    Write-Host "      PAINEL DE CONTROLE - $AbaName"
    Write-Host "========================================"
    Write-Host ""
    Write-Host "Config: $currentEnvPainel" -ForegroundColor Gray
    if (-not [string]::IsNullOrEmpty($venvPath)) {
        Write-Host "Venv:   $venvPath" -ForegroundColor Gray
    }
    Write-Host ""

    for ($i = 0; $i -lt $Commands.Count; $i++) {
        $cmdInfo = $Commands[$i]
        $index = $i + 1
        $description = $cmdInfo.description
        $command = $cmdInfo.command
        $arguments = $cmdInfo.arguments

        $fullCommand = "$command $arguments".Trim()

        Write-Host "  [$index] $description" -ForegroundColor Cyan
        if ($fullCommand) {
            Write-Host "      $fullCommand" -ForegroundColor Gray
        }
    }

    Write-Host ""
    Write-Host "   Q. Sair"
    Write-Host ""
}
