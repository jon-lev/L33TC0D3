class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':'abc',
               '3':'def',
               '4':'ghi',
               '5':'jkl',
               '6':'mno',
               '7':'pqrs',
               '8':'tuv',
               '9':'wxyz'}
        
        #empty digit given, return empty array
        if len(digits) == 0:
            return []
        
        #start with ''
        allCombos = ['']
        
        #loop through all digits in string
        for digit in digits:
            #empty list for every iteration of digits
            currCombo = []
            #find all possible letters for specific digit
            for letter in dic[digit]:
                for combo in allCombos:
                    currCombo.append(combo + letter)
                    
            allCombos = currCombo
        # aC: ['']
        # cC: ['a', 'b', 'c']
        # ---->
        # aC: ['a', 'b', 'c']
        # cC: []
        # cC: ['ad', 'bd', 'cd', "ae", "be", "ce", "af", "bf", "cf"]
        # aC == cC
        return allCombos
                    
                