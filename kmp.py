# def compute_LPS(pat,lps,m):
    
#     len = 0
#     i = 1
#     lps[0] = 0

#     while i < m:
#         if pat[len] == pat[i] :
#             lps[i] = len + 1
#             len +=1
#             i+=1

#         else:
#             if len !=0:
#                 len = lps[len -1]

#             else :
#                 lps[i] = 0
#                 i +=1

# def kmp_algo(pat,txt):
#     n = len(txt)
#     m = len(pat)
#     lps = [0] * m

#     i=0
#     j=0

#     compute_LPS(pat,lps,m)

#     print(lps)

#     while i < n -m + 1:

#         if pat[j] == txt[i]:
#             i+=1
#             j+=1
       
#         else :
#             if j != 0 :
#                 j = lps[j-1]
#             else:
#                 i+=1

#         if j == m:
#             print("pattern found at index ",i-j)
#             j = lps[j-1]


        


# txt = "ABABDABACDABABCABAB"
# pat = "ABAB"
# kmp_algo(pat,txt)

def compute_LPS(pat, lps, m):
    len = 0
    i = 1
    lps[0] = 0  # First entry is always 0

    while i < m:
        if pat[len] == pat[i]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1


def kmp_algo(pat, txt):
    n = len(txt)
    m = len(pat)
    lps = [0] * m

    # Precompute the LPS array
    compute_LPS(pat, lps, m)

    i = 0  # index for txt
    j = 0  # index for pat

    while i < n:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == m:
            print("Pattern found at index", i - j)
            j = lps[j - 1]  # Continue searching for next match

        # Mismatch after j matches
        elif i < n and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


txt = "ABABDABACDABABCABAB"
pat = "ABAB"
kmp_algo(pat, txt)
