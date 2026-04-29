def if_func(args):
    return (
            args.func and
            not args.mouse and
            not args.time and
            not args.press and
            not args.view and
            not args.key
    )


def if_showfunc(args):
    return (
            args.showfunc and
            not args.func and
            not args.mouse and
            not args.time and
            not args.press and
            not args.view and
            not args.key
    )
