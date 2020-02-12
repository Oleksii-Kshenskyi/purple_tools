import sys

def accumulate(limiter):
    number = int(limiter)

    acc = 0
    count = 0
    while acc <= number:
        count += 1
        if (acc + count) > number:
            break
        acc += count

    print("Range of the accumulator: 1 to", count - 1)
    print("The remainder is:", number - acc)

def calculate_sum(low, high):
    acc = 0
    for i in range(low, high + 1):
        acc += i

    print("The sum of numbers in range(",low,", ",high,") is ", acc, sep='')

if __name__ == "__main__":
    try:
        if sys.argv[1] == '-a':
            accumulate(int(sys.argv[2]))
        elif sys.argv[1] == '-c':
            calculate_sum(int(sys.argv[2]), int(sys.argv[3]))
        else:
            print("usage:\n", "\tcounter.py [-a|-c] [limiter|low_lim high_lim]")
    except Exception as e:
        print("This thing went WRONG:", e)

