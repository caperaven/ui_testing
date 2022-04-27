def get_name(args):
    if "id" in args:
        return args["id"]

    if "query" in args:
        return args["query"]
