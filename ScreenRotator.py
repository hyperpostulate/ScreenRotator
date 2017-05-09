#!/usr/bin/env python3
# Original work: frecel [https://github.com/frecel/ScreenRotator]
# Modified by: hyperpostulate
# License: GPL3+

import os
import signal
from subprocess import call
from gi.repository import Gtk
from gi.repository import AppIndicator3 as AppIndicator

APPINDICATOR_ID = "screenrotator"
orientation = "normal"

def main():
    indicator = AppIndicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('./icon.svg'), AppIndicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    Gtk.main()

def build_menu():
    menu = Gtk.Menu()
    item_header = Gtk.MenuItem('Screen Rotator')
    menu.append(item_header)
    seperator = Gtk.SeparatorMenuItem()
    menu.append(seperator)
    #flip
    # item_flip = Gtk.MenuItem('Flip')
    # item_flip.connect('activate', flip_screen)
    # menu.append(item_flip)
    #landscape
    item_landscape = Gtk.MenuItem('Normal Mode')
    item_landscape.connect('activate', make_landscape)
    menu.append(item_landscape)
    #portrait
    item_portrait = Gtk.MenuItem('Portrait Mode')
    item_portrait.connect('activate', make_portrait)
    menu.append(item_portrait)
    #tent
    item_tent = Gtk.MenuItem('Tent Mode')
    item_tent.connect('activate', make_tent)
    menu.append(item_tent)
    #seperator
    seperator = Gtk.SeparatorMenuItem()
    menu.append(seperator)
    #quit
    item_quit = Gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    menu.show_all()
    return menu

def make_landscape(source):
    call(["./touchscreen-normal.sh"])
    call(["xrandr", "-o", "normal"])

def make_portrait(source):
    call(["./touchscreen-left.sh"])
    call(["xrandr", "-o", "left"])

def make_tent(source):
    call(["./touchscreen-inverted.sh"])
    call(["xrandr", "-o", "inverted"])



# def flip_screen(source):
#     global orientation
#     if orientation == "normal":
#         direction = "inverted"
#         call(["./touchscreen-inverted.sh"])
#     elif orientation == "inverted":
#         direction = "left"
#         call(["./touchscreen-left.sh"])
#     elif orientation == "left":
#         direction = "normal"
#         call(["./touchscreen-normal.sh"])
#     call(["xrandr", "-o", direction])
#     orientation = direction


if __name__ == "__main__":
    #make sure the screen is in normal orientation when the script starts
    call(["xrandr", "-o", orientation])
    call(["./touchscreen-normal.sh"])
    #keyboard interrupt handler
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
