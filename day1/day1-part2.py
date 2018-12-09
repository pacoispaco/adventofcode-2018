#!/usr/bin/env python3

"""This program is a solution to part 2 of https://adventofcode.com/2018/day/2"""

import sys
import argparse

DATA_FILE = "input.dat"

def solve_problem (verbose=False):
    """Solve the problem."""
    result = 0   # Current result
    results = [] # List of results
    found = False
    i = 1
    iteration = 1
    while not found:
        f = open (DATA_FILE)
        if verbose:
            print ("Iteration %d" % (iteration))
        for line in f:
            try:
                result += int (line)
                if result in results:
                    found = True
                    break
                else:
                    results.append (result)
            except ValueError:
                print ("Value error on line %d: '%s'" % (i, line.strip ()))
                sys.exit (1)
            i += 1
        f.close ()
        iteration += 1
    print (result)

def main():
    parser = argparse.ArgumentParser (description='This program solves part 2 of the Advent\
                                      of code problem https://adventofcode.com/2018/day/2')
    parser.add_argument ('-v', '--verbose', action='store_true', default=False,
                         help="print info about what's going on [False]")
    args = parser.parse_args ()
    solve_problem (args.verbose)
    sys.exit (0)

if __name__ == "__main__":
    main()
