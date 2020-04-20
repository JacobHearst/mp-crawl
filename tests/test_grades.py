from mp_scraper.grades import YDS, Hueco, Ice
import unittest


class TestGrades(unittest.TestCase):
    def run_test_matrix(self, matrix, GradeType):
        for case in matrix:
            with self.subTest(grade=case[0]):
                self.assertEqual(GradeType(case[0]).index(), case[1])

    def test_yds(self):
        with self.subTest(test="Single digit"):
            self.run_test_matrix([
                ["3rd", 0],
                ["4th", 1],
                ["Easy 5th", 2],
                ["5.0-", 3],
                ["5.0", 4],
                ["5.0+", 5],
                ["5.6", 22],
                ["5.9", 31],
                ["5.9+", 32]
            ], YDS)

        with self.subTest(test="Double digit"):
            self.run_test_matrix([
                ["5.10a", 33],
                ["5.11a/b", 41],
                ["5.12-", 48],
                ["5.13b", 56],
                ["5.14b/c", 64],
                ["5.15", 71],
                ["5.10c", 37],
                ["5.11c/d", 45],
                ["5.12+", 52],
                ["5.15d", 74]
            ], YDS)

    def test_hueco(self):
        self.run_test_matrix([
            ["V-easy", 0],
            ["VB", 0],
            ["V0-", 1],
            ["V0", 2],
            ["V0+", 3],
            ["V6-7", 21],
            ["V8+", 27],
            ["V17", 53],
            ["V17+", 54]
        ], Hueco)

    def test_ice(self):
        self.run_test_matrix([
            ["WI1", 1],
            ["WI2", 4],
            ["WI3-4", 8],
            ["WI5+", 14],
            ["WI2-", 3],
            ["AI1", 1],
            ["AI4-", 9],
            ["AI2+", 5],
            ["AI1-", 0],
        ], Ice)


if __name__ == "__main__":
    unittest.main()
