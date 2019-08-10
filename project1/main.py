import sys
import copy
from Parser import Parser
from FCFS import FCFS
from SJF import SJF
from RR import RR
from FileHandler import FileHandler
from Utils import get_stats_str, verbose_mode


def main():
    verbose = verbose_mode(sys.argv)
    parser = Parser()
    output = FileHandler("results.txt")

    processes = parser.parse_file(sys.argv[1])

    # Creates a FCFS scheduler
    fcfs_p_copy = copy.deepcopy(processes)
    fcfs = FCFS(fcfs_p_copy)
    fcfs_stats = fcfs.run()

    # Creates a SJF Scheduler
    sjf_processes_copy = copy.deepcopy(processes)
    sjf = SJF(sjf_processes_copy)
    sjf_stats = sjf.run()

    # Creates a RR Scheduler
    rr_processes_copy = copy.deepcopy(processes)
    rr = RR(rr_processes_copy)
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
