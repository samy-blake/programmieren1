class Length:
    def __init__(self, foot, inch):
        self._inch = foot * 12 + inch
    
    def __str__(self):
        [foot, inch] = self._calcFootAndInch(self._inch)
        return str(foot) + ' feet and ' + \
        str(inch) + ' inch'
    
    def __add__(self, otherLength):
        addInch = self.getInch() + otherLength.getInch()
        [foot, inch] = self._calcFootAndInch(addInch)
        return Length(foot, inch)

    def _calcFootAndInch(self, newInch):
        foot = newInch // 12
        inch = newInch % 12
        return [foot, inch]

    def getInch(self):
        return self._inch

    def setInch(self, inch):
        self._inch = inch



if __name__ == '__main__':
    len1 = Length(1, 9)
    len2 = Length(3, 5)
    len3 = len1 + len2
    print(len3)