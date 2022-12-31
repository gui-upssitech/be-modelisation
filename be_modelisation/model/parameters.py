class Parameters:

    def __init__(self, l: list[float], h: list[float]) -> None:    
        self.__h = h
        self.__l = l

    def get_lengths(self) -> list[float]:
        return self.__l

    def l(self, i: int) -> float:
        return self.__l[i-1]
    
    def get_heights(self) -> list[float]:
        return self.__h

    def h(self, i: int) -> float:
        return self.__h[i-1]