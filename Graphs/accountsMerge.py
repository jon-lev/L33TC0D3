#Union Find
class UF:
    def __init__(self, n):
        self.count = n
        self.id = [i for i in range(n)]
    
    def find(self, p):
        return self.id[p]
    
    #O(V)
    def union(self, child, parent):
        cID = self.find(child)
        pID = self.find(parent)
        
        if pID == cID: return
        
        for i in range(len(self.id)):
            if self.id[i] == cID:
                self.id[i] = pID
            

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        
        #match correct owner to all emails
        ownership = {}
        
        #for all list of emails in accounts
        for i, (_, *emails) in enumerate(accounts):
            #for every email in the list of emails
            for email in emails:
                #if its already marked to an ID, add to UF graph
                if email in ownership:
                    uf.union(i, ownership[email])
                #otherwise mark the ID 
                ownership[email] = i
        
        #combine all to one owner ID for answer
        ret = collections.defaultdict(list)
        for email, owner in ownership.items():
            ret[uf.find(owner)].append(email)
        
        #create string with the owner's name and the correct list of emails
        return [[accounts[i][0]] + sorted(emails) for i, emails in ret.items()]