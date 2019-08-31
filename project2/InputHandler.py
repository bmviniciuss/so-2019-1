import os


class InputHandler(object):
    """Class that parses a input files in the specific pattern."""

    def open_file(self, filename):
        # Open the input file
        if(filename):
            base_dir = os.path.dirname(__file__)
            file_path = os.path.join(base_dir, filename)
            file = open(file_path, "r")
            self.file = file

    def parse_file(self, filename):
        """Function that parses the file and return the number of memory_blocks and an array with the reference reference accesses"""
        self.open_file(filename)
        if self.file and self.file.mode == "r":
            c = 0
            memory_blocks = None
            references = []
            for line in self.file:
                if c == 0:
                    memory_blocks = self.parse_line(line)
                else:
                    references.append(self.parse_line(line))
                c += 1
            self.close_file()
            return [memory_blocks, references]

    def parse_line(self, line):
        """Function that parse a sigle line of the input file"""
        return int(line)

    def close_file(self):
        """Function that closes the input file"""
        self.file.close()
