$currentDir = Get-Location
$currentDirName = Get-Location | Get-Item
$destinationName = "equestria"
if($currentDirName.Name -eq "equestria_dev")
{
    $destinationName = "..\$destinationName"
}
elseif (Test-Path -Path "$currentDir\equestria_dev")
{
    $currentDir = "$currentDir\equestria_dev"
}
else
{
    Write-Error "equestria_dev doesn't exist"
    exit
}
if (Test-Path -Path $destinationName)
{
Remove-Item -Recurse -Force $destinationName
}
New-Item -ItemType Directory -Force -Path $destinationName
Get-ChildItem -Path $currentDir -Force -Exclude @(".*", "tutorial", "equestria_dev.mod") | Copy-item -Force -Exclude @("popularities_regex.txt", "MTG_notes.txt", "regexes.txt", "*.psd", "*.py", "*.ps1", "*.sh", "*.7z") -Container -Recurse -Verbose -Destination $destinationName
Copy-Item "$destinationName/equestria.mod" -Force -Destination "$destinationName/.."
