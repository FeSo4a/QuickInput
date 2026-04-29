import time

import keyboard
import mouse

from song import *


def key_press(args, standard_keys):
    print('长按2s后开始,长按F8停止。')
    time.sleep(2)
    beep_sound()

    for key in args.press:
        if key in standard_keys:
            keyboard.press(key)

    while not keyboard.is_pressed('f8'):
        time.sleep(0.1)

    else:
        for key in args.press:
            if key in standard_keys:
                keyboard.release(key)
        beep_sound()
        print('已停止。')


def mouse_press(args, standard_mouse):
    print('长按2s后开始,长按F8停止。')
    time.sleep(2)
    beep_sound()

    for key in args.pmouse:
        if key in standard_mouse:
            mouse.press(key)

    while not keyboard.is_pressed('f8'):
        time.sleep(0.1)

    else:
        for key in args.pmouse:
            if key in standard_mouse:
                mouse.release(key)
        beep_sound()
        print('已停止。')
