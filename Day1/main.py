from solution import Solution

INPUT_FILENAME = "./input.txt"
SHORT = "./short.txt"

def main():
    s = Solution()
    print("Star 1: " + str(s.trebuchet(INPUT_FILENAME)))
    print("Star 2: " + str(s.trebuchet2(INPUT_FILENAME)))

if __name__ == "__main__":
    main()

