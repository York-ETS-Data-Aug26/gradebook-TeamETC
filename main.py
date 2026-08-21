"""Gradebook command line interface."""
import os
import sys
from gradebook.reports import mean, summary
from gradebook.errors import GradebookError
from gradebook.storage import load
from gradebook.roster import find_student

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "roster.json")

def show_help(roster_dict, args):
    print("commands:", ", ".join(sorted(COMMANDS)))

def top(roster_dict, args):
    if not roster_dict:
        print("no students in roster")
        return
    best_student = max(roster_dict, key=lambda name: mean(roster_dict[name]))
    print(best_student, mean(roster_dict[best_student]))

def run_summary(roster_dict, args):
    report_list = []
    for name, scores in roster_dict.items():
        report_list.append({"name": name, "scores": scores})

    print(summary(report_list))

def run_find(roster_dict, args):
    if not args:
        print("no students in roster")
        return

    student_name = args[0]

    try:
        scores = find_student(roster_dict, student_name)
        print(f"Student: {student_name} | Scores: {scores}")
    except GradebookError as e:
        print(f"error: {e}", file=sys.stderr)


def run_average(roster_dict, args):
    if not args:
        print("error: please provide a student name", file=sys.stderr)
        return

    student_name = args[0]
    try:
        # Step 1: Use Owner A's function to get the student's score list
        scores = find_student(roster_dict, student_name)
        # Step 2: Pass that list into Owner C's mean calculation function
        student_avg = mean(scores)
        print(f"{student_name}'s Average Grade: {student_avg:.2f}")
    except GradebookError as e:
        print(f"error: {e}", file=sys.stderr)

COMMANDS = {
    "help": show_help,
    "find": run_find,
    "average": run_average,
    "top": top,
    "summary": run_summary
}


def main(argv):
    command = argv[1] if len(argv) > 1 else "help"

    try:
        roster_dict = load(DATA_FILE)
    except GradebookError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    try:
        if command in COMMANDS:
            COMMANDS[command](roster_dict, argv[2:])
        else:
            print(f"uknown command: {command}", file=sys.stderr)
            return 1
    except GradebookError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))