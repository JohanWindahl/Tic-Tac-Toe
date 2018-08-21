import random
from Platform import Platform


class Tournament:

    def __init__(self, players):

        self.players = players
        self.tournament_tree = self.create_tournament_tree()


    def create_tournament_tree(self):
        """
        Function: Create the tournament tree
        """
        random.shuffle(self.players)

        tournament_tree = []

        i = 0
        while i < len(self.players):
            platform = Platform(self.players[i], self.players[i+1])
            tournament_tree.append([platform])
            i = i + 2

        return tournament_tree

    def print_welcome_message(self):
        """
        Function: Print tournament welcome message
        """
        print("\n\n######################################")
        print("########## Let the games begin! ######")
        print("######################################\n\n")

    def print_tournament(self):

        self.print_welcome_message()
        for platform in self.tournament_tree:

            print("---------" + str(platform))

            # Checks if player is last
            if platform is self.tournament_tree[len(self.tournament_tree)-1]:
                break

            for i in range(0, 5):
                print("|")
