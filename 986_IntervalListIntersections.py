class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        res = []
        while firstList and secondList:
            if firstList[0][1] < secondList[0][0]:
                firstList.pop(0)
            elif secondList[0][1] < firstList[0][0]:
                secondList.pop(0)
            elif firstList[0][0] <= secondList[0][0]:
                if firstList[0][1] <= secondList[0][1]:
                    res.append([secondList[0][0], firstList[0][1]])
                    firstList.pop(0)
                else:
                    res.append(secondList[0])
                    secondList.pop(0)
            elif firstList[0][0] > secondList[0][0]:
                if firstList[0][1] >= secondList[0][1]:
                    res.append([firstList[0][0], secondList[0][1]])
                    secondList.pop(0)
                else:
                    res.append(firstList[0])
                    firstList.pop(0)
        return res
