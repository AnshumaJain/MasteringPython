
from fractions import Fraction
def slopeAndIntercept(points):
    #points = [[3,4], [5,6]]
    [point1, point2] = points
    if (point1[0] - point2[0]) == 0:
        m = "inf"
        b = point1[0]
        key = str(m) + "," + str(b)

    else:
        m = Fraction((point1[1] - point2[1]), (point1[0] - point2[0]))
        b = point1[1] - (m * point1[0])

        key = str(m) + "," + str(b)
    return key

class Solution:

    def __init__(self):
        self.dict = {}

    def maxPoints(self, points):

        if len(points) == 0:
            return 0
        elif len(points) == 1:
            return 1
        count = 0
        for i in range(0, len(points)):
            for j in range(i + 1, len(points)):
                list = [points[i], points[j]]
                #print(list)
                key = slopeAndIntercept(list)
                #print(key)
                if key in self.dict.keys(): #achhe se samajhna
                    self.dict[key].append(list)
                else:
                    self.dict[key] = []
                    self.dict[key].append(list)

        #print(self.dict)

        for keys, values in self.dict.items():
            print(keys)
            print(values)
            print("")

        valueLen = 0
        for i in self.dict.keys():
            if len(self.dict[i]) >= valueLen:
                valueLen = len(self.dict[i])
                Maxkey = i
        #print(Maxkey, "length = " + str(valueLen))

        listOfPoints = []
        ListOfCoordinates = self.dict[Maxkey]

        print(ListOfCoordinates)
        for i in ListOfCoordinates:

            if i[0] in listOfPoints:
                pass
            else:
                listOfPoints.append(i[0])

            if i[1] in listOfPoints:
                pass
            else:
                listOfPoints.append(i[1])

        print(listOfPoints)

        for i in listOfPoints:
            for j in points:
                if i == j:
                    count+=1

        maxpoints = count

        return maxpoints

p = Solution()
#pp = pprint.PrettyPrinter(indent=4)

output = p.maxPoints([[-240,-657],[-27,-188],[-616,-247],[-264,-311],[-352,-393],[-270,-748],[3,4],[-308,-87],[150,526],[0,-13],[-7,-40],[-3,-10],[-531,-892],[-88,-147],[4,-3],[-873,-555],[-582,-360],[-539,-207],[-118,-206],[970,680],[-231,-47],[352,263],[510,143],[295,480],[-590,-990],[-236,-402],[308,233],[-60,-111],[462,313],[-270,-748],[-352,-393],[-35,-148],[-7,-40],[440,345],[388,290],[270,890],[10,-7],[60,253],[-531,-892],[388,290],[-388,-230],[340,85],[0,-13],[770,473],[0,73],[873,615],[-42,-175],[-6,-8],[49,176],[308,222],[170,27],[-485,-295],[170,27],[510,143],[-18,-156],[-63,-316],[-28,-121],[396,304],[472,774],[-14,-67],[-5,7],[-485,-295],[118,186],[-154,-7],[-7,-40],[-97,-35],[4,-9],[-18,-156],[0,-31],[-9,-124],[-300,-839],[-308,-352],[-425,-176],[-194,-100],[873,615],[413,676],[-90,-202],[220,140],[77,113],[-236,-402],[-9,-124],[63,230],[-255,-118],[472,774],[-56,-229],[90,228],[3,-8],[81,196],[970,680],[485,355],[-354,-598],[-385,-127],[-2,7],[531,872],[-680,-263],[-21,-94],[-118,-206],[616,393],[291,225],[-240,-657],[-5,-4],[1,-2],[485,355],[231,193],[-88,-147],[-291,-165],[-176,-229],[154,153],[-970,-620],[-77,33],[-60,-111],[30,162],[-18,-156],[425,114],[-177,-304],[-21,-94],[-10,9],[-352,-393],[154,153],[-220,-270],[44,-24],[-291,-165],[0,-31],[240,799],[-5,-9],[-70,-283],[-176,-229],[3,8],[-679,-425],[-385,-127],[396,304],[-308,-352],[-595,-234],[42,149],[-220,-270],[385,273],[-308,-87],[-54,-284],[680,201],[-154,-7],[-440,-475],[-531,-892],[-42,-175],[770,473],[118,186],[-385,-127],[154,153],[56,203],[-616,-247]])

print(output)
