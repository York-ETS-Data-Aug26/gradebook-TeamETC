"""Gradebook command line interface."""
import sys

from gradebook.reports import mean, run_summary
from gradebook.errors import GradebookError

from gradebook.storage import load

from gradebook.roster import find_student


DATA_FILE = "roster.json"


def show_help(roster, args):
    print("commands:", ", ".join(sorted(COMMANDS)))

def top(roster, args):
    if not roster:
        print("no students in roster")
        return
    best_student = max(roster, key=lambda name: mean(roster[name]))
    print(best_student, mean(roster[best_student]))


COMMANDS = {
    "help": show_help,
    "load": load,
    "find": find_student,
    "average": mean,
    "top": top,
    "summary": run_summary
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