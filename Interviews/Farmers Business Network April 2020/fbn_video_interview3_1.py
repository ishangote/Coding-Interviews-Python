"""
# [ [ "abc", "123", "ghi" ], [], [], ["789", "456"], ["foo", "bar", "baz"]]
# [ "abc", "123", "ghi", "789", "456", "foo", "bar", "baz"]

next(input_itr)
[ "abc", "123", "ghi" ]

next(input)
next(inner_itr) -> 'abc'
next(inner_itr) -> '123'
next(inner_itr) -> 'ghi'
next(inner_itr) -> Raise StopIteration

iter((0, 1, 2))
"""

class FlatIterator:
	def __init__(self, input):
		self.input = input
		self.inner = iter(tuple())
	
	def __next__(self) -> str:
		while True:
            try:
                return next(self.inner)
            except StopIteration:
                self.inner = next(self.input)

flat_iterator = FlatIterator(input)

try:
	while True:
		x = next(flat_iterator)
		print(x)
except StopIteration:
	pass