"""Statistics and formatted output. Owner: C."""
from gradebook.errors import ReportError

def mean(scores):
    if not scores:
        raise ReportError("No scores provided")
    return sum(scores) / len(scores)

def summary(roster):
    if not roster:
        raise ReportError("ROSTER SUMMARY\n--------------\nNo records available")
    lines = ["==============================",
             "       STUDENT ROSTER        ",
             "=============================="]

    for index, record in enumerate(roster, start=1):
        if not isinstance(record, dict):
            lines.append(f"{index}. [Invalid Record]")
            continue

        name = record.get("name", "Unknown Student")
        scores = record.get("scores")

        if isinstance(scores, list) and len(scores) > 0:
            formatted_scores = ", ".join(str(s) for s in scores)
        elif isinstance(scores, list) and len(scores) == 0:
            formatted_scores = "No scores recorded"
        else:
            formatted_scores = "N/A"

        lines.append(f"{index}. Name: {name}\n   Scores: {formatted_scores}")

    lines.append("==============================")
    return "\n".join(lines)

def run_summary(roster_dict, args):
    report_list = []
    for name, scores in roster_dict.items():
        report_list.append({"name": name, "scores": scores})

    print(summary(report_list))

# checking with if is correct here whereas catching would not be because we
# are attempting to filter out formatting issues as opposed to actually
# catching logic or syntax error in the code