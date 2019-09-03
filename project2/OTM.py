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
        pages_index = 0
        atingidas = []

        aux = list(dict.fromkeys(self.references))

        for access in references_copy:

            if access in self.pages:
                cache_hit += 1
            else:
                memory_errors += 1

                if None in self.pages:
                    for i in range(len(self.pages)):
                        if self.pages[i] == None:
                            self.pages[i] = access
                            break
                else:
                    atingidas = []
                    verificou_todas = 0

                    for e in self.references[access_index + 1:]:
                        if verificou_todas < len(aux):
                            if e not in atingidas:
                                atingidas.append(e)
                        else:
                            break

                    # adiciona elementos que n foram lidos (baixa preferencia)
                    atingidas += list(set(aux) - set(atingidas))

                    elemento = None

                    for e in atingidas[::-1]:
                        if e in self.pages:
                            elemento = e
                            break

                    if elemento == None:
                        self.pages[0] = access
                    else:

                        for i in range(len(self.pages)):
                            if self.pages[i] == elemento:
                                self.pages[i] = access
                                break

            access_index += 1

        return memory_errors
