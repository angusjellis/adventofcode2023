import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class GameSummariser:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def set_games(self):
        with open(self.filename) as f:
            self.games = {}
            game_string = f.read()
            lines = game_string.splitlines()

            for line in lines:
                game_number, reveals = line.split(":")
                game_number = int(game_number.split(" ")[1])
                reveals = reveals.strip()
                reveals = reveals.split(";")
                self.games[game_number] = reveals

    @staticmethod
    def get_max_for_colours(games: dict) -> dict:
        for game, reveals in games.items():
            green_max = 0
            blue_max = 0
            red_max = 0
            for reveal in reveals:
                reveal = reveal.strip()
                reveal = reveal.split(",")
                for r in reveal:
                    r = r.strip()
                    print(r)
                    number, colour = r.split(" ")
                    print(colour, number)
                    number = int(number)
                    if colour == "green":
                        if number > green_max:
                            green_max = number
                    elif colour == "blue":
                        if number > blue_max:
                            blue_max = number
                    elif colour == "red":
                        if number > red_max:
                            red_max = number
            games[game] = {"green": green_max, "blue": blue_max, "red": red_max}
        return games

    def summarise(self):
        self.set_games()
        self.games_with_max_colours = self.get_max_for_colours(self.games)
        self.games_with_possibility = self.find_possible_games(
            self.games_with_max_colours
        )
        return self.games_with_possibility

    @staticmethod
    def find_possible_games(games: dict) -> dict:
        red_max = 12
        blue_max = 14
        green_max = 13
        possible_games = 0
        for reveals in games.values():
            reveals["possible"] = False
            if (
                reveals["red"] <= red_max
                and reveals["blue"] <= blue_max
                and reveals["green"] <= green_max
            ):
                possible_games += 1
                reveals["possible"] = True
        return games

    @staticmethod
    def summarise_ids_of_possible_games(games) -> list:
        id_sum = 0
        for id, game in games.items():
            if game["possible"]:
                id_sum += id
        return id_sum

    @staticmethod
    def get_sum_of_power_of_max_colours(games: dict) -> dict:
        sum = 0
        for id, game in games.items():
            green_max = game["green"]
            blue_max = game["blue"]
            red_max = game["red"]
            power = green_max * blue_max * red_max
            games[id]["power"] = power
            sum += power
        return sum


if __name__ == "__main__":
    filename = "input.txt"
    if not os.path.isabs(filename):
        filename = os.path.join(os.path.dirname(__file__), filename)
    summariser = GameSummariser(filename=filename)
    games_with_possibility = summariser.summarise()
    id_sum = summariser.summarise_ids_of_possible_games(games_with_possibility)
    power_sum = summariser.get_sum_of_power_of_max_colours(games_with_possibility)
    print(power_sum)
