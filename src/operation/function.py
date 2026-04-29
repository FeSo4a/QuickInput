import json
import os
import time
from json import JSONDecodeError
from typing import *

import keyboard
import mouse

from song import *


def load_func(args) -> Optional[list]:
    # noinspection PyBroadException
    try:
        with open(f'func/{args.func}', 'r', encoding='utf-8') as func:
            func = json.load(func)
            return func

    except FileNotFoundError:
        print('文件不存在。')
        return None

    except JSONDecodeError:
        print('文件格式错误。')
        return None


def show_func(func) -> None:
    print('已加载宏：')
    for key in func:
        print(f'{key.get("key", "")} -> {key.get("keys")}{key.get("mouses", "")}')


def run_func(func) -> None:
    if type(func) != list:
        return

    beep_sound()
    print('宏模式启动，按下F8退出。')
    show_func(func)

    while not keyboard.is_pressed('F8'):
        for key in func:
            trigger_key = key.get('key', None)
            if trigger_key and keyboard.is_pressed(trigger_key):
                keys = key.get('keys', [])
                mouses = key.get('mouses', [])
                for k in keys:
                    keyboard.press_and_release(k)
                for m in mouses:
                    mouse.click(m)

                # 等待按键释放，避免重复触发
                while keyboard.is_pressed(trigger_key):
                    time.sleep(0.05)

        time.sleep(0.01)  # 降低CPU占用

    else:
        print('已退出宏模式。')
        beep_sound()


def view_func():
    for filename in os.listdir('func'):
        print(filename)
