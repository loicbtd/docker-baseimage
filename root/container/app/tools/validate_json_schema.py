import json
import jsonschema
import sys


def main():
    if len(sys.argv) != 3:
        sys.exit("Error: " + sys.argv[0] + ": invalid argv length")
    try:
        with open(sys.argv[1]):
            pass
    except IOError:
        sys.exit("Error: " + sys.argv[0] + ": json data file not found")
    try:
        with open(sys.argv[2]):
            pass
    except IOError:
        sys.exit("Error: " + sys.argv[0] + ": json schema file not found")
    with open(sys.argv[1]) as file:
        json_data = json.load(file)
    with open(sys.argv[2]) as file:
        json_schema = json.load(file)
    try:
        jsonschema.validate(json_data, json_schema)
    except jsonschema.exceptions.ValidationError:
        sys.exit("Error: " + sys.argv[0] + ": json does not match schema")
    sys.exit(0)


main()
