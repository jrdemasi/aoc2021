#!/usr/bin/env python3

def read_input():
    coordinates = []
    f = open("input", "r")
    for line in f:
        coord = (line.split()[0], int(line.split()[1]))
        coordinates.append(coord)
    f.close()
    return coordinates

def part1(coordinates):
    horiz = 0 
    depth = 0
    for coord in coordinates:
        if coord[0] == "forward":
            horiz += coord[1]
        elif coord[0] == "up":
            depth -= coord[1]
        elif coord[0] == "down":
            depth += coord[1]
        else:
            print("This shouldn't ever print")
    print("Multiplying final positions together equals {}".format(depth*horiz))
    return    

def part2(coordinates):
    horiz = 0 
    depth = 0
    aim = 0
    for coord in coordinates:
        if coord[0] == "forward":
            horiz += coord[1]
            depth = depth + (aim * coord[1])
        elif coord[0] == "up":
            aim -= coord[1]
        elif coord[0] == "down":
            aim += coord[1]
        else:
            print("This shouldn't ever print")
    print("Multiplying final positions together equals {}".format(depth*horiz))

    return

def main():
    coordinates = read_input()
    part1(coordinates)
    part2(coordinates)
    return

if __name__ == '__main__':
    main()
