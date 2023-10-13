# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):

        flat_list = []

        def flatten_list(nested_list):
            for elem in nested_list:
                if elem.isInteger():
                    flat_list.append(elem.getInteger())
                else:
                    flatten_list(elem.getList())

        flatten_list(nestedList)
        self.flat_list = flat_list
        self.position = 0

    def next(self) -> int:
        elem = self.flat_list[self.position]
        self.position += 1
        return elem

    def hasNext(self) -> bool:
        return self.position < len(self.flat_list)



# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())