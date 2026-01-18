def main():
    print("has duplicates")
    print(has_duplicates([1,2,3,4,5]))
    print(has_duplicates([1,2,3,4,5,1]))
    print("remove duplicates")
    print(remove_duplicates([1,2,3,4,5]))
    print(remove_duplicates([1,2,3,4,5,1]))

def has_duplicates(nums):
    temp = list(set(nums))
    return temp != nums

def remove_duplicates(nums):
    return list(set(nums))


if __name__ == "__main__":
    main()