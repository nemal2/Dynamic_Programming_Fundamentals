def z_arr(str):
    n = len(str)
    z = [0]*n
    l = 0
    r = 0
    for i in range(1,n):
        if i > r:
            l = r = i
            while r < n and str[r-l] == str[r]:
                r+=1
            z[i] = r-l
            r-=1
        else:
            k1 = i-l
            # if z[k1] < r-i+1:
            #     z[i] = z[k1]
            # else:
            #     l = i
            #     while r < n and str[r-l] == str[r]:
            #         r+=1
            #     z[i] = r-l
            #     r-=1
    return z



def z_algo(pat,txt):
    com = pat + "$" + txt
    z = z_arr(com)

    ans = []
    pat_len = len(pat)

    for i in range(len(com)):
        if z[i] == pat_len:
            ans.append(i - pat_len - 1)

    return ans

pat = "abc"
txt = "ababcabc"
print(z_algo(pat,txt))