from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        unique_emails = set()
        for email in emails:
            at_id = email.index('@')
            email = email[:at_id].replace('.', '') + email[at_id:]
            if '+' in email:
                plus_id = email.index('+')
                at_id = email.index('@')
                email = email[:plus_id] + email[at_id:]
            unique_emails.add(email)

        return len(unique_emails)