def if_click_key(args) -> bool:
    return (
            args.key and
            args.time and
            not args.press and
            not args.view and
            not args.mouse and
            not args.func
    )


def if_click_mouse(args) -> bool:
    return (
            args.mouse and
            args.time and
            not args.press and
            not args.view and
            not args.key and
            not args.func
    )
