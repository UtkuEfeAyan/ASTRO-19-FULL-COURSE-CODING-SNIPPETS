
# program that prints the sum of floating point numbers from 2 inputs type defined
def sum_floating_point_numbers():
    float1 = float(input("Enter first floating point number: "))
    float2 = float(input("Enter second floating point number: "))
    total = float1 + float2
    print("Sum of floating point numbers:", total, "\n Type:", type(total))

#program that prints the difference between two integers type defined
def difference_between_integers():
    int1 = int(input("Enter first integer: "))
    int2 = int(input("Enter second integer: "))
    diff = int1 - int2
    print("Difference between integers:", diff, "\n Type:", type(diff))



def main():
    sum_floating_point_numbers()
    difference_between_integers()

if __name__ == "__main__":
    main()