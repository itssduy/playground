def main():
    print('largest number')
    print(largest_number([1,2,3,4,5,99,31,1,44,52]))
    print('is palindrome')
    print(is_palindrome("tacocat"))
    print(is_palindrome("hello"))
    print("count words")
    print(count_words("today i met a bike that could ride a bike inside of a bike"))
    print('remove duplicates')
    print([1,2,3,4,5,566,6,7,3,213,2,3,4,55,6,7,8,9,1,2,3,4])

def largest_number(l):
    if len(l) < 1:
        return None
    largest = l[0]
    for i in l:
        if i > largest:
            largest = i
    return largest

def is_palindrome(string):
    return string == string[::-1]

def count_words(sentence):
    word_list = sentence.split(" ")
    dict = {}

    for i in word_list:
        dict[i] = dict.get(i,0) + 1
    return dict

def remove_duplicates(l):
    return list(set(l))

if __name__ == "__main__":
    main()