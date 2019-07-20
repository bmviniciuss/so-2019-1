from Process import Process
import os

class Parser(object):
    def open_file(self,filename):
        if(filename):
            base_dir = os.path.dirname(__file__)
            file_path = os.path.join(base_dir, filename)
            file = open(file_path, "r")
            self.file = file
    
    def parse_file(self, filename):
        self.open_file(filename)
        if self.file and self.file.mode == "r":
            p_counter = 0
            processes = []
            for line in self.file:
                t_arrival, cpu_peak = self.parse_line(line)
                process = Process(p_counter, t_arrival, cpu_peak)
                processes.append(process)
                p_counter += 1 
            print(processes)
            return processes
            self.close_file()

    def parse_line(self, line):
        values = line.split()
        if len(values) == 2:
            t_arrival = int(values[0])
            cpu_peak = int(values[1])
            return [t_arrival, cpu_peak]

    def close_file(self):
        self.file.close()