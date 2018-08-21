
from Platform import Platform
from Player import Player
from Tournament import Tournament


class UINavigator:
    # function for not a valid input option
    def notValidInput(self):
        """
        Function: Print warning if the user does not select a valid input.
        """

        print("")
        print("You have not selected a valid option!")
        print("")

    # function for continue and finish the tournament.
    def continueTournament(self, tournament):
        newPlayersList = []
        playersOfTournament = tournament.players
        tournament.print_tournament()
        tournamentContinues = True

        while True:
            # Loops with 2 step each time to avoid that same player plays multiply times.
            for x in range(0, len(playersOfTournament) - 1, 2):
                winnersName = Platform(playersOfTournament[x], playersOfTournament[x+1]).startGame()

                # Add the player that won the game.
                if winnersName == playersOfTournament[x].name:
                    newPlayersList.append(playersOfTournament[x])
                else:
                    # Reset th players moves.
                    newPlayersList.append(playersOfTournament[x+1])
            # Check if the tournament is finished.
            if len(newPlayersList) == 1:
                tournamentContinues = False

            # If the tournament is not finished it start over with the player that are left.
            if tournamentContinues:
                NewTournament = Tournament(newPlayersList)
                self.continueTournament(NewTournament)
            else:
                print(newPlayersList[0].name + " has won the tournament!!")
                break
            break

    # function for creating a tournament with enterd amount of players.
    def startTournament(self):
        """
        Function: Create the tournament tree with entered amount of player
        """

        try:
            print
            "How many players will participate in the tournament?"
            amount_of_players = int(input("Choose between 2,4 or 8 participates: _"))
            if 2 == amount_of_players or amount_of_players == 4 or amount_of_players == 8:
                players = self.createPlayers(amount_of_players)
                tournament = Tournament(players)
                self.continueTournament(tournament)

            else:
                print
                "Incorrect input for amount of participants, try again!\n\n"
                self.startTournament()
        except ValueError:
            print
            "Incorrect input for amount of participants, try again!\n\n"
            self.startTournament()

    # fucntion for priting the start menu.
    def print_menu(self):
        """
        Function: Print the Main Menu
        """

        print("")
        print("")
        print("******TIC***TAC***TOE***MENU***********")
        print("")
        print("[S]tart game")
        print("[T]ournament")
        print("[Q]uit game")
        print("")
        print("****************************************")
        print("")

    def choose_mode(self):
        """
        Function: Handle the user valid-input based on the main menu.
        """

        done = False

        while not done:

            self.print_menu()

            select_option = input("What do you want to do? Please choose between S, T, or Q _").lower()

            if select_option == "s":
                self.startQuickMatch()


            elif select_option == "t":
                self.startTournament()


            elif select_option == "q":
                loopQuit = True
                while loopQuit:
                    select_option_quit = input("Do you really want to quit? \n[Y]es / [N]o \n").lower()
                    if select_option_quit == "y":
                        print("")
                        print("Thanks for playing!")
                        print("Goodbye")
                        loopQuit = False
                        done = True

                    elif select_option_quit == "n":
                        loopQuit = False
                    else:
                        self.notValidInput()
            else:
                self.notValidInput()

    def createPlayers(self, amount_of_players):
        """
        Function:   Handle the player creation if it is a human or AI, and also the AI level.
        Return:     List of created players
        """

        # Creates a list of players
        players = []

        for i in range(1, amount_of_players + 1):
            print
            "\nCreating player number " + str(i)
            # Creates a new player
            while True:
                player_name = input("Choose name for player " + str(i) + " _")
                if player_name.isspace() == False and player_name != "":
                    break
                print("Invalid name")

            player = Player(player_name, False, None)

            while True:
                # User can define the player type, Human or AI
                player_type = input("Choose the type for " + str(player_name) + "\n1. Player" + "\n2. AI _").lower()

                if player_type == "1":
                    break
                if player_type == "2":
                    break

            # Choosing AI level
            if player_type == "2":

                while True:
                    ai_level = input(
                        "Choose the AI level for " + str(player_name) + "\n1.Easy \n2.Medium \n3.Hard").lower()

                    if ai_level == "1":
                        break
                    if ai_level == "2":
                        break
                    if ai_level == "3":
                        break
                player.setIsAI(True)
                player.setAIlevel(ai_level)
            players.append(player)
        return players

    # function for starting a quickmatch with different options PvP PvAI, AIvAI
    def startQuickMatch(self):
        """
        Function: Handle a single game. It can be Player vs Player, Player vs AI, or AI vs AI.
        """

        loopQuit = True
        while loopQuit:

            # Menu for startQuickMatch
            print("")
            print("")
            print("******GAME MODE ***********************")
            print("")
            print("1. Player vs Player ")
            print("2. Player vs AI ")
            print("3. AI vs AI ")
            print("4. Go back to menu")
            print("****************************************")
            print("")
            select_option_singlegame = input("Enter number on what type of game you wanna play: ")

            '''
            select_option_singlegame = raw_input(
                "Do you want to play: \n"
                "1. Player vs Player \n"
                "2. Player vs AI \n"
                "3. AI vs AI \n"
                "4. Go back to menu\n").lower()
            '''
            winnersName = ""
            # Player vs Player
            if select_option_singlegame == "1":

                while True:
                    p1_name = input("\n\n\nEnter the name of player 1: ")
                    if p1_name.isspace() == False and p1_name != "":
                        break
                    print("Invalid name")

                while True:
                    p2_name = input("Enter the name of player 2: ")
                    if p2_name.isspace() == False and p2_name != "":
                        break
                    print("Invalid name")

                print(" \n \n")

                player1 = Player(p1_name, False, None)
                player2 = Player(p2_name, False, None)

                Platform(player1, player2).startGame()

            # Player vs AI
            elif select_option_singlegame == "2":

                while True:
                    p1_name = input("Enter the name of player 1: ")
                    if p1_name.isspace() == False and p1_name != "":
                        break
                    print("Invalid name")

                while True:
                    ai_name = input("Enter the name of the AI: ")
                    if ai_name.isspace() == False and ai_name != "":
                        break
                    print("Invalid name")

                correctAiLevelGiven = False

                while not correctAiLevelGiven:

                    try:
                        while True:
                            ai_level = input(
                                "Enter the level of the AI: \n1.Easy \n2.Medium \n3.Hard ").lower()

                            if ai_level == "1":
                                break
                            if ai_level == "2":
                                break
                            if ai_level == "3":
                                break
                            print
                            'Invalid input for AI level, number expected \n'

                        ai_level_int = int(ai_level)

                        player1 = Player(p1_name, False, None)
                        ai_player = Player(ai_name, True, ai_level_int)
                        Platform(player1, ai_player).startGame()

                        correctAiLevelGiven = True
                    except ValueError:
                        print
                        'Invalid input for AI level, number expected \n'

            elif select_option_singlegame == "3":
                # AI vs AI
                while True:
                    ai1_name = input("Enter the name of the first AI: ")
                    if ai1_name.isspace() == False and ai1_name != "":
                        break
                    print("Invalid name")

                while True:
                    ai2_name = input("Enter the name of the second AI: ")
                    if ai2_name.isspace() == False and ai2_name != "":
                        break
                    print("Invalid name")


                correctAiLevelGiven = False

                while not correctAiLevelGiven:

                    try:
                        while True:
                            ai1_level = input(
                                "Enter the level of " + ai1_name + ": \n1.Easy \n2.Medium \n3.Hard ").lower()

                            if ai1_level == "1":
                                break
                            if ai1_level == "2":
                                break
                            if ai1_level == "3":
                                break
                            print
                            'Invalid input for AI level, number expected \n'

                        ai1_level_int = int(ai1_level)

                        while True:
                            ai2_level = input(
                                "Enter the level of " + ai2_name + ": \n1.Easy \n2.Medium \n3.Hard ").lower()

                            if ai2_level == "1":
                                break
                            if ai2_level == "2":
                                break
                            if ai2_level == "3":
                                break
                            print
                            'Invalid input for AI level, number expected \n'

                        ai2_level_int = int(ai2_level)

                        ai1_player = Player(ai1_name, True, ai1_level_int)
                        ai2_player = Player(ai2_name, True, ai2_level_int)

                        winnersName = Platform(ai1_player, ai2_player).AIvsAI()
                        print("\nCongratulation, " + winnersName + " win!")

                        correctAiLevelGiven = True
                    except ValueError:
                        print
                        'Invalid input for AI level, number expected\n'
            elif select_option_singlegame == "4":
                loopQuit = False

            else:
                self.notValidInput()


# Main loop with a new UINavigator
if __name__ == '__main__':

    try:
        ui = UINavigator()
        ui.choose_mode()
    except KeyboardInterrupt:
        print
        "\nGoodbye, see ya!"
