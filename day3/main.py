#!/usr/bin/env python3

def read_input():

    # Get a max length to make sure no funny business
    max_length = 0 
    numbers = []
    with open("input", "r") as f:
        for line in f:
            number = line.strip("\n")
            if len(number) > max_length:
                max_length = len(number)
            numbers.append(number)
    return max_length, numbers

def to_decimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def find_oxygen_generator_rating(max_length, numbers):
    most_common_bits = [0] * max_length
    for i in range(max_length):
        zeroes = 0 
        ones = 0 
        for number in numbers:
            if number[i] == "0":
            elif number[i] == "1";
            else:
                print("This should never print")
        if zeroes >  ones:
        elif zeroes < ones:
        else:
    return

def find_scrubber_rating:
    return

def part2(max_length, numbers):
    return

def part1(max_length, numbers):

    gamma = [0] * max_length
    for i in range(max_length):
        zeroes = 0 
        ones = 0
        for number in numbers:
            if number[i] == "0":
                zeroes += 1
            elif number[i] == "1":
                ones += 1
            else:
                print("This should never print")
        if zeroes > ones:
            gamma[i] = 0
        else:
            gamma[i] = 1

    epsilon = [0] * max_length
    for i in range(max_length):
        zeroes = 0
        ones = 0
        for number in numbers:
            if number[i] == "0":
                zeroes += 1
            elif number[i] == "1":
                ones += 1
            else:
                print("This should never print")
        if zeroes < ones:
            epsilon[i] = 0
        else:
            epsilon[i] = 1

    gamma = [str(int) for int in gamma]
    gamma = int("".join(gamma))
    epsilon = [str(int) for int in epsilon]
    epsilon = int("".join(epsilon))
    return gamma, epsilon

def main():

    max_length, numbers = read_input()
    gamma, epsilon = part1(max_length, numbers)
    print("Power consumption: {}".format(to_decimal(gamma)*to_decimal(epsilon)))
    return

if __name__ == '__main__':
    main()
