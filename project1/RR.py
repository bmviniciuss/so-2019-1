class RR:
    """Implements a RR scheduler """

    def __init__(self, processes):
        self.processes = processes.copy()
        self.done = []
        self.ready_queue = []
        self.cpu_active = False
        self.on = True
        self.timer = 0
        self.quantum = 2

    def get_processes(self):
        """Get a list of processes by the time of the timer"""
        processes_copy = self.processes.copy()
        filtered = list(filter(lambda p: self.timer >=
                               p.t_arrival, processes_copy))
        self.processes = [p for p in self.processes if p not in filtered]
        return filtered

    def increment_waiting_time(self):
        """Increments the waiting time of all processes in the Ready Queue"""
        for p in self.ready_queue:
            p.wait()

    def print_process(self, ps, message):
        """Function that print a list of processes"""
        print(message)
        for p in ps:
            print(p)

    def tick(self):
        """Ticks the timer by 1 unit of time"""
        self.timer += 1

    def update_ready_queue(self):
        """Updates the ready queue with the latest processes"""
        # Get proccess by time
        ps = self.get_processes()
        # Append processes in ready queue
        self.ready_queue += ps

    def print_ready(self):
        string = "Time: {} = [".format(self.timer)

        for p in self.ready_queue:
            string += str(p.pid) + " "
        string += "]"

        print(string)

    def run(self):
        """Runs the FCFS algorithm"""
        self.timer = 0
        self.on = True
        self.cpu_active = False

        # self.print_process(self.processes, "Original: ")
        while self.on:
            self.update_ready_queue()  # Update Ready Queue
            # self.print_ready()
            #  self.print_process(

            # self.ready_queue, "TIME: {} FILA: ".format(self.timer))

            # scheduling
            if len(self.ready_queue) > 0:
                if self.cpu_active == False:  # if cpu does not has a process
                    # process already arrived
                    if self.timer >= self.ready_queue[0].t_arrival:
                        self.cpu_active = True
                        p = self.ready_queue.pop(0)
                        if p.remaining() == p.cpu_peak:

                            # print("NUNCA P{}".format(p.pid))
                            p.init_process(self.timer)
                        else:
                            # print("JA P{}".format(p.pid))
                            p.start_process()

                        c = 0
                        while c < self.quantum and not p.is_done():
                            self.update_ready_queue()
                            p.run()
                            self.tick()
                            self.increment_waiting_time()
                            c += 1

                        p.stop_process()
                        self.cpu_active = False

                        if p.is_done():
                            p.end_process(self.timer)
                            self.done.append(p)
                        else:
                            # self.tick()

                            self.update_ready_queue()
                            self.ready_queue.append(p)
                else:  # cpu has a process
                    self.update_ready_queue()  # update ready queue
            else:
                break

        # self.print_process(self.done, "Done: ")
        result = self.compute_stats()
        # print(self.timer)
        return result
        # return [1, 1, 1]

    def compute_stats(self):
        """Compute the scheduler's peformance stats"""
        n = len(self.done)

        # t_return, t_response, t_waiting
        sums = [0, 0, 0]

        for p in self.done:
            # print(p.t_return)
            sums[0] += p.t_return
            sums[1] += p.t_response
            sums[2] += p.t_waiting

        avgs = list(map(lambda x: x / n, sums))
        return avgs
