import json
import sys
import deepdiff


def main():
    if len(sys.argv) != 3:
        sys.exit("Error: " + sys.argv[0] + ": invalid argv length")
    try:
        with open(sys.argv[1]):
            pass
    except IOError:
        sys.exit("Error: " + sys.argv[0] + ": json file 1 not found")
    try:
        with open(sys.argv[2]):
            pass
    except IOError:
        sys.exit("Error: " + sys.argv[0] + ": json file 2 not found")
    with open(sys.argv[1]) as file:
        json_file_1 = json.load(file)
    with open(sys.argv[2]) as file:
        json_file_2 = json.load(file)
    if not deepdiff.DeepDiff(json_file_1, json_file_2, ignore_order=True):
        sys.exit("Error: " + sys.argv[0] + ": json have the same data")
    else:
        sys.exit(0)


main()
