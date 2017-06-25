#!/bin/sh
# Author: hyperpostulate
#Converts touchscreen to inverted mode
#Change TOUCHSCREEN_DEVICE_NAME with tour touchscreen device name. [Use xinput -list to find out device name]
TOUCHSCREEN_DEVICE_NAME="SIS0457:00 0457:1136"
xinput set-prop "$TOUCHSCREEN_DEVICE_NAME" --type=float "Coordinate Transformation Matrix" -1 0 1 0 -1 1 0 0 1
