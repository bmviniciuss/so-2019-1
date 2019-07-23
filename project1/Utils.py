
def get_stats_str(type, avgs):
    """Function that return the output formatted for a single scheduler"""
    str_rep = type + " "

    for avg in avgs:
        str_rep += "{:.1f} ".format(avg)

    return str_rep + "\n"
