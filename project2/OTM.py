import copy


class OTM:
    def __init__(self, memory_blocks, references):
        self.memory_blocks = copy.deepcopy(memory_blocks)
        self.references = copy.deepcopy(references)
        self.pages = [None for i in range(self.memory_blocks)]

    def run(self):
        references_copy = copy.deepcopy(self.references)
        memory_errors = 0
        cache_hit = 0

        access_index = 0
        atingidas = []

        # all possible pages in references (no repetition)
        aux = list(dict.fromkeys(self.references))

        for access in references_copy:

            if access in self.pages:
                # access in pages
                cache_hit += 1
            else:
                # acces not in pages
                memory_errors += 1

                # there is empty space in pages
                if None in self.pages:
                    for i in range(len(self.pages)):
                        if self.pages[i] == None:
                            self.pages[i] = access
                            break
                else:
                    # there is no empty space in pages
                    checked = []

                    for e in self.references[access_index + 1:]:
                        if len(checked) < len(aux):
                            if e not in checked:
                                checked.append(e)
                        else:
                            break

                    # add elements that was not read on the "future accesses" but maybe is on pages
                    # append to the checked list the intersection of aux and checked
                    checked += list(set(aux) - set(checked))

                    element = None

                    for e in checked[::-1]:
                        if e in self.pages:
                            element = e
                            break

                    if element == None:
                        self.pages[0] = access
                    else:

                        for i in range(len(self.pages)):
                            if self.pages[i] == element:
                                self.pages[i] = access
                                break

            access_index += 1

        return memory_errors
