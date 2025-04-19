#!/bin/bash

PARAM_FILE="$1"

CHANGED_FILES=$(git diff --name-only)

NEED_COMMIT=false

while IFS= read -r file; do
    while IFS= read -r class; do
        if [ "$file" == "$class" ]; then
            echo "Обнаружены изменения в файле: $file"
            NEED_COMMIT=true
            break
        fi
    done <"$PARAM_FILE"
done <<<"$CHANGED_FILES"

if [ "$NEED_COMMIT" = true ]; then
    git add .
    git commit -m "autocommit: changes in classes from $PARAM_FILE"
    echo "Коммит выполнен"
else
    echo "Изменения в указанных файлах не обнаружены, коммит не требуется"
fi
