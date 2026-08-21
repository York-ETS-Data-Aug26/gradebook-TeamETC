"""Gradebook command line interface."""
import sys

from gradebook import reports
from gradebook.errors import GradebookError

from gradebook.storage import load

from gradebook.roster import find_student
from gradebook.reports import average


DATA_FILE = "roster.json"


def show_help(roster, args):
    print("commands:", ", ".join(sorted(COMMANDS)))

def top(roster, args):
    if not roster:
        print("no students in roster")
        return
    best_student = max(roster, key=lambda name: average(roster[name]))
    print(best_student, average(roster[best_student]))


COMMANDS = {
    "help": show_help,
    "load": load,
    "find": find_student,
    "average": reports.mean,
    "top": top
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