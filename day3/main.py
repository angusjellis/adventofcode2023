import os
import sys

import re

# Something is adjacent if it is it is seperated from the symbol by one unit
# in the x or y direction. So, if the symbol is at (1, 2), then the adjacent
# symbols are at (0, 2), (2, 2), (1, 1), and (1, 3).
# Parts of the grid that are not adjacent to any symbol are not considered
# Periods do not count as symbols

# The grid is a list of lists, where each list is a row of the grid
# If a character is not a standard letter or a number or a period, it is
# considered a symbol

# We can't just compare individual characters as part numbers can be multiple digits

# Let's create a coordinate system for the grid, where the origin is the top left
# corner of the grid, and the x axis increases to the right, and the y axis
# increases downwards

# Part numbers will have attributes of starting_coordinate, ending_coordinate
# and length

# Symbols will have attributes of coordinate


symbol_regex = r"[^a-zA-Z0-9\.]"

class SchematicParser:
    def __init__(self, filename: str) -> None:
        self.filename = filename
    
    def parse(self):
        with open(self.filename) as f:
            grid = []
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                grid.append(line)

        self.grid = grid
        self.create_part_number_objects(grid)
        self.check_part_numbers_against_symbols(grid, self.part_numbers_with_coordinates)


    def create_part_number_objects(self, grid: list) -> list:
        self.part_numbers_with_coordinates = {}
        for i, row in enumerate(grid):
            self.check_row(row=row, row_index=i)
        

    def check_row(self, row: str, row_index: int, start_index: int=0) -> None:
            row = row[start_index:]
            for col_index, char in enumerate(row):                
                if char.isdigit():
                    part_number, part_coordinate = self.get_part_number(self.grid, row_index, col_index, part_number=char, row=row)
                    self.part_numbers_with_coordinates[part_coordinate] = part_number
                    self.check_row(row=row, row_index=row_index, start_index=col_index + len(part_number))
                    break

    def get_part_number(self, grid: list, row_index: int, col_index: int, row: str, part_number: str) -> dict:        
        current_coordinate = (col_index, row_index)
        if col_index + 1 < len(row):
            next_char = row[col_index + 1]
            if next_char.isdigit():
                current_coordinate = (col_index, row_index)
                part_number += next_char
                part_number, updated_coordinate = self.get_part_number(grid, row_index, col_index + 1, row, part_number)
        return part_number, current_coordinate
    
    def get_adjacent_symbols(self, grid: list, coordinate: tuple) -> list:
        adjacent_symbols = []
        x, y = coordinate
        if x - 1 >= 0:
            adjacent_symbols.append(grid[y][x - 1])
        if x + 1 < len(grid[y]):
            adjacent_symbols.append(grid[y][x + 1])
        if y - 1 >= 0:
            adjacent_symbols.append(grid[y - 1][x])
        if y + 1 < len(grid):
            adjacent_symbols.append(grid[y + 1][x])
        return adjacent_symbols
    
    def check_part_numbers_against_symbols(self, grid: list, part_numbers: list) -> None:
        coordinates_with_part_numbers = self.part_numbers_with_coordinates.items()
        valid_part_numbers = []
        part_number_list = []
        for coordinate, part_numbers in coordinates_with_part_numbers:
            part_number_list.append(part_numbers)
            start_x, start_y = coordinate
            if start_y - 1 >= 0:
                adjacent_y = start_y - 1, start_y + 1
                y_range = range(*adjacent_y)
            else:
                adjacent_y = start_y, start_y + 1
                y_range = range(*adjacent_y)

            if start_x - 1 >= 0:
                adjacent_x = start_x - 1, (start_x + len(part_numbers) - 1)
                x_range = range(*adjacent_x)
            else:
                adjacent_x = start_x + 1
                x_range = range(adjacent_x)
            
            part_number_valid = False
            for x in x_range:
                for y in y_range:
                    # a symbol is anything that isn't a letter, number, or period
                    symbol = grid[y][x]
                    if part_numbers == "501":
                        print(symbol)
                        print(start_y, start_y + 1)
                        for y in range(start_y, start_y + 1):
                            print(grid[y][x])
                    symbol_regex = r"[^a-zA-Z0-9\.]"
                    if symbol != ".":
                        if re.match(symbol_regex, symbol):
                            part_number_valid = True
                            break

            if part_number_valid:
                valid_part_numbers.append(part_numbers)
        
        valid_part_number_sum = sum([int(part_number) for part_number in valid_part_numbers])
        
    
    

def main():
    filename = "input.txt"
    if not os.path.isabs(filename):
        filename = os.path.join(os.path.dirname(__file__), filename)
    parser = SchematicParser(filename)
    parser.parse()

if __name__ == "__main__":
    main()