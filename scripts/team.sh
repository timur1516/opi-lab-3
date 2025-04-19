#!/bin/bash

JAR_PATH="$1"
OUTPUT_ZIP="$2"

TEMP_DIR="tmp/revisions"
REVISIONS=("HEAD~1" "HEAD~2" "HEAD~3" "HEAD~4")

mkdir -p "$TEMP_DIR"

CURRENT_BRANCH="$(git rev-parse HEAD)"

JAR_FILES=()

for REV in "${REVISIONS[@]}"; do

    if ! git checkout "$REV"; then
        echo "Failed to checkout $REV"
        break
    fi

    ninja build

    OUTPUT_JAR="$TEMP_DIR/$(git rev-parse --short HEAD).jar"

    cp "$JAR_PATH" "$OUTPUT_JAR"

    JAR_FILES+=("$OUTPUT_JAR")

    ninja clean

    git checkout "$CURRENT_BRANCH"
done

zip "$OUTPUT_ZIP" "${JAR_FILES[@]}"

rm -rf "$TEMP_DIR"
