import argparse

from .scrap_data import *

def get_args():
    parser = argparse.ArgumentParser(description='Convert novel chapters to an EPUB file.')
    parser.add_argument('-url', type=str, help='URL of the novel source', required=True)
    parser.add_argument('-sc', '--start-chapter', type=int, help='Start chapter number', default=1)
    parser.add_argument('--end-chapter', type=int, help='End chapter number', required=True)
    return parser.parse_args()

def main():
    args = get_args()

    print(f'Converting novel from {args.url}')
    scrap_book_data(args.url)


if __name__ == '__main__':
    main()
