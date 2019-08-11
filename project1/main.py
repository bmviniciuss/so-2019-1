import sys
import copy
from Parser import Parser
from FCFS import FCFS
from SJF import SJF
from RR import RR
from OutputHandler import OutputHandler
from Utils import get_stats_str, verbose_mode


def main():
    verbose = verbose_mode(sys.argv)
    parser = Parser()
    output = OutputHandler("results.txt")

    processes = parser.parse_file(sys.argv[1])

    # Creates a FCFS scheduler
    fcfs = FCFS(copy.deepcopy(processes))
    fcfs_stats = fcfs.run()

    # Creates a SJF Scheduler
    sjf = SJF(copy.deepcopy(processes))
    sjf_stats = sjf.run()

    # Creates a RR Scheduler
    rr = RR(copy.deepcopy(processes))
    rr_stats = rr.run()

    # If verbose. print to terminal
    if verbose:
        print(get_stats_str("FCFS", fcfs_stats), end="")
        print(get_stats_str("SJF", sjf_stats), end="")
        print(get_stats_str("RR", rr_stats), end="")

    # Done - writing results to output file
    output.write_to_file(get_stats_str("FCFS", fcfs_stats),
                         get_stats_str("SJF", sjf_stats), get_stats_str("RR", rr_stats))


if __name__ == "__main__":
    main()
