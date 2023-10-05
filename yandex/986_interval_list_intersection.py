[[1, 3], [5, 9]]
# []

# [[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        answer = []

        if len(firstList) == 0 or len(secondList) == 0:
            return answer

        int1_i, int2_i = 0, 0

        while int1_i < len(firstList) and int2_i < len(secondList):

            int1, int2 = firstList[int1_i], secondList[int2_i]

            if int1[0] > int2[1]:
                int2_i += 1

            if int2[0] > int1[1]:
                int1_i += 1

            if not (int1[0] > int2[1] or int2[0] > int1[1]):
                answer.append([max(int1[0], int2[0]), min(int1[1], int2[1])])
                if int1[1] == int2[1]:
                    int1_i += 1
                    int2_i += 1
                elif int1[1] < int2[1]:
                    int1_i += 1
                else:
                    int2_i += 1

        return answer