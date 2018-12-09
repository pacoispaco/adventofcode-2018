#!/usr/bin/env python3

"""This program is a solution to https://adventofcode.com/2018/day/3"""

import sys
import argparse
import re

DATA_FILE = "input.dat"

def solve_problem (verbose=False):
    """Solve the problem."""
    result = 0
    strings_with_same_two_letters = 0
    strings_with_same_three_letters = 0
    i = 1
    f = open (DATA_FILE)
    for line in f:
        len_line = len (line)
        chars = set (line)
        len_set = len (chars)
        if len_set == (len_line - 1):
            strings_with_same_two_letters += 1
            if verbose:
                print ("Line %d \"%s\" has exactly one letter that appears twice." % (i, line))
        elif len_set <= (len_line - 1):
            two_found = False
            three_found = False
            for c in chars:
                if not two_found and line.count (c) == 2:
                    strings_with_same_two_letters += 1
                    two_found = True
                    if verbose:
                        print ("In line %d \"%s\" the letter '%s' appears twice." % (i, line, c))
                elif not three_found and line.count (c) ==3:
                    strings_with_same_three_letters += 1
                    three_found = True
                    if verbose:
                        print ("In line %d '%s' the letter '%s' appears thrice." % (i, line, c))
                if two_found and three_found:
                    break
        i += 1
    f.close ()
    if verbose:
        print ("No of strings with letter that appears exactly twice: %s" % (strings_with_same_two_letters))
        print ("No of strings with letter that appears exactly thrice: %s" % (strings_with_same_three_letters))
    result = strings_with_same_two_letters * strings_with_same_three_letters
    print (result)

def main():
    parser = argparse.ArgumentParser (description='This program solves the Advent\
                                      of code problem https://adventofcode.com/2018/day/2')
    parser.add_argument ('-v', '--verbose', action='store_true', default=False,
                         help="print info about what's going on [False]")
    args = parser.parse_args ()
    solve_problem (args.verbose)
    sys.exit (0)

if __name__ == "__main__":
    main()
