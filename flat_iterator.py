class FlatIterator():

    def __init__(self, lst):
        self.lst = lst
        self.len_lst = len(self.lst)
        self.cursor = -1

    def __iter__(self):
        self.cursor += 1
        self.next_cursor = 0
        return self

    def __next__(self):
        if self.next_cursor == len(self.lst[self.cursor]):
            iter(self)
        if self.cursor == self.len_lst:
            raise StopIteration
        value = self.lst[self.cursor][self.next_cursor]
        self.next_cursor += 1
        return value


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
    print("ok")


#
# list_of_lists_1 = [
#     ['a', 'b', 'c'],
#     ['d', 'e', 'f', 'h', False],
#     [1, 2, None]
# ]
#
# all = []
# for i in list_of_lists_1:
#     all.extend(i)
# print(all)
