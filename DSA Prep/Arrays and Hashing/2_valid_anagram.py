# https://neetcode.io/problems/is-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count_dict,t_count_dict = {},{}
        for i in range(len(s)):
            s_count_dict[s[i]] = s_count_dict.get(s[i], 0) +1
            t_count_dict[t[i]] = t_count_dict.get(t[i], 0) +1
            
        for char in s_count_dict.keys():
            if t_count_dict.get(char,None) == s_count_dict[char]:
                continue
            else:
                return False

        return True       
          
if __name__ == "__main__":
    s = "jar"
    t = "jam"
    print(Solution().isAnagram(s,t))