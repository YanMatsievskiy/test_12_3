import runner
import runner_and_tournament
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        name_runner = runner.Runner('NIK')
        for i in range(10):
            name_runner.walk()
        self.assertEqual(name_runner.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        name_runner = runner.Runner('ANDREY')
        for i in range(10):
            name_runner.run()
        self.assertEqual(name_runner.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        name_runner_1 = runner.Runner('NIK')
        name_runner_2 = runner.Runner('ANDREY')
        for i in range(10):
            name_runner_1.walk()
            name_runner_2.run()
        self.assertNotEqual(name_runner_1.distance, name_runner_2.distance)


class TournamentTest(unittest.TestCase):
    all_results = None
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = runner_and_tournament.Runner('Усэйн', 10)
        self.andrey = runner_and_tournament.Runner('Андрей', 9)
        self.nik = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        res = {}
        for key, value in cls.all_results.items():
            for k, v in value.items():
                res[k] = str(v)
            print(res)

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        first_run = runner_and_tournament.Tournament(90, self.usain, self.nik)
        result = first_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        second_run = runner_and_tournament.Tournament(90, self.andrey, self.nik)
        result = second_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        third_run = runner_and_tournament.Tournament(90, self.andrey, self.usain, self.nik)
        result = third_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result


if __name__ == '__main__':
    unittest.main()