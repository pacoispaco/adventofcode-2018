#!/usr/bin/env python3

"""This program is a solution to part 1 of https://adventofcode.com/2018/day/1"""

import sys
import argparse

DATA_FILE = "input.dat"

def solve_problem (verbose=False):
    """Solve the problem."""
    result = 0
    f = open (DATA_FILE)
    i = 1
    for line in f:
        try:
            result += int (line)
        except ValueError:
            print ("Value error on line %d: '%s'" % (i, line.strip ()))
            sys.exit (1)
        i += 1
    f.close ()
    print (result)

def main():
    parser = argparse.ArgumentParser (description='This program solves part 1 of the Advent\
                                      of code problem https://adventofcode.com/2018/day/1')
    parser.add_argument ('-v', '--verbose', action='store_true', default=False,
                         help="print info about what's going on [False]")
    args = parser.parse_args ()
    solve_problem (args.verbose)
    sys.exit (0)

if __name__ == "__main__":
    main()
