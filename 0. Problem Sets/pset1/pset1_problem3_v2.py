from icecream import ic

def longestalpha(s: str) -> str:

    longest = ""
    substr = ""

    for i in range(len(s)):

        substr += s[i]
        
        if i == len(s)-1 or s[i] > s[i+1]:
            if len(substr) > len(longest):
                longest = substr
            substr = ""
        
        ic(substr, i)
        
    return longest


ic(longestalpha("ttifipjrif'")) # "fip"
ic(longestalpha("azcbobobegghakl")) # "beggh"