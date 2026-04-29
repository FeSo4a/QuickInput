def if_press_key(args) -> bool:
    return (
            args.press and
            not args.key and
            not args.time and
            not args.view and
            not args.pmouse and
            not args.func
    )


def if_press_mouse(args) -> bool:
    return (
            args.pmouse and
            not args.key and
            not args.time and
            not args.view and
            not args.press and
            not args.func
    )
