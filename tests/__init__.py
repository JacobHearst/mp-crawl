from mp_scraper.items import Route

def compare_item_iter(test_case, first, second):
    """Compare two iterables that contain scrapy items

    Arguments:
        test_case {unittest.TestCase} -- The context of the test
        first {Iterable[Item]} -- First iterable to compare
        second {Iterable[Item]} -- Second iterable to compare
    """
    for index, item in enumerate(first):
        with test_case.subTest(expected=item, actual=second[index]):
            test_case.assertDictEqual(dict(item), dict(second[index]))

    test_case.assertEqual(len(first), len(second))
