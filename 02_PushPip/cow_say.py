import argparse
from cowsay import cowsay, list_cows


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='cowsay app')
    parser.add_argument("-e", type=str, default='oo', help="eye_string")
    parser.add_argument("-f", type=str, default='default', help="file with cow")
    parser.add_argument("-l", action="store_true", help="")
    parser.add_argument("-n", action="store_true", help="")
    parser.add_argument("-T", type=str, default='  ', help="tongue_string")
    parser.add_argument("-W", type=int, default=40, help="column")
    args = parser.parse_args()
