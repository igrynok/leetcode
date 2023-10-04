# [""]
# [[""]]

# ["a"]
# [["a"]]

# ["eat","tea","tan","ate","nat","bat"]
# [["bat"],["nat","tan"],["ate","eat","tea"]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_strs = [ "".join(sorted(s)) for s in strs]
        str_dict = {}
        answer = []

        for i, s in enumerate(sorted_strs):

            if s in str_dict:
                index = str_dict[s]
                answer[index].append(strs[i])
            else:
                group_index = len(answer)
                str_dict[s] = group_index
                answer.append([strs[i]])

        return answer


