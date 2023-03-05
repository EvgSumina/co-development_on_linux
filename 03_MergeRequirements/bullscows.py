from argparse import ArgumentParser


if __name__ == "__main__":
    parser = ArgumentParser(prog='bulls-cows', description="Game 'bulls and cows'")
    parser.add_argument('dictionary', type=str, action='store', help='file of useful words')
    parser.add_argument('length', type=int, action='store', nargs='?', default=5,
                        help='length of used words')
    args = parser.parse_args()
