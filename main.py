"""Gradebook command line interface."""
import sys

from gradebook.errors import GradebookError
<<<<<<< HEAD
from gradebook.storage import load
=======
from gradebook.roster import find_student
>>>>>>> 2b9c3dafa7c9959b888b98a704e5b993a8be571d

DATA_FILE = "roster.json"


def show_help(roster, args):
    print("commands:", ", ".join(sorted(COMMANDS)))


COMMANDS = {
    "help": show_help,
<<<<<<< HEAD
    "load": load,
=======
    "find": find_student
>>>>>>> 2b9c3dafa7c9959b888b98a704e5b993a8be571d
}


def main(argv):
    command = argv[1] if len(argv) > 1 else "help"
    roster = {}
    try:
        COMMANDS[command](roster, argv[2:])
    except KeyError:
        print(f"unknown command: {command}", file=sys.stderr)
        return 1
    except GradebookError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))