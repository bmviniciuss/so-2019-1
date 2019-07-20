import sys

from Parser import Parser
from FCFS import FCFS

def main():
    parser = Parser()
    processes = parser.parse_file(sys.argv[1])
    fcfs = FCFS(processes)
    fcfs_stats = fcfs.run()

if __name__ == "__main__":
    main()