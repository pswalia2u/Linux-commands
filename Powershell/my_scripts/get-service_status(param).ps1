Param(
    [Parameter(Mandatory=$true)]
    [string[]]
    $Computername
    )

    $Allservices=Get-Service -ComputerName $Computername 

    foreach($service in $Allservices) #getting each service one by one
    {
        $status=$service.Status
        if($status -eq "Running")
        {
            Write-Output "Service $service is Running Properly"
        }
        else 
        {
            Write-Output "Service $service is not Running."
            
        }
    }