def get_name(args):
    if "id" in args:
        return args["id"]

    if "query" in args:
        return args["query"]


def get_eval(args):
    if "eval" in args:
        return args["eval"]
    else:
        return None
