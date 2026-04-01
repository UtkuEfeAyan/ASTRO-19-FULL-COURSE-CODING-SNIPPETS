#function f(x) that returns x^3 + 8
def f(x):
    return x**3 + 8

def main():
    var1 = 9
    #var1 = input("Enter a number: ")
    result = f(int(var1))
    print("Result:", result)
    if result > 27:
        print("YAY!")

if __name__ == "__main__":
    main()
