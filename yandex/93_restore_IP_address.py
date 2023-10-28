class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        answer = []

        def dfs(path):

            if not path and len(s) > 12:
                return

            if path and len(s[path[-1]:]) > 3*(4 - len(path)):
                return

            if len(path) == 3:

                if len(s[path[-1]:]) > 1 and s[path[-1]] == '0':
                    return
                if int(s[path[-1]:]) > 255:
                    return

                address = s[:path[0]] + '.'+ s[path[0]:path[1]] + '.' + s[path[1]:path[2]] + '.' + s[path[2]:]
                answer.append(address)
                return

            for i in range(1, 4):

                mask = ''
                if not path:
                    mask = s[:i]
                else:
                    if path[-1] + i < len(s):
                        mask = s[path[-1]:path[-1] + i]

                if mask == '':
                    break

                if i==1 and int(mask) == 0:
                    if path:
                        path.append(path[-1] + 1)
                    else:
                        path.append(1)
                    dfs(path)
                    path.pop()
                    break

                if int(mask) > 255:
                    break

                if not path:
                    path.append(i)
                else:
                    path.append(path[-1] + i)

                dfs(path)
                path.pop()

        dfs([])
        return answer
