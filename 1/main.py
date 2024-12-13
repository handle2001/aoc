"""
AOC Day 1

Throughout the Chief's office, the historically significant locations are 
listed not by name but by a unique number called the location ID. To make
sure they don't miss anything, The Historians split into two groups, each
searching the office and trying to create their own complete list of
location IDs.

There's just one problem: by holding the two lists up side by side
(your puzzle input), it quickly becomes clear that the lists aren't very
similar. Maybe you can help The Historians reconcile their lists?
"""

class DayOne():
    """Class holding properties and methods for solving AOC Day One"""

    left_list: list[int] = []
    right_list: list[int] = []
    distance: list[int] = []

    def __init__(self, inputfile) -> None:
        """Initialize both lists from the input file"""
        with open(inputfile, "r") as input_lists:
            for line in input_lists:
                l,r = line.rsplit("   ")
                self.left_list.append(int(l))
                self.right_list.append(int(r))
            self.left_list.sort()
            self.right_list.sort()

    def calculate_distance(self) -> int:
        """Calculate the distances between both lists"""
        for j in self.left_list:
            for k in self.right_list:
                self.distance.append(abs(k - j))
        return sum(self.distance)

def main():
    """Do the thing"""
    day_one = DayOne("input.txt")
    solution = day_one.calculate_distance()
    print(solution)

if __name__ == "__main__":
    main()
