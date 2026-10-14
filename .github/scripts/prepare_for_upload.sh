#!/bin/sh
set -eu

destination=$1
thumbnail_source=$2
repository_root=$(CDPATH= cd -- "$(dirname "$0")/../.." && pwd)

cd "$repository_root"

if [ -e "$destination" ]; then
    echo "$destination already exists" >&2
    exit 1
fi

mkdir -p "$destination"
rsync -ahm \
    --include='/thumbnail.png' \
    --include='/descriptor.mod' \
    --include='/README.md' \
    --exclude='*.7z' \
    --exclude='/*.*' \
    --exclude='/.*' \
    --exclude='/build' \
    --exclude='/tutorial' \
    --exclude='/scripts' \
    --exclude='*.sh' \
    --exclude='*.ps1' \
    --exclude='*.psd' \
    --exclude='*.py' \
    ./ "$destination/"

if [ ! -f "$destination/thumbnail.png" ]; then
    magick "$thumbnail_source" "$destination/thumbnail.png" ||
        convert "$thumbnail_source" "$destination/thumbnail.png"
fi

sed -i '/^picture=/d' "$destination/descriptor.mod"
cp "$destination/descriptor.mod" "${destination}.mod"
