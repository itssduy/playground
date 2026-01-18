def main():
    nums = [1,2,3,4,5]
    print("set")
    print(sum_list(nums))
    print("\n\nmin")
    print(min_list(nums))

def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum

def min_list(list):
    if(len(list) < 1):
        return -1
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min
if __name__ == "__main__":
    main()