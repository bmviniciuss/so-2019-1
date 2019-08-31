
def get_stats_str(type, value):
    """Function that return the output formatted for a single algorithm"""
    str_rep = type + " " + str(value)

    return str_rep + "\n"


def verbose_mode(args):
    """Check if verbose mode is active in args, to show output on the terminal"""
    verbose = ["-v", "-V", "--verbose"]
    for v in verbose:
        if v in args:
            return True
    return False
