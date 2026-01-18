def main():
    print("vowels")
    print(count_vowels("happy birthday"))
    print('\n\nreverse')
    print(reverse_string("superman"))

def reverse_string(string):
    return string[::-1]
def count_vowels(string):
    vowels = 'aeiouy'
    vowel_count = 0
    for i in string:
        if vowels.find(i) != -1:   
            vowel_count += 1
            print(i)
            continue
    return vowel_count
if __name__ == "__main__":
    main() 