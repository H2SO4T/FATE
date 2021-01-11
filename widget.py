class Widget:
    def __init__(self, father, transition):
        self.active = transition['active']
        self._father = father
        self.type = transition['type']
        self.guard = transition['guard']
        self.set = transition['set']
        if self.type == 'editText':
            self.strings = []
            f = open('strings.txt', 'r+')
            for line in f.readlines():
                self.strings.append(line[:-1])
        self.destination = transition['destination']
