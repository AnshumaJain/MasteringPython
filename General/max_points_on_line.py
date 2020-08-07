"""
LeetCode Problem #149: Max Points on a Line

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:
Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o
+------------->
0  1  2  3  4

Example 2:
Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
"""
from fractions import Fraction


def slope_and_intercept(points):
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

    def max_points(self, points):

        if len(points) == 0:
            return 0
        elif len(points) == 1:
            return 1
        count = 0
        for i in range(0, len(points)):
            for j in range(i + 1, len(points)):
                list = [points[i], points[j]]
                key = slope_and_intercept(list)
                if key in self.dict.keys():  # achhe se samajhna
                    self.dict[key].append(list)
                else:
                    self.dict[key] = []
                    self.dict[key].append(list)

        # for keys, values in self.dict.items():
        #     print(keys)
        #     print(values)
        #     print("")

        valueLen = 0
        for i in self.dict.keys():
            if len(self.dict[i]) >= valueLen:
                valueLen = len(self.dict[i])
                maxkey = i

        list_of_points = []
        list_of_coordinates = self.dict[maxkey]

        # print(list_of_coordinates)
        for i in list_of_coordinates:

            if i[0] in list_of_points:
                pass
            else:
                list_of_points.append(i[0])

            if i[1] in list_of_points:
                pass
            else:
                list_of_points.append(i[1])

        # print(list_of_points)

        for i in list_of_points:
            for j in points:
                if i == j:
                    count += 1

        maxpoints = count

        return maxpoints


if __name__ == "__main__":

        sol = Solution()
        print(sol.max_points([[1, 1],[2, 2],[3, 3]]))
        print(sol.max_points([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
