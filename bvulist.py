class bvulist(list):

    def prepend(self, val):
        self.insert(0, val)

    def pop_back(self):

        self.pop()

    def pop_front(self):

        return self.pop(0)
