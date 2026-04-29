import time

import keyboard
import mouse

from song import *


def key_click(args, standard_keys):
    print('连点2s后开始，长按F8停止。')
    time.sleep(2)
    beep_sound()

    while not keyboard.is_pressed('f8'):
        for key in args.key:
            if key in standard_keys:
                keyboard.press_and_release(key)
        time.sleep(args.time)

    else:
        beep_sound()
        print('已停止。')


def mouse_click(args, standard_mouse):
    print('连点2s后开始，长按F8停止。')
    time.sleep(2)
    beep_sound()

    while not keyboard.is_pressed('f8'):
        for key in args.mouse:
            if key in standard_mouse:
                mouse.click(key)
        time.sleep(args.time)

    else:
        beep_sound()
        print('已停止。')
