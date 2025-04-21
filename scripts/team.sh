#!/bin/bash

JAR_PATH="$1"
OUTPUT_ZIP="$2"
FILE_EXTENSION="$3"
TMP_DIR="$4/revisions"

REVISIONS=("HEAD~1" "HEAD~2" "HEAD~3" "HEAD~4")

mkdir -p "$TMP_DIR"

CURRENT_BRANCH="$(git rev-parse HEAD)"

JAR_FILES=()

for REV in "${REVISIONS[@]}"; do

    if ! git checkout "$REV" >/dev/null 2>&1; then
        echo "Не удалось переключиться на ревизию $REV"
        git checkout "$CURRENT_BRANCH" >/dev/null
        break
    fi

    ninja build >/dev/null

    OUTPUT_JAR="$TMP_DIR/$(git rev-parse --short HEAD).$FILE_EXTENSION"

    cp "$JAR_PATH" "$OUTPUT_JAR"

    JAR_FILES+=("$OUTPUT_JAR")

    ninja clean >/dev/null

    git checkout "$CURRENT_BRANCH" >/dev/null
done

zip "$OUTPUT_ZIP" "${JAR_FILES[@]}"

rm -rf "$TMP_DIR"
