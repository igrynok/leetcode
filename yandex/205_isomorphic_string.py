class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        char_dict = {}
        t_set = set()

        for index, elem in enumerate(s):
            if elem in char_dict:
                iso = char_dict[elem]
                if iso != t[index]:
                    return False
            else:
                if t[index] in t_set:
                    return False
                char_dict[elem] = t[index]
                t_set.add(t[index])

        return True
