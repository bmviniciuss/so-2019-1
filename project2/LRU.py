import copy


class LRU:
    def __init__(self, memory_blocks, references):
        self.memory_blocks = copy.deepcopy(memory_blocks)
        self.references = copy.deepcopy(references)
        self.pages = [None for i in range(self.memory_blocks)]

    def run(self):
        memory_errors = 0
        cache_hit = 0

        access_index = 0
        pages_index = 0
        for access in self.references:
            if access in self.pages:
                cache_hit += 1
                # botar inicio da pilha
                index = self.pages.index(access)
                self.pages.pop(index)
                self.pages.insert(0, access)
            else:
                memory_errors += 1
                self.pages.pop()
                self.pages.insert(0, access)

            access_index += 1

        return memory_errors
