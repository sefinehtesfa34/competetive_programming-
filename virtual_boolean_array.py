class BooleanArray:
    def __init__(self):
        self.boolean = {}
        self.recent = False
    def setTrue(self, i):
        self.boolean[i] = True
    def setFalse(self, i):
        self.boolean[i] = False
    def setAllTrue(self):
        self.recent = True
        self.boolean = {}
    def setAllFalse(self):
        self.recent = False
        self.boolean = {}
    def getValue(self, i):
        return self.boolean.get(i, self.recent)
