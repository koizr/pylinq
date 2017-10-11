import typing


class Enumerable(object):
    """
    this class is lazy iterable like LINQ.
    """

    def __init__(self, values):
        self.values = (x for x in values)

    def __iter__(self):
        return self.values

    @classmethod
    def from_(cls, values):
        return cls(values)

    @classmethod
    def range(cls, *args):
        """
        組み込みの range() と同じ挙動で Enumerable を生成する
        """
        return cls(range(*args))

    @classmethod
    def empty(cls):
        """
        空の Enumerable を返す
        """
        return cls([])

    def where(self, predicate: typing.Callable):
        """
        受け取った関数を適用してフィルタリングした結果を返す
        """
        if predicate is None:
            predicate = lambda _: True

        return self.__class__((x for x in self.values if predicate(x)))
