def naive ( txt , pat ) :
    len_pat = len(pat)
    len_txt = len(txt)

    for i in range(len_txt - len_pat + 1) :
        j = 0
        while j<len_pat  and txt[i + j] == pat[j] :
            j+=1

        if j == len_pat :
            print("Pattern found at index " + str(i))


txt = "AABAACAADAABAAABAA"
pat = "AABA"

naive(txt, pat)