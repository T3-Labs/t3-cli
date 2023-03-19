from rich.console import Console
from rich.table import Table

console = Console()


def calculate_intersection_over_union(box1, box2):
    left = max(box1[0], box2[0])
    right = min(box1[0] + box1[2], box2[0] + box2[2])

    upper = max(box1[1], box2[1])
    bottom = min(box1[1] + box1[3], box2[1] + box2[3])

    inter_w = right - left
    if inter_w < 0:
        inter_w = 0
    inter_h = bottom - upper
    if inter_h < 0:
        inter_h = 0

    inter_square = inter_w * inter_h
    union_square = (box1[2] * box1[3]) + (box2[2] * box2[3]) - inter_square

    return inter_square / union_square


def precision_recall_metrics(true_positive: float, false_positive: float, false_negative_positive: float,
                             save: bool = False):
    precision: float = true_positive / (true_positive + false_positive)
    recall: float = true_positive / (true_positive + false_negative_positive)

    if precision + recall > 0:
        f1score = 2 * ((precision * recall) / (precision + recall))
    else:
        f1score = 0

    output = "TP: {} FP: {} FN: {}\nprecision: {}\nrecall: {}\nf1score: {}".format(true_positive, false_positive,
                                                                                   false_negative_positive, precision,
                                                                                   recall,
                                                                                   f1score)

    table = Table(title="Precision Recall F1Score")

    table.add_column("True Positive", justify="right", style="cyan", no_wrap=True)
    table.add_column("False Positive", style="magenta")
    table.add_column("False Negative", justify="right", style="green")
    table.add_column("Precision", justify="right", style="blue")
    table.add_column("Recall", justify="right", style="red")
    table.add_column("F1 Score", justify="right", style="yellow")

    table.add_row(str(true_positive), str(false_positive), str(false_negative_positive), str(precision), str(recall),
                  str(f1score))

    console.print(table)

    if save is True:
        with open("metrics.txt", 'w+') as file:
            file.write(output)

    return precision, recall
