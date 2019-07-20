import sys
from Parser import Parser

def main():
    parser = Parser()
    processes = parser.parse_file(sys.argv[1])
    print(processes)

if __name__ == "__main__":
    main()