#!/bin/sh
# Author: hyperpostulate
# Enables touchpad and keyboard
#Change TOUCHPAD_ID and KEYBOARD_ID with tour  device IDs. [Use xinput -list to find out device IDs]
TOUCHPAD_ID=11
KEYBOARD_ID=14
xinput --enable $TOUCHPAD_ID
xinput --enable $KEYBOARD_ID