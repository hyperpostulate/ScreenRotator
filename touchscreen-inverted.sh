#!/bin/sh
# Author: hyperpostulate
#Converts touchscreen to inverted mode
#"SIS0457:00 0457:1136" is like "your-device-id-goes-here"
xinput set-prop "SIS0457:00 0457:1136" --type=float "Coordinate Transformation Matrix" -1 0 1 0 -1 1 0 0 1

Process finished with exit code 0
