def longestCommonPrefix( strs):
    strs.sort()
    i = 0
    first = strs[0]
    last = strs[-1]

    while i < len(strs[0]) and first[i] == last[i]:
        i+=1
    return first[:i]


