from argparse import ArgumentParser
import os
from urllib.request import urlretrieve
from random import choice
from collections import defaultdict

#jjfjfj
def ask(prompt: str, valid: list[str] = None) -> str:
    word = input(prompt)
    if valid:
        while word not in valid:
            word = input(prompt)
    return word


def bullscows(guess: str, secret: str) -> (int, int):
    bulls, cows = 0, 0
    for a, b in zip(guess, secret):
        if a == b:
            bulls += 1
    g_dict = defaultdict(int)
    s_dict = defaultdict(int)
    for a in guess:
        g_dict[a] += 1
    for a in secret:
        s_dict[a] += 1
    for a, n in s_dict.items():
        cows += min(n, g_dict[a])
    cows -= bulls
    return bulls, cows


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret = choice(words)
    n = 0
    while True:
        guess = ask("Input word: ", words)
        n += 1
        bulls, cows = bullscows(guess, secret)
        inform("Bulls {}, Cows {}", bulls, cows)
        if guess == secret:
            break
    return n


if __name__ == "__main__":
    parser = ArgumentParser(prog='bulls-cows', description="Game 'bulls and cows'")
    parser.add_argument('dictionary', type=str, action='store', help='file of useful words')
    parser.add_argument('length', type=int, action='store', nargs='?', default=5,
                        help='length of used words')
    args = parser.parse_args()

    filename = args.dictionary
    if not os.path.exists(filename):
        filename, _ = urlretrieve(args.dictionary)

    word_arr = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if len(line) == args.length:
                word_arr.append(line)

    if len(word_arr) == 0:
        print('There are no words with needed length')
    else:
        num = gameplay(ask, inform, word_arr)
        print(f"Congratulations!")
        print(f"Number of attempts: {num}")
