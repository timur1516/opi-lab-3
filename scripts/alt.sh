#!/bin/bash

REPLACEMENTS_FILE="$1"
FILES_FOR_ALT_FILE="$2"

while IFS= read -r file; do
    echo "Выполняется замена в файле $file"
    sed -i -f $REPLACEMENTS_FILE $file
done <"$FILES_FOR_ALT_FILE"

ninja build >/dev/null
