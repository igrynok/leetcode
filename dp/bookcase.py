class Solution(object):

    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """

        def min_height(i, current_width, current_height, memo):

            if (i, current_width, current_height) in memo:
                return memo[(i, current_width, current_height)]

            if i == (len(books)):
                return current_height

            min_h = 10 ** 9

            if books[i][0] + current_width <= shelfWidth:
                the_same_shelf = min_height(i + 1, books[i][0] + current_width, max(books[i][1], current_height), memo)
                a_new_shelf = min_height(i + 1, books[i][0], books[i][1], memo) + current_height
                min_h = min(the_same_shelf, a_new_shelf)
            else:
                min_h = min_height(i + 1, books[i][0], books[i][1], memo) + current_height

            memo[(i, current_width, current_height)] = min_h
            return min_h

        memo = {}
        return min_height(1, books[0][0], books[0][1], memo)
