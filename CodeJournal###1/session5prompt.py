#imported math
import math

# program that graphs the numbers in a grid using math functions
def graphNumbersInGrid():
    varLowLimit = 0
    varHighLimit = 2 * math.pi
    varNumEntries = 1000
    step = (varHighLimit - varLowLimit) / varNumEntries
    
    for i in range(varNumEntries):
        x = i * step
        print("x:", x, "sin(x):", math.sin(x), end="\n")
    print()
    
#main
def main():
    graphNumbersInGrid()

if __name__ == "__main__":
    main()
    
#date: 2026-04-02