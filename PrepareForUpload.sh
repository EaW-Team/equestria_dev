currentDir=$(pwd)
currentDirName=$(basename "$currentDir")
destinationName="equestria"
if [ $currentDirName=="equestria_dev" ] ; then
{
    destinationName="../$destinationName"
}
elif [ -d "$currentDir/equestria_dev"] ; then
{
    currentDir="$currentDir/equestria_dev"
}
else
{
    echo "equestria_dev doesn't exist"
    exit 1
}
fi

if [ -d $destinationName ] ; then
    echo "$destinationName exists, deleting"
    rm -rfd $destinationName
fi

mkdir $destinationName
rsync --recursive --exclude='*.7z' --exclude='regexes.txt' --exclude='MTG_notes.txt' --exclude='popularities_regex.txt' --exclude='/.*' --exclude='*.sh' --exclude='*.ps1' --exclude='*.psd' --exclude='*.py' --exclude='equestria_dev.mod' . $destinationName
cp -f "$destinationName/equestria.mod" "$destinationName/.."
