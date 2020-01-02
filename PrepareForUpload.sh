#!/bin/sh
currentDir=$(pwd)
currentDirName=$(basename "$currentDir")
devDirName="$1"
destinationName="$2"
if [ $currentDirName==$devDirName ] ; then
{
    destinationName="../$destinationName"
}
elif [ -d "$currentDir/$devDirName"] ; then
{
    currentDir="$currentDir/$devDirName"
}
else
{
    echo "$devDirName doesn't exist"
    exit 1
}
fi

if [ -d $destinationName ] ; then
    echo "$destinationName exists, deleting"
    rm -rfd $destinationName
fi

mkdir $destinationName
rsync -ahm --include='/thumbnail.jpg' --include='/descriptor.mod' --include='/README.md' --exclude='*.7z' --exclude='/*.*' --exclude='/.*' --exclude='/tutorial' --exclude='*.sh' --exclude='*.ps1' --exclude='*.psd' --exclude='*.py' . $destinationName
cp -f "$destinationName/descriptor.mod" "$destinationName/../$2.mod"
