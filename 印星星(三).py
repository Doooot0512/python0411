def print_pattern():
    n = 5
    
    for i in range(n // 2 + 1):
        spaces = (n // 2) - i
        stars = 2 * i + 1
        print(" " * spaces + "*" * stars)
    
    for i in range(n // 2):
        spaces = i + 1
        stars = n - 2 * spaces
        print(" " * spaces + "*" * stars)

def main():
    print_pattern()

if __name__ == "__main__":
    main()

