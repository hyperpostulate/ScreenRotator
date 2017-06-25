#!/bin/sh
# Author: hyperpostulate
# Disables touchpad and keyboard
#Change TOUCHPAD_ID and KEYBOARD_ID with tour  device IDs. [Use xinput -list to find out device IDs]
TOUCHPAD_ID=11
KEYBOARD_ID=14
xinput --disable $TOUCHPAD_ID
xinput --disable $KEYBOARD_ID