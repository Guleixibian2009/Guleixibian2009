<# This is a basic program to set up your IT class's computer. #>
<# Be sure to run as ADMIN. #>

Set-Variable http_proxy=http://192.168.0.24:31181
Set-Variable https_proxy=http://192.168.0.24:31181
setx.exe "http_proxy" "http://192.168.0.24:31181" /m
setx.exe "https_proxy" "http://192.168.0.24:31181" /m
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
if (choco -v) {
    choco install croc
    setx.exe "PATH" "%PATH%; C:\ProgramData\chocolatey\lib\croc\tools" /m
    RefreshEnv.cmd
}