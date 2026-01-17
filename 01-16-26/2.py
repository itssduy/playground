def main():
    testArr = [1,2,3,4,5,6,7,8,9,10]
    print("For loops")
    printArr()
    printArr5(testArr)
    print("While loops") 
    printLoop()
    printLoop5(testArr)

def printArr():
   for i in range(10):
       print(i+1, sep=" ") 
def printArr5(arr):
   for i in arr:
       if i > 5:
           print(i, sep=" ") 

def printLoop():
   i = 1
   while i <= 10:
       print(i, sep="") 
       i += 1
def printLoop5(arr):
   i = 0
   arrlen = len(arr) 
   while i < arrlen:
       if arr[i] > 5:
           print(arr[i])
       i+=1
if __name__ == "__main__":
    main()