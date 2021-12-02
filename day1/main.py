#!/usr/bin/env python3

# Let's just read the inputs once and convert to an int
def read_input():
    measurements = []
    f = open("input", "r")
    for line in f:
        measurements.append(int(line))
    f.close()
    return measurements

def part1(measurements):
    previous = None
    num_greater = 0
    for measurement in measurements:
        if previous:
            if measurement > previous:
                num_greater += 1
            previous = measurement
        else:
            previous = measurement
    print("The total number of greater measurements is {}".format(num_greater))
    return

def part2(measurements):
    previous = None
    num_greater = 0 
    window_size = 3
    for i in range(len(measurements) - window_size + 1):
        window = measurements[i: i + window_size]
        if previous:
            new = sum(window)
            if new > previous:
                num_greater += 1
            previous = new
        else:
            previous = sum(window)
    print("The total number of greater measurements based on the sliding window is {}".format(num_greater))
    return

def main():
    measurements = read_input()
    part1(measurements)
    part2(measurements)
    return

if __name__ == '__main__':
    main()
