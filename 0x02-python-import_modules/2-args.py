#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1

    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(argc))
        for idx, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(idx, arg))
