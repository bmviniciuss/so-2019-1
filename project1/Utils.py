
def get_stats_str(type, avgs):
    """Function that return the output formatted for a single scheduler"""
    str_rep = type + " "

    for avg in avgs:
        str_rep += "{:.1f} ".format(avg)

    return str_rep + "\n"


def verbose_mode(args):
    verbose = ["-v", "-V", "--verbose"]
    for v in verbose:
        if v in args:
            return True
    return False
