class Measures:
    __sample = 0

    @staticmethod
    def findMode(selection):
        mode = {}
        for i in selection:
            if i not in mode:
                mode[i] = 1
            else:
                mode[i] += 1
        frequency = max(mode.values())
        mode = {key : value for key, value in mode.items() if value == frequency}
        return mode

    @staticmethod
    def findMedian(selection):
        return Measures.findQuantiles(1, selection)

    @staticmethod
    def findQuoters(selection):
        return Measures.findQuantiles(2, selection)

    @staticmethod
    def findQuantiles(n, selection):
        __sample = sorted(selection)
        l = len(cusList)
        if (l % 2 == 0):
            median = (cusList[n // 2 - 1] + cusList[n // 2]) / 2
        else:
            median = cusList[n // 2]
        return median

def findAverage(selection):
    average = sum(selection) / len(selection)
    return average

def findRange(selection):
    range = max(selection) - min(selection)
    print(range)
    return range

class Variance:
    __variance = 0
    __sd = 0

    def __init__(self, selection):
        average = findAverage(selection)
        devSquareAmount = 0
        for i in selection:
            devSquareAmount += (i - average) ** 2
        self.__variance = devSquareAmount / (len(selection) - 1)
        self.__sd = self.__variance ** 0.5

    def getVariance(self):
        return self.__variance

    def getSD(self):
        return self.__sd