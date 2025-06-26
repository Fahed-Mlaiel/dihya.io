import unittest


# Exemple de fonction de pagination à tester
def paginate(items, page, page_size):
    start = (page - 1) * page_size
    end = start + page_size
    return items[start:end]


class TestPagination(unittest.TestCase):
    def test_pagination_basic(self):
        items = list(range(1, 21))
        self.assertEqual(paginate(items, 1, 5), [1, 2, 3, 4, 5])
        self.assertEqual(paginate(items, 2, 5), [6, 7, 8, 9, 10])
        self.assertEqual(paginate(items, 4, 5), [16, 17, 18, 19, 20])

    def test_pagination_empty(self):
        items = []
        self.assertEqual(paginate(items, 1, 5), [])

    def test_pagination_out_of_range(self):
        items = list(range(1, 11))
        self.assertEqual(paginate(items, 3, 5), [])


if __name__ == "__main__":
    unittest.main()
