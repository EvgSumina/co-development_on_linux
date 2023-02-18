import argparse
from cowsay import cowsay, list_cows


OPTIONALS = set("bdgpstwy")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='cowsay app')
    parser.add_argument("-e", type=str, default='oo', help="eye_string")
    parser.add_argument("-f", type=str, default='default', help="file with cow")
    parser.add_argument("-l", action="store_true", help='calls the cowlist')
    parser.add_argument("-n", action="store_true", help='not to wrap the message')
    parser.add_argument("-T", type=str, default='  ', help='specify a tongue')
    parser.add_argument("-W", type=int, default=40, help='the width of the text bubble')
    for option in OPTIONALS:
        parser.add_argument(f"-{option}", action="store_true")
    args = parser.parse_args()
