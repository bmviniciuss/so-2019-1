class Process:
    def __init__(self, pid, t_arrival, cpu_peak):
        self.pid = pid
        self.t_arrival = t_arrival
        self.cpu_peak = cpu_peak
        self.active = False
        self.t_active = 0
        self.t_wait = 0
        self.t_entry = None
        self.done = False
        self.t_done = None
    
    def start_process(self, time):
        self.active = True # makes process's active flag true
        self.t_entry = time  # save the time that the process starts working

    def finish_process(self, time):
        self.active = False  # process has been finished
        self.done = True # makes process done flag true
        self.t_done = time  # save the time of doness

    def run(self):
        self.t_active += 1  # increment process's active timer 

    def is_done(self):
        return  self.t_active < self.cpu_peak

    def __str__(self):
        string =  "## Process {}\n".format(self.pid)
        string += "Arrival: {}\n".format(self.t_arrival)
        string += "CPU Peak: {}\n".format(self.cpu_peak)
        string += "Active: {}\n".format(self.active)
        string += "Done: {}\n".format(self.done)
        string += "T_Entry: {}\n".format(self.t_entry)
        string += "T_Waiting: {}\n".format(self.t_wait)
        string += "T_Active: {}\n".format(self.t_active)
        string += "T_Done: {}\n".format(self.t_done)
        return string