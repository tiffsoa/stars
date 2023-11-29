def main():
    print("Square")
    n = 5
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()
    print("Increasing Triangle")
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()
    print("Decreasing Triangle")
    for i in range(n):
        for j in range(n - i):   # or for j in range(i, 5)
            print("*", end=" ")
        print()
    print("")
    print("Right Sided Triangle")  # Decreasing Space + Increasing Triangle
    for i in range(n):
        for j in range(n - i):
            print(" ", end=" ")
        for k in range(i+1):
            print("*", end=" ")
        print()
    print("Upper Right Triangle")
    for i in range(n):
        for j in range(i+1):
            print(" ", end=" ")
        for k in range(n-i):
            print("*", end=" ")
        print()
    print("Pyramid")
    for i in range(n):
        for j in range(n-i):
            print(" ", end=" ")
        for k in range(i+1):
            print("*", end=" ")
        for e in range(i):
            print("*", end=" ")
        print()
    print("Upside Down Pyramid")
    for i in range(n):
        for e in range(i+1):
            print(" ", end=" ")
        for j in range(n-i):
            print("*", end=" ")
        for k in range(n-1-i):
            print("*", end=" ")
        print()


if __name__ == '__main__':
    main()

