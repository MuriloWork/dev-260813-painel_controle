param(
    [string]$Aba = $null,
    [string]$Choice = $null
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$PSDefaultParameterValues['Out-File:Encoding'] = 'utf8'
chcp 65001 > $null

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
. "$scriptDir\painel_view.ps1"

$env_base_path = "C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\.env.base"
$currentEnvPainel = ""
$venvPath = ""
if (Test-Path $env_base_path) {
    Get-Content $env_base_path -Encoding UTF8 | ForEach-Object {
        if ($_ -match '^ENV_PAINEL=(.*)$') {
            $currentEnvPainel = $matches[1].Trim().Trim('"').Trim("'")
        }
        if ($_ -match '^PJ_VENV_PATH_2=(.*)$') {
            $venvPath = $matches[1].Trim().Trim('"').Trim("'")
        }
    }
}

$painelRoot = $null
if ($currentEnvPainel) {
    $envPainelFile = Get-Item $currentEnvPainel -ErrorAction SilentlyContinue
    if ($envPainelFile) {
        $painelRoot = $envPainelFile.Directory.Parent.Parent.FullName
    }
}
if (-not $painelRoot) {
    $painelRoot = (Get-Item $scriptDir).Parent.Parent.FullName
}

if (-not [string]::IsNullOrEmpty($venvPath)) {
    Write-Host "[INFO] Venv: $venvPath" -ForegroundColor Cyan
}

if (-not [string]::IsNullOrEmpty($currentEnvPainel)) {
    $env:ENV_PAINEL = $currentEnvPainel
}

& python -c "import sys; sys.path.insert(0, r'$painelRoot\src'); from utils.init_utils import env_loader; env_loader.load_environment_main()" 2>$null
if ($LASTEXITCODE -ne 0 -and $LASTEXITCODE -ne $null) {
    Write-Host "[AVISO] env_loader nao pode ser carregado (painelRoot=$painelRoot)" -ForegroundColor DarkYellow
}

function Confirm-EnvPainel {
    param([string]$CurrentEnvPainel)
    
    Write-Host ""
    Write-Host "========================================"
    Write-Host "  Confirmar Projeto"
    Write-Host "========================================"
    Write-Host ""
    Write-Host "Painel config: $CurrentEnvPainel" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "[ENTER] Confirmar e abrir abas" -ForegroundColor Gray
    Write-Host "[S]     Sair" -ForegroundColor Gray
    Write-Host "[Novo]  Informar novo caminho do JSON" -ForegroundColor Gray
    Write-Host ""
    
    $input = Read-Host "Opção (ENTER para confirmar)"
    
    if ($input -eq 's' -or $input -eq 'S') {
        exit 0
    }
    
    if ([string]::IsNullOrWhiteSpace($input)) {
        return $CurrentEnvPainel
    }
    
    $newRawPath = $input.Trim().Trim('"').Trim("'")
    $resolvedPath = [System.IO.Path]::GetFullPath($newRawPath)
    
    if ((Test-Path $resolvedPath) -and ((Get-Item $resolvedPath) -is [System.IO.DirectoryInfo])) {
        $resolvedPath = Join-Path $resolvedPath "set_painel_pipeline_paths.json"
    }
    
    if (-not (Test-Path $resolvedPath)) {
        Write-Host "[ERRO] JSON nao encontrado em: $resolvedPath" -ForegroundColor Red
        return $CurrentEnvPainel
    }
    
    try {
        $content = Get-Content $env_base_path -Raw
        $content = $content -replace '(?m)^ENV_PAINEL=.*$', "ENV_PAINEL=`"$resolvedPath`""
        Set-Content -Path $env_base_path -Value $content -NoNewline -Encoding UTF8
        Write-Host "[OK] .env.base atualizado para: $resolvedPath" -ForegroundColor Green
    } catch {
        Write-Host "[ERRO] Falha ao atualizar .env.base: $_" -ForegroundColor Red
    }
    
    return $resolvedPath
}

if (-not $Aba) {
    $currentEnvPainel = Confirm-EnvPainel -CurrentEnvPainel $currentEnvPainel
    
    Write-Host ""
    Write-Host "Projeto validado. Abrindo 3 abas..." -ForegroundColor Green
    if (-not [string]::IsNullOrEmpty($venvPath)) {
        Write-Host "[INFO] Venv: $venvPath" -ForegroundColor Cyan
    }
    
    $scriptPath = $MyInvocation.MyCommand.Path
    
    Start-Process "wt" -ArgumentList "-w","0","nt","--title","SHELL","powershell.exe","-NoExit","-File","""$scriptPath""","-Aba","shell"
    Start-Process "wt" -ArgumentList "-w","0","nt","--title","PARSE","powershell.exe","-NoExit","-File","""$scriptPath""","-Aba","parse"
    Start-Process "wt" -ArgumentList "-w","0","nt","--title","LOGS","powershell.exe","-NoExit","-File","""$scriptPath""","-Aba","logs"
    
    Start-Sleep -Seconds 1
    $host.UI.RawUI.WindowTitle = "Fechando..."
    Stop-Process -Id $PID -Force
}

$menu_path = "$painelRoot\src\config\set_painel_menu.json"
if (-not (Test-Path $menu_path)) {
    Write-Host "[ERRO] Menu config nao encontrado: $menu_path" -ForegroundColor Red
    exit 1
}

$config = Get-Content -Path $menu_path -Encoding UTF8 | ConvertFrom-Json

# Carregar var_ref do set_painel_actions_data_paths.json para placeholders dinamicos
$actionsDataPath = "$painelRoot\src\config\set_painel_actions_data_paths.json"
$actionsData = $null
if (Test-Path $actionsDataPath) {
    $actionsData = Get-Content -Path $actionsDataPath -Encoding UTF8 | ConvertFrom-Json
}

$validAbas = @("shell", "parse", "logs")
if ($Aba -and $Aba -notin $validAbas) {
    Write-Host "Aba inválida: $Aba. Abas disponíveis: $($validAbas -join ', ')" -ForegroundColor Red
    exit 1
}

$abaConfig = $config.$Aba.commands

function Run-ShellCommand {
    param([string]$Option, [array]$Commands)
    
    $isValidNumber = $Option -match '^\d+$'
    $index = [int]$Option - 1
    if ($isValidNumber -and $index -ge 0 -and $index -lt $Commands.Count) {
        $commandInfo = $Commands[$index]
        Write-Host "`n--- Iniciando: $($commandInfo.description) ---" -ForegroundColor Yellow
        Write-Host "Abrindo em novo terminal..." -ForegroundColor Gray
        
        $scriptPath = $commandInfo.command
        $arguments = $commandInfo.arguments
        
        if ($commandInfo.PSObject.Properties.Name -contains 'placeholders') {
            foreach ($placeholder in $commandInfo.placeholders) {
                $name = $placeholder.name
                $prompt = $placeholder.prompt
                $default = $placeholder.default

                # Resolver default_var_ref do set_painel_actions_data_paths.json
                if ([string]::IsNullOrWhiteSpace($default) -and $placeholder.PSObject.Properties.Name -contains 'default_var_ref' -and $actionsData) {
                    $varRef = $placeholder.default_var_ref
                    $section = $null
                    if ($actionsData.data_paths.sources.PSObject.Properties.Name -contains $varRef) {
                        $section = $actionsData.data_paths.sources
                    } elseif ($actionsData.data_paths.targets.PSObject.Properties.Name -contains $varRef) {
                        $section = $actionsData.data_paths.targets
                    } elseif ($actionsData.data_paths.database.PSObject.Properties.Name -contains $varRef) {
                        $section = $actionsData.data_paths.database
                    }
                    if ($section) {
                        $refValue = $section.$varRef
                        if ($refValue -is [string]) {
                            $raw = Join-Path $painelRoot $refValue
                            $default = [System.IO.Path]::GetFullPath($raw)
                        } elseif ($refValue.paths) {
                            $pathList = @()
                            foreach ($p in $refValue.paths) {
                                $raw = Join-Path $painelRoot $p
                                $fullPath = [System.IO.Path]::GetFullPath($raw)
                                if ($fullPath -match '\s') {
                                    $fullPath = "`"$fullPath`""
                                }
                                $pathList += $fullPath
                            }
                            $default = $pathList -join ' '
                        } elseif ($refValue.path) {
                            $raw = Join-Path $painelRoot $refValue.path
                            $default = [System.IO.Path]::GetFullPath($raw)
                        } else {
                            $default = $painelRoot
                        }
                    }
                }

                $inputValue = Read-Host "$prompt (default: $default)"
                if ([string]::IsNullOrWhiteSpace($inputValue)) {
                    $inputValue = $default
                }

                $inputValue = $inputValue.Trim()
                if ($inputValue -match '\s' -and $inputValue -notmatch '"') {
                    # Single unquoted path with spaces → wrap
                    $inputValue = "`"$inputValue`""
                }
                $arguments = $arguments.Replace("`$$name", $inputValue)
            }
        }

        $commandType = $commandInfo.type

        if ($commandType -eq 'python') {
            if ([string]::IsNullOrEmpty($venvPath)) {
                $venvPath = "C:\Users\muril\venvs\pessoal"
            }
            $pythonExe = Join-Path $venvPath "Scripts\python.exe"
            $fullScriptPath = Join-Path $painelRoot $scriptPath
            $fullCommand = "& `"$pythonExe`" `"$fullScriptPath`" $arguments"
        }
        elseif ($commandType -eq 'module') {
            if ([string]::IsNullOrEmpty($venvPath)) {
                $venvPath = "C:\Users\muril\venvs\pessoal"
            }
            $pythonExe = Join-Path $venvPath "Scripts\python.exe"
            $moduleDir = Join-Path $painelRoot $commandInfo.chdir
            $fullCommand = "Set-Location '$moduleDir'; & `"$pythonExe`" -m $scriptPath $arguments"
        }
        elseif ($commandType -eq 'shell' -and $scriptPath -eq 'powershell') {
            $fullCommand = $arguments
        }
        else {
            $fullCommand = "& `"$scriptPath`" $arguments"
        }

        $bytes = [System.Text.Encoding]::Unicode.GetBytes($fullCommand)
        $encoded = [Convert]::ToBase64String($bytes)
        Start-Process powershell "-NoExit -EncodedCommand $encoded"
    } else {
        Write-Host "Opção inválida: $Option" -ForegroundColor Red
    }
}

if ($Choice) {
    Run-ShellCommand -Option $Choice -Commands $abaConfig
} else {
    do {
        Show-Menu -AbaName $Aba.ToUpper() -Commands $abaConfig
        $choice = Read-Host "Escolha uma opcao"
        
        if ($choice -ne 'q' -and $choice -ne 'Q') {
            Run-ShellCommand -Option $choice -Commands $abaConfig
            Read-Host "`nPressione Enter para voltar ao menu..."
        }
    } while ($choice -ne 'q' -and $choice -ne 'Q')
}
