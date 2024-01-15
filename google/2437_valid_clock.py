class Solution:
    def countTime(self, time: str) -> int:

        hours, minutes = time.split(':')
        answer = 1

        if hours[0] == '?' and hours[1] == '?':
            answer = 24
        elif hours[0] == '?':
            hour2 = int(hours[1])
            answer = 3 if hour2 < 4 else 2
        elif hours[1] == '?':
            hours1 = int(hours[0])
            answer = 10 if hours1 < 2 else 4

        if minutes[0] == '?':
            answer = answer * 6
        if minutes[1] == '?':
            answer = answer * 10

        return answer
