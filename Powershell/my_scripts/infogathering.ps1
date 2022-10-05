#OS Description
$OS=(Get-CimInstance -ClassName Win32_OperatingSystem).Caption
$OS

#Disk Freespace on OS Drive
$size_bytes=(Get-CimInstance -ClassName Win32_LogicalDisk | Where-Object -Property DeviceID -eq "D:").Size
$size_GiB=($size_bytes)/1GB
$size_GiB

#Amount of System Memory
((Get-CimInstance -ClassName CIM_PhysicalMemory).Capacity | measure -Sum).Sum 
$All_rams=(Get-CimInstance -ClassName CIM_PhysicalMemory).Capacity
$total_ram=0
foreach($ram in $All_rams)
{
    $total_ram+=$ram
}
$total_ram/1GB

#Last Reboot of System
$LastReboot=(Get-CimInstance -ClassName Win32_OperatingSystem).LastBootUpTime
$LastReboot

#IP Address & DNS Name
$public_IP=(curl ifconfig.me).Content
$hostname=HOSTNAME.EXE
$dns_server=nslookup.exe $hostname
$dns_server

