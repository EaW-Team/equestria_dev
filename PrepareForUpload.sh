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
rsync -avhm --include='/changelog.txt' --include='/art_credits.txt' --include='/equestria.jpg' --include='/equestria.mod' --include='/descriptor.mod' --include='/README.md' --exclude='*.7z' --exclude='/*.*' --exclude='/.*' --exclude='/tutorial' --exclude='*.sh' --exclude='*.ps1' --exclude='*.psd' --exclude='*.py' . $destinationName
cp -f "$destinationName/equestria.mod" "$destinationName/.."
