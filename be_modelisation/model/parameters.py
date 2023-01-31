class Parameters:

    def __init__(self, l, h):    
        self.__h = h
        self.__l = l

    def get_lengths(self):
        return self.__l

    def l(self, i):
        return self.__l[i-1]
    
    def get_heights(self):
        return self.__h

    def h(self, i):
        return self.__h[i-1]