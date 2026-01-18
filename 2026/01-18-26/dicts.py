def main():
    print("count letters")
    print(count_letters("banana"))
    print("\n\nfreq numbers")
    print(freq_numbers([0,1,2,3,4,5,1,2,2,3,3,3,4,4,4,4,5,3,1,2,7,4,8,4,3,2]))

def count_letters(string):
    letters = {}
    for i in string:
        letters[i] = letters.get(i,0) + 1
    return letters

def freq_numbers(list):
    freq = {}
    for i in list:
        freq[i] = freq.get(i, 0) + 1
    
    highest = None
    for k, v in freq.items():
        if highest == None or v > freq[highest]:
            highest = k
    return highest

if __name__ == "__main__":
    main()