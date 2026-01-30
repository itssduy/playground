def main():
    print("Hello world")
    print(longestCommonPrefix(["flower","flow","flight"]))  

def longestCommonPrefix(strs):
      if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]
        least = strs[0]
        for i in strs:
            if len(i) < len(least):
                least = i

        prefix = ""
        for j in range(len(least)):
            for i in strs:
                if i[j] != strs[0][j]:
                    return prefix
            prefix += strs[0][j]


if __name__ == "__main__":
    main()
