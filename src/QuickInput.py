import argparse
from typing import *
import os
from operation import *
from trigger import *

standard_keys: Final[list] = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12',
    'enter', 'esc', 'tab', 'backspace', 'delete', 'space',
    'up', 'down', 'left', 'right',
    'ctrl', 'alt', 'shift', 'win',
    'caps lock', 'num lock', 'scroll lock'
]
standard_mouse: Final[list] = [
    'left', 'right', 'middle'
]


def main():
    os.makedirs('func', exist_ok=True)

    parser = argparse.ArgumentParser(
        description='快速键入工具 v1.0.0\nBy FeSo4a\n使用MIT许可证',
        epilog='''
        示例: QuickInput --key=a --key=b --key=c --time=0.5
             QuickInput --press=2 --press=3 --press=6
        宏写法：
        [
          {"key":"触发按键","keys":["触发后模拟按下按键1","2","3"],"mouses":["触发后模拟按下鼠标1","2","3"]},
          ...
        ]
        ''',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('--key', type=str, help='按下按键（支持多次传入） - 只能与time连用。', action='append')
    parser.add_argument('--mouse', type=str, help='按下鼠标（支持多次传入） - 只能与time连用。', action='append')
    parser.add_argument('--time', type=float, help='按下按键间隔（秒） - 只能与key或mouse连用')
    parser.add_argument('--press', type=str, help='模拟持续按下按键（支持多次传入） - 与其他参数冲突', action='append')
    parser.add_argument('--pmouse', type=str, help='模拟持续按下鼠标（支持多次传入） - 与其他参数冲突', action='append')
    parser.add_argument('--view', help='查看可用按键（不需要传入数据） - 与其他参数冲突', action='store_true')
    parser.add_argument('--func', type=str, help='读取宏（只能传入func文件夹里面的一个宏文件名称） - 与其他参数冲突')
    parser.add_argument('--showfunc', help='查看可用宏文件（不需要传入数据） - 与其他参数冲突', action='store_true')

    args = parser.parse_args()

    if if_click_key(args):
        key_click(args, standard_keys)
    elif if_press_key(args):
        key_press(args, standard_keys)
    elif if_press_mouse(args):
        mouse_press(args, standard_mouse)
    elif if_click_mouse(args):
        mouse_click(args, standard_mouse)
    elif if_view(args):
        print_view(standard_keys, standard_mouse)
    elif if_func(args):
        run_func(load_func(args))
    elif if_showfunc(args):
        view_func()


if __name__ == '__main__':
    main()
