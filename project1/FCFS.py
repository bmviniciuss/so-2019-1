class FCFS:
    #  Implements an FCFS scheduler (First-Come, First-Served)
    def __init__(self, processes):
        self.processes = processes.copy()
        self.done = []
        self.ready_queue = []
        self.cpu_active = False
        self.on = True
        self.timer = 0

    def get_processes(self):
        processes_copy = self.processes.copy()
        filtered = list(filter(lambda p: self.timer >= p.t_arrival, processes_copy))
        self.processes = [p for p in self.processes if p not in filtered]

        return filtered

    def increment_waiting_time(self):
        for p in self.ready_queue:
            if not p.active:
                p.t_wait += 1

    def print_process(self, ps, message):
        print(message)
        for p in ps:
            print(p)

    def run(self):
        self.timer = 0
        self.on = True    
        self.cpu_active = False

        # self.print_process(self.processes, "Original: ")
        while self.on:
            # Get proccess by time
            ps = self.get_processes()

            # Append process in ready queue
            self.ready_queue += ps

            # scheduling
            if len(self.ready_queue) > 0:
                if self.cpu_active == False: # if cpu does not has a process
                    if self.timer >= self.ready_queue[0].t_arrival: # process already arrive
                        self.cpu_active = True # make cpu active
                        p = self.ready_queue.pop(0) # pop process first process from ready_queue
                        p.start_process(self.timer) # Starts process

                        # do some cpu work
                        while p.is_done():
                            self.timer += 1 # incremet the timer
                            p.run() # run single interation of process
                            self.increment_waiting_time() # icrement waiting process in ready_queue

                        p.finish_process(self.timer) # finish process
                        self.cpu_active = False # cpu is not working at the time
                        self.done.append(p) # append finished process to the done list

                else: # cpu has a process
                    # self.timer += 1 # increment timer until has a process
                    self.increment_waiting_time() # increment waiting time
            else:
                break

        
        self.print_process(self.done, "Done: ")
        
