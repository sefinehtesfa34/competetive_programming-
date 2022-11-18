class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {email:email for account in accounts for email in account[1:]}
        names = {email:account[0] for account in accounts for email in account[1:]}
        group = defaultdict(list)
        answer = []
        
        def find(email):
            if email == parent[email]:
                return email
            parent[email] = find(parent[email])
            return parent[email]
        
        def union(email1, email2):
            email_for1 = find(email1)
            email_for2 = find(email2)
            if email_for1 != email_for2:
                parent[email_for1] = email_for2
                
        for account in accounts:
            first_email = account[1]
            for email in account[2:]:
                union(email, first_email)
                
        for email in parent:
            email_par = find(email)
            group[email_par].append(email)
            
        for email in group:
            name = names[email]
            answer.append([name] + sorted(group[email]))
        return answer
        
            
        