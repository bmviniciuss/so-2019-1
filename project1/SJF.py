class SJF:
    """Implements an SJF scheduler (Shortest Job First) """

    def __init__(self, processes):
        self.processes = processes.copy()
        self.done = []
        self.ready_queue = []
        self.cpu_active = False
        self.on = False
        self.timer = 0

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

        def sortP(p):
            """Sort functions that returns the cpu peak of a process"""
            return p.cpu_peak

        self.ready_queue.sort(key=sortP)

    def run(self):
        """Runs the FCFS algorithm"""
        self.timer = 0
        self.on = True
        self.cpu_active = False

        # self.print_process(self.processes, "SJF Original: ")
        while self.on:
            self.update_ready_queue()  # Update Ready Queue

            # scheduling
            if len(self.ready_queue) > 0:
                if self.cpu_active == False:  # if cpu does not has a process
                    # process already arrive
                    if self.timer >= self.ready_queue[0].t_arrival:
                        self.cpu_active = True  # make cpu active
                        # pop process first process from ready_queue
                        p = self.ready_queue.pop(0)
                        p.start_process(self.timer)  # Starts process

                        # do some cpu work
                        while p.is_done():
                            self.update_ready_queue()  # update ready queue
                            p.run()  # run single interation of process
                            self.tick()  # incremet the timer
                            self.increment_waiting_time()  # icrement waiting process in ready_queue

                        p.finish_process(self.timer)  # finish process
                        self.cpu_active = False  # cpu is not working at the time
                        # append finished process to the done list
                        self.done.append(p)

                else:  # cpu has a process
                    self.tick()  # increment timer until has a process
                    self.update_ready_queue()  # update ready queue
                    self.increment_waiting_time()  # increment waiting time
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
            sums[0] += p.t_return
            sums[1] += p.t_response
            sums[2] += p.t_waiting

        avgs = list(map(lambda x: x / n, sums))
        return avgs
