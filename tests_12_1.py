import runner
import unittest
import random


def generate_random_name():
    name = ""
    vowels = 'ауеыоэёяию'
    consonants = 'бвгджзйклмнпрстфхцчшщь'

    for i in range(2):
        name += random.choice(consonants)
        name += random.choice(vowels)

    name = name.capitalize()
    return name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_1 = runner.Runner(generate_random_name())
        for i in range(10):
            runner.Runner.walk(runner_1)
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_1 = runner.Runner(generate_random_name())
        for i in range(10):
            runner.Runner.run(runner_1)
        self.assertEqual(runner_1.distance, 100)

    def test_challenge(self):
        runner_1 = runner.Runner(generate_random_name())
        runner_2 = runner.Runner(generate_random_name())

        methods = [runner.Runner.run, runner.Runner.walk]

        for i in range(10):
            random.choice(methods)(runner_1)
            random.choice(methods)(runner_2)
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == '__main__':
    unittest.main()
