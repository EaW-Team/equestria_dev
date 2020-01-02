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
if [ ! -f "thumbnail.png" ]; then
    sudo apt-get update && sudo apt-get install imagemagick
    convert $3 thumbnail.png
fi
sed -i "s/picture=.*//g" "descriptor.mod"
rsync -ahm --include="/thumbnail.png" --include='/descriptor.mod' --include='/README.md' --exclude='*.7z' --exclude='/*.*' --exclude='/.*' --exclude='/tutorial' --exclude='*.sh' --exclude='*.ps1' --exclude='*.psd' --exclude='*.py' . $destinationName
cp -f "$destinationName/descriptor.mod" "$destinationName/../$2.mod"
