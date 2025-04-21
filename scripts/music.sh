#!/bin/bash

MUSIC_FILE="$1"
GIF_FILE="$2"

mpg321 $MUSIC_FILE >/dev/null 2>&1 &
MPG321_PID=$!

timg -g30x30 $GIF_FILE &
TIMG_PID=$!

wait $MPG321_PID

kill $TIMG_PID
