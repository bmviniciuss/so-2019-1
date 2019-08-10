class Process:
    """Class that represents a process in a system"""

    def __init__(self, pid, t_arrival, cpu_peak):
        self.pid = pid
        self.t_arrival = t_arrival
        self.cpu_peak = cpu_peak
        self.active = False
        self.t_active = 0
        self.t_waiting = 0
        self.t_entry = 0
        self.done = False
        self.t_done = 0
        self.t_return = 0
        self.t_response = 0

    def init_process(self, time):
        """Starts a process."""
        self.active = True  # makes process's active flag true
        self.t_entry = time  # save the time that the process starts working

    def start_process(self):
        self.active = True

    def stop_process(self):
        self.active = False

    def end_process(self, time):
        """Ends a process"""
        self.active = False  # process has been finished
        self.done = True  # makes process done flag true
        self.t_done = time  # save the time of doness
        self.t_return = (self.t_done - self.t_arrival)
        self.t_response = (self.t_entry - self.t_arrival)

    def run(self):
        """Run the process for a single iteration."""
        self.t_active += 1  # increment process's active timer

    def is_done(self):
        """Check if a process is done."""
        return not (self.t_active < self.cpu_peak)

    def remaining(self):
        return self.cpu_peak - self.t_active

    def wait(self):
        """Increments the waiting time of a process, if not active"""
        if not self.active:
            self.t_waiting += 1

    def __str__(self):
        string = "## Process {}\n".format(self.pid)
        string += "Arrival: {}\n".format(self.t_arrival)
        string += "CPU Peak: {}\n".format(self.cpu_peak)
        string += "Active: {}\n".format(self.active)
        string += "Done: {}\n".format(self.done)
        string += "T_Entry: {}\n".format(self.t_entry)
        string += "T_Active: {}\n".format(self.t_active)
        if self.done:
            string += "T_Done: {}\n".format(self.t_done)
            string += "T_Return: {}\n".format(self.t_done - self.t_arrival)
            string += "T_Response: {}\n".format(self.t_entry - self.t_arrival)
            string += "T_Waiting: {}\n".format(self.t_waiting)
        return string
