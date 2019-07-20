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

    def __str__(self):
        string =  "## Process {}\n".format(self.pid)
        string += "Arrival: {}\n".format(self.t_arrival)
        string += "CPU Peak: {}\n".format(self.cpu_peak)
        string += "Active: {}\n".format(self.active)
        string += "T_Active: {}\n".format(self.t_active)
        string += "T_Waiting: {}\n".format(self.t_wait)
        string += "T_Entry: {}\n".format(self.t_entry)
        string += "Done: {}\n".format(self.done)
        string += "T_Done: {}\n".format(self.t_done)
        return string