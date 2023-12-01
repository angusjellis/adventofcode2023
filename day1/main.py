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
            self.valid_string_digits = {
                "o": {"one": "1"},
                "t": {"two": "2", "three": "3"},
                "f": {"four": "4", "five": "5"},
                "s": {"six": "6", "seven": "7"},
                "e": {"eight": "8"},
                "n": {"nine": "9"},
            }
            use_valid_string_digits = input("Use valid string digits? (y/n): ").lower()
            if use_valid_string_digits == "y":
                self.use_valid_string_digits = True
            else:
                self.use_valid_string_digits = False

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
        for i, char in enumerate(line):
            if char.isdigit():
                if first_num is None:
                    first_num = char
                last_num = char
            elif self.use_valid_string_digits:
                matching_values = self.valid_string_digits.get(char)

                if matching_values is not None:

                    print(line, matching_values, char, i)
                    matching_chars = 0
                    for key, value in matching_values.items():
                        current_index = i
                        matching_string = ""
                        for char in key:
                            if current_index >= len(line):
                                break
                            if char == line[current_index]:
                                print(f"Matching {char} with {line[current_index]}")
                                matching_string += line[current_index]
                                print(f"Matching string is now {matching_string}")
                                matching_chars += 1
                                current_index += 1

                                if len(key) == matching_chars:
                                    print(f"Found matching value {key}")
                                    print(line, value)
                                    if first_num is None:
                                        first_num = value
                                    last_num = value
                                    break
                            else:
                                matching_chars = 0
                                current_index = i
                                break

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
