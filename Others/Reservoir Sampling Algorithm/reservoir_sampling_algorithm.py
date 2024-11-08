import random


class NumsStream:
    def __init__(self):
        self.stream = []

    def add_num(self, num):
        self.stream.append(num)

    def pick(self):
        reservoir = None

        for idx, num in enumerate(self.stream, start=1):
            if random.randint(0, idx - 1) == 0:
                reservoir = num

        return reservoir


def main():
    nums_stream = NumsStream()
    nums_stream.add_num(1)
    nums_stream.add_num(2)
    nums_stream.add_num(3)
    nums_stream.add_num(4)
    nums_stream.add_num(5)

    print("Random Num: ")
    print(nums_stream.pick())


if __name__ == "__main__":
    main()
