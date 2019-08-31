import copy


class FIFO:
    def __init__(self, memory_blocks, references):
        self.memory_blocks = copy.deepcopy(memory_blocks)
        self.references = copy.deepcopy(references)
        self.pages = [None for i in range(self.memory_blocks)]

    def run(self):
        memory_errors = 0

        access_index = 0
        pages_index = 0
        for access in self.references:
            if access not in self.pages:
                memory_errors += 1
                self.pages[pages_index] = access
                pages_index += 1
                if pages_index >= len(self.pages):
                    pages_index = 0

            access_index += 1

        return memory_errors
