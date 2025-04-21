#!/bin/bash

REPLACEMENTS_FILE="$1"
FILES_FOR_ALT_FILE="$2"
SRC_DIR="$3"
TMP_DIR="$4"

rm -rf $TMP_DIR/$SRC_DIR
mkdir -p $TMP_DIR/$SRC_DIR
cp -r $SRC_DIR $TMP_DIR/

while IFS= read -r file; do
    sed -i -f $REPLACEMENTS_FILE $file
    echo "Выполнена замена в файле $file"
done <"$FILES_FOR_ALT_FILE"

ninja build >/dev/null

cp -r $TMP_DIR/$SRC_DIR/* $SRC_DIR/
rm -rf $TMP_DIR/$SRC_DIR
