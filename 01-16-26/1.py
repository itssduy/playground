def main():
    while True: 
        num = input("Number: ")
        if(not num.isnumeric()):
            break
        even_odd(int(num))
    print("Program quit")
def even_odd(n):
    if n % 2 == 1:
        print("Odd")
    else:
        print("Even")

if __name__ == "__main__":
    main()