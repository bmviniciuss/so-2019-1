import sys
import copy
from InputHandler import InputHandler
from OutputHandler import OutputHandler
from Utils import get_stats_str, verbose_mode
from FIFO import FIFO


def main():
    verbose = verbose_mode(sys.argv)
    input_handler = InputHandler()
    output_handler = OutputHandler("results.txt")

    [memory_blocks, references] = input_handler.parse_file(sys.argv[1])

    fifo = FIFO(memory_blocks, references)
    fifo_stats = fifo.run()
    fifo_stats_str = get_stats_str("FIFO", fifo_stats)

    output_handler.write_to_file(fifo_stats_str)

    if verbose:
        print(fifo_stats_str)


if __name__ == "__main__":
    main()
