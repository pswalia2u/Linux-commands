$ComputerName= Read-host "Enter the Computer Name"
$StoppedServices= Get-Service | Where-Object -Property Status -EQ "Stopped"
Write-Output $StoppedServices