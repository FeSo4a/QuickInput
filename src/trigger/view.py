def if_view(args) -> bool:
    return (
            args.view and
            not args.press and
            not args.key and
            not args.time and
            not args.pmouse and
            not args.mouse and
            not args.func
    )
