from argparse import ArgumentParser
import os
from urllib.request import urlretrieve


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
