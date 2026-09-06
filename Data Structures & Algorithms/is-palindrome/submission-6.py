class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_nospace = re.sub(r'[^a-zA-Z0-9\s]', '', s)
        s_nospace = s_nospace.replace(" ", "").lower()
        s_nospace=" ".join(s_nospace)
        if len(s_nospace)==1 or len(s_nospace)==0:
            return True
        if len(s_nospace)%2 == 0:
            one_mid=False
            first_mid = int(len(s_nospace)/2) -1
            second_mid = first_mid +1
        else:
            one_mid=True
            mid = round(len(s_nospace)/2)

        back=-1
        for i in range(len(s_nospace)):
            if one_mid:
                if i == mid:
                    return True
                    break
                
                if s_nospace[i]==s_nospace[back]:
                    back-=1
                    continue
                else:
                    return False
                    break
            else:
                if i== first_mid:
                    if s_nospace[first_mid]!=s_nospace[second_mid]:
                        return False
                        break
                    else:
                        return True
                        break
                else:
                    s_nospace[i]==s_nospace[back]
                    back-=1
                    continue
            
        