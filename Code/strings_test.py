#!python

from strings import contains, find_index, find_all_indexes
import unittest


class StringsTest(unittest.TestCase):

    def test_contains_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert contains('abc', '') is True  # all strings contain empty string
        assert contains('abc', 'a') is True  # single letters are easy
        assert contains('abc', 'b') is True
        assert contains('abc', 'c') is True
        assert contains('abc', 'ab') is True  # multiple letters are harder
        assert contains('abc', 'bc') is True
        assert contains('abc', 'abc') is True  # all strings contain themselves
        assert contains('aaa', 'a') is True  # multiple occurrences
        assert contains('aaa', 'aa') is True  # overlapping pattern
        self.assertTrue(contains('Spider-Man', 'spider'))
        self.assertTrue(contains("I'll Be Back", "i'll"))
        self.assertTrue(contains("Never Gonna Give You Up", "give you"))

    def test_contains_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert contains('abc', 'z') is False  # remember to test other letters
        assert contains('abc', 'ac') is False  # important to test close cases
        assert contains('abc', 'az') is False  # first letter, but not last
        assert contains('abc', 'abz') is False  # first 2 letters, but not last
        assert contains("I am your father", "mother") is False
        assert contains("Star Wars", 'star-wars') is False

    def test_contains_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert contains('ababc', 'ab') is True  # multiple occurrences
        assert contains('banana', 'na') is True  # multiple occurrences
        assert contains('ababc', 'abc') is True  # overlapping prefix
        assert contains('bananas', 'nas') is True  # overlapping prefix
        self.assertTrue(contains('aaaaababbabc', 'abc'))
        self.assertTrue(contains('wingardium leviosa', 'M l'))
        self.assertTrue(contains('bb Beibi/be', 'be'))
        self.assertTrue(find_index("rat a tat cat", "at"))

    def test_find_index_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert find_index('abc', '') == 0  # all strings contain empty string
        assert find_index('abc', 'a') == 0  # single letters are easy
        assert find_index('abc', 'b') == 1
        assert find_index('abc', 'c') == 2
        assert find_index('abc', 'ab') == 0  # multiple letters are harder
        assert find_index('abc', 'bc') == 1
        assert find_index('abc', 'abc') == 0  # all strings contain themselves
        assert find_index('aaa', 'a') == 0  # multiple occurrences
        assert find_index('aaa', 'aa') == 0  # overlapping pattern
        self.assertEqual(find_index("Where's Waldo?", 'w'), 0)

    def test_find_index_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert find_index('abc', 'z') is None  # remember to test other letters
        assert find_index('abc', 'ac') is None  # important to test close cases
        assert find_index('abc', 'az') is None  # first letter, but not last
        assert find_index('abc', 'abz') is None  # first 2, not last letter
        self.assertIs(find_index('Mecca', 'Makkah'), None)
        self.assertIs(find_index('GoogleMePlease', 'Google me'), None)

    # Difficult test cases (examples) with complex patterns
    def test_find_index_with_complex_patterns(self):
        # overlapping prefix
        assert find_index('ababc', 'abc') == 2
        # overlapping prefix
        assert find_index('bananas', 'nas') == 4
        # multiple occurrences
        assert find_index('abcabcabc', 'abc') == 0
        # multiple occurrences
        assert find_index('abcabcab', 'abc') == 0
        # overlapping prefix
        assert find_index('abcabcdef', 'abcd') == 3
        # overlapping prefix
        assert find_index('abcabcdef', 'abcdef') == 3
        # overlapping prefix
        assert find_index('abcabcdabcde', 'abcde') == 7
        # multiple occurrences, overlapping prefix
        assert find_index('abcabcdabcde', 'abcd') == 3
        # multiple occurrences
        assert find_index('abra cadabra', 'abra') == 0
        # overlapping prefix
        assert find_index('abra cadabra', 'adab') == 6
        assert find_index('oooooh', 'oooh') == 2
        assert find_index('oooooooooh', 'oooh') == 6
        self.assertEqual(find_index('adcf', ''), 0)
        self.assertEqual(find_index("windwums are chummy-chum'd", "um'"), 22)
        self.assertEqual(find_index("cuckoo for cococoa puffs", 'coa'), 15)
        self.assertEqual(find_index("rat a tat cat", "at"), 1)

    # Positive test cases (examples) with matching patterns
    def test_find_all_indexes_with_matching_patterns(self):
        # all strings contain empty string
        assert find_all_indexes('abc', '') == [0, 1, 2]
        # single letters are easy
        assert find_all_indexes('abc', 'a') == [0]
        assert find_all_indexes('abc', 'b') == [1]
        assert find_all_indexes('abc', 'c') == [2]
        # multiple letters are harder
        assert find_all_indexes('abc', 'ab') == [0]
        assert find_all_indexes('abc', 'bc') == [1]
        # all strings contain themselves
        assert find_all_indexes('abc', 'abc') == [0]
        # multiple occurrences
        assert find_all_indexes('aaa', 'a') == [0, 1, 2]
        assert find_all_indexes('aaa', 'aa') == [0, 1]  # overlapping pattern

        self.assertEqual(find_all_indexes('abc', ''), [0, 1, 2])
        self.assertEqual(find_all_indexes('aaa', 'a'), [0, 1, 2])
        self.assertEqual(find_all_indexes("Darth Vader's dark", 'd'),
                         [0, 8, 14])

    # Negative test cases (counterexamples) with non-matching patterns
    def test_find_all_indexes_with_non_matching_patterns(self):
        # remember to test other letters
        assert find_all_indexes('abc', 'z') == []
        # important to test close cases
        assert find_all_indexes('abc', 'ac') == []
        # first letter, but not last
        assert find_all_indexes('abc', 'az') == []
        # first 2 letters, but not last
        assert find_all_indexes('abc', 'abz') == []

        self.assertEqual(find_all_indexes('avv', 'vg'), [])
        self.assertEqual(find_all_indexes('ygd', 'z'), [])
        self.assertEqual(find_all_indexes('math rocks', 'cs rocks'), [])

    def test_find_all_indexes_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert find_all_indexes('ababc', 'abc') == [2]  # overlapping prefix
        # overlapping prefix
        assert find_all_indexes('bananas', 'nas') == [4]
        # multiple occurrences
        assert find_all_indexes('abcabcabc', 'abc') == [0, 3, 6]
        # multiple occurrences
        assert find_all_indexes('abcabcab', 'abc') == [0, 3]
        # overlapping prefix
        assert find_all_indexes('abcabcdef', 'abcd') == [3]
        # overlapping prefix
        assert find_all_indexes('abcabcdef', 'abcdef') == [3]
        # overlapping prefix
        assert find_all_indexes('abcabcdabcde', 'abcde') == [7]
        # multiple occurrences, overlapping prefix
        assert find_all_indexes('abcabcdabcde', 'abcd') == [3, 7]
        # multiple occurrences
        assert find_all_indexes('abra cadabra', 'abra') == [0, 8]
        # overlapping prefix
        assert find_all_indexes('abra cadabra', 'adab') == [6]

        self.assertEqual(find_all_indexes("", ""), [])
        self.assertEqual(find_all_indexes("bananns", "nns"), [4])
        self.assertEqual(find_all_indexes("20-02-01 202:41", "02"), [3, 10])
        self.assertEqual(find_all_indexes("[]][][[[][]]]", "][]"), [2, 8])
        self.assertEqual(find_all_indexes(
            "Python 3.7.6, pytest-5.1.2, py-1.8.0, pluggy-0.13.0", ", "),
            [12, 26, 36])
        self.assertEqual(find_all_indexes("rat a tat cat", "at"), [1, 7, 11])


if __name__ == '__main__':
    unittest.main()
