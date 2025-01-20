import unittest
from runner_and_tournament import Tournament, Runner


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        print("Результаты всех тестов:")
        for test_name, result in cls.all_results.items():
            print(f"{test_name}: {result}")

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.__class__.all_results["test_usain_and_nick"] = {
            place: runner.name for place, runner in results.items()
        }
        self.assertTrue(results[max(results.keys())].name == "Ник")

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results["test_andrey_and_nick"] = {
            place: runner.name for place, runner in results.items()
        }
        self.assertTrue(results[max(results.keys())].name == "Ник")

    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results["test_usain_andrey_and_nick"] = {
            place: runner.name for place, runner in results.items()
        }
        self.assertTrue(results[max(results.keys())].name == "Ник")


if __name__ == "__main__":
    unittest.main(verbosity=2)