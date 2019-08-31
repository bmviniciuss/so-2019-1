import os


class OutputHandler:
    """Class that controls the output of the program to a file"""

    def __init__(self, filename):
        self.filename = filename
        self.file = self.open_file()

    def open_file(self):
        """Open/Create the output file"""
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, self.filename)
        return open(file_path, "w")

    def write_to_file(self, *args):
        """Function that takes all algorithms stats and write to output file than closes the file."""
        final = ""
        for arg in args:
            final += arg

        self.file.write(final)
        self.file.close()
