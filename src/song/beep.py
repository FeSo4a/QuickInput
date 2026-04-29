import platform


def beep_sound():
    system = platform.system()

    if system == "Windows":
        import winsound
        winsound.Beep(1000, 500)  # 频率1000Hz，持续500ms
    else:
        # Linux/macOS 使用终端蜂鸣
        print('\a', end='', flush=True)
