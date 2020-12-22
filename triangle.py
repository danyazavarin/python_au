from math import sqrt
import sys

class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)


class Triangle:
    def __init__(self, side1, side2, side3):
        def length(x, y, x0, y0):
            return sqrt((x - x0) * (x - x0) + (y - y0)*(y - y0))
        self.side1 = length(side1.x, side1.y, side2.x, side2.y)
        self.side2 = length(side2.x, side2.y, side3.x, side3.y)
        self.side3 = length(side1.x, side1.y, side3.x, side3.y)


    def S(self):
        if self.chech_triangle() == True:
            p = self.poluperimetr()
            return sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))
        return -1

    def poluperimetr(self):
        return (self.side1 + self.side2 +self.side3) / 2


    def chech_triangle(self):
        return (self.side1 < self.side2 + self.side3) and (self.side2 < self.side1 + self.side3) and (self.side3 < self.side1 + self.side3)


class Solution:
    def __init__(self,filename, outputname):
        self.filename = str(filename)
        self.outputname = str(outputname)

    def get_list(self):
        with open(self.filename) as i:
            self.result = list(map(lambda x: x.strip('\n').split(), i.readlines()))
        return self.result


    def find(self):
        def check(result):
            if len(result) != 6:
                return False
            for i in range(len(result)):
                if (result[i].isdigit()) == False:
                    return False
            return True
        arr = []
        file = open((self.outputname), 'w')
        count = len(self.get_list())
        result = self.get_list()
        for i in range(count):
            if check(result[i]):
                area = Triangle(Point(self.result[i][0], self.result[i][1]),
                                Point(self.result[i][2], self.result[i][3]),
                                Point(self.result[i][4], self.result[i][5]))
                area1 = area.S()
                arr.append(area1)
            else:
                arr.append(-1)
        if max(arr) != -1:
            b = result[arr.index(max(arr))]
            for i in range(len(b)):
                file.write(str(b[i]) + ' ')
            file.close()


def main(inputname, outputname):
    arr = Solution(inputname, outputname)
    arr.find()


if __name__ == "__main__":
    params = sys.argv
    main(params[0], params[1])