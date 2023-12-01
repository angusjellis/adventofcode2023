import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class StringSummariser:
    """
    Class to summarise a string
    """

    def __init__(self, filename: str):
        with open(filename, "r") as f:
            self.string = f.read()
            self.valid_string_digits = [
                "one",
                "two",
                "three",
                "four",
                "five",
                "six",
                "seven",
                "eight",
                "nine",
            ]

    def get_sum(self) -> int:
        """
        Get the sum of all combinations of the first and last number in each line
        """
        sum = 0
        for line in self.string.splitlines():
            sum += self.get_combination_from_line(line)
        return sum

    def get_combination_from_line(self, line: str) -> int:
        """
        Get the combination of the first and last number in a string
        Finds the first and last number in a string and combines them into a two digit number
        """
        first_num = None
        last_num = None
        for char in line:
            if char.isdigit():
                if first_num is None:
                    first_num = char
                last_num = char
        combined_num = first_num + last_num
        return int(combined_num)


def main():
    filename = input("Enter filename: ")
    if not os.path.isabs(filename):
        filename = os.path.join(os.path.dirname(__file__), filename)
    summariser = StringSummariser(filename=filename)
    print(summariser.get_sum())


if __name__ == "__main__":
    main()
