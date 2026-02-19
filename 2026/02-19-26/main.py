import csv

def main():
    print("Hello, world!") 
    readFile()

def readFile():
    file_name = "test.csv"
    with open(file_name, "r") as file:
        for i in csv.DictReader(file):
            print(i)
        # for i in file:
            # print(i, end="")
if __name__ == "__main__":
    main()
