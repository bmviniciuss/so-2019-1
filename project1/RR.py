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

    def run(self):
        """Runs the FCFS algorithm"""
        self.timer = 0
        self.on = True
        self.cpu_active = False

        # self.print_process(self.processes, "Original: ")
        while self.on:
            self.update_ready_queue()  # Update Ready Queue

            # scheduling
            if len(self.ready_queue) > 0:
                if self.cpu_active == False:  # if cpu does not has a process
                    # process already arrived
                    if self.timer >= self.ready_queue[0].t_arrival:
                        self.cpu_active = True  # makes cpu active flag true
                        # pop first process of readty queue
                        p = self.ready_queue.pop(0)

                        # check if process already went to the cpu
                        if p.remaining() == p.cpu_peak:
                            # process never went to the cpu
                            p.init_process(self.timer)
                        else:
                            # process already went to the cpu
                            p.start_process()

                        # do cpu work
                        c = 0  # quantum counter
                        while c < self.quantum and not p.is_done():
                            self.update_ready_queue()
                            p.run()
                            self.tick()
                            self.increment_waiting_time()
                            c += 1

                        p.stop_process()  # stop process
                        self.cpu_active = False  # makes cpu inactive

                        if p.is_done():  # check if process is done
                            p.end_process(self.timer)  # end process
                            self.done.append(p)  # put process in the done list
                        else:
                            self.update_ready_queue()
                            # put process back, at the end, in the ready queue
                            self.ready_queue.append(p)
                else:  # cpu has a process
                    self.update_ready_queue()  # update ready queue
            else:
                break

        # self.print_process(self.done, "Done: ")
        result = self.compute_stats()
        return result

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
