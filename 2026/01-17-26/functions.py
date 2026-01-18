def main():
    print('square')
    print(square(5))
    print('\n\nis_positive')
    print(is_positive(10))
def square(x):
    return pow(x,2)

def is_positive(x):
    if x > 0:
        return True
if __name__ == "__main__":
    main()