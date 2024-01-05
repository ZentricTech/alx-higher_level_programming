#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1

    if argc == 0:
        print("0")
    else:
        total = sum(int(arg) for arg in argv[1:])
        print(total)
