class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        no_dash = s.replace('-', '').upper()
        rem = len(no_dash) % k

        answer = ''
        if rem:
            answer = no_dash[:rem]

        for group in range(rem, len(no_dash), k):
            if answer:
                answer += '-'
            answer += no_dash[group:group + k]

        return answer