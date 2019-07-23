import sys
from Parser import Parser
from FCFS import FCFS
from FileHandler import FileHandler
from Utils import get_stats_str


def main():
    debug = True
    parser = Parser()
    output = FileHandler("results.txt")

    processes = parser.parse_file(sys.argv[1])

    # Creates a FCFS scheduler
    fcfs = FCFS(processes)
    fcfs_stats = fcfs.run()

    # Done - writing results to output file
    output.write_to_file(get_stats_str("FCFS", fcfs_stats))

    # If Debug print to terminal
    if debug:
        print(get_stats_str("FCFS", fcfs_stats))


if __name__ == "__main__":
    main()
