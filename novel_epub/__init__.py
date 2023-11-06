import argparse

from .novel import *

def get_args():
    parser = argparse.ArgumentParser(description="Convert novel chapters to an EPUB file.")
    parser.add_argument('-url', dest="url", type=str, help="URL of the novel source", required=True)
    parser.add_argument('-sc', '--start-chapter', dest="start_chapter",  type=int, 
                        help="Start chapter number. Value has to be greater or equal to 1", default=1)
    parser.add_argument('-ec', '--end-chapter', dest="end_chapter", type=int, 
                        help="End chapter number", required=True)
    parser.add_argument('-title', dest="title", type=str, 
                        help="Desired novel's title. Default title is the one gotten from the URL")
    parser.add_argument('-author', dest="author", type=str, 
                        help="Desired novel's author's name. Default author's name is the one gotten from the URL")

    return parser.parse_args()

def main():
    args = get_args()

    
    novel = Novel(args.url, title=args.title)
    print(novel)


if __name__ == '__main__':
    main()
