class Process:
    def __init__(self, pid, t_arrival, cpu_peak):
        self.pid = pid
        self.t_arrival = t_arrival
        self.cpu_peak = cpu_peak

    def __repr__(self):
        return "[{}, {}, {}]".format(self.pid, self.t_arrival, self.cpu_peak)

    def __str__(self):
        return "# Process {} - Arrival: {}, CPU Peak: {}".format(self.pid, self.t_arrival, self.cpu_peak)