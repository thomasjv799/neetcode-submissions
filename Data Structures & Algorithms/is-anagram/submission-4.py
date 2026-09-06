class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
            
        def char_counts(s):
            char={}
            for i in sorted(s):
                if i in char:
                    char[i]+=1
                else:
                    char[i]=1
            return char

            
        s_char=char_counts(s)
        t_char=char_counts(t)

        for i in s_char:
            if i not in t_char or s_char[i] != t_char[i]:
                return False
                break
        else:
            return True
        