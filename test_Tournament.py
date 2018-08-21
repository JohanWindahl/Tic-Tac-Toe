
from Tournament import Tournament
from unittest import TestCase
from Player import Player








class TestTournament(TestCase):
    def test_create_tournament_tree(self):
        player1 = Player("1", False, None)
        player2 = Player("2", False, None)
        players2 = [player1,player2]

        t2 = Tournament(players2)
        tree2 = t2.create_tournament_tree()
        self.assertEqual(len(tree2), 1)

        player3 = Player("3", False, None)
        player4 = Player("4", False, None)
        players4 = [player1,player2,player3,player4]
        t4 = Tournament(players4)
        tree4 = t4.create_tournament_tree()

        self.assertEqual(len(tree4), 2)

        player5 = Player("5", False, None)
        player6 = Player("6", False, None)
        player7 = Player("7", False, None)
        player8 = Player("8", False, None)

        players8 = [player1, player2, player3, player4,player5, player6, player7, player8]

        t8 = Tournament(players8)
        tree8 = t8.create_tournament_tree()

        self.assertEqual(len(tree8), 4)

        t = Tournament([])
        tree = t.create_tournament_tree()
        self.assertEqual(len(tree), 0)

    def test_print_welcome_message(self):
        self.fail()

    def test_print_tournament(self):
        self.fail()

if __name__ == '__main__':
    tT = TestTournament()
    tT.test_create_tournament_tree()