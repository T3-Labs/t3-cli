import json

import click

from pathlib import Path
import os
from getpass import getpass

from t3_cli.metrics.metric import calculate_intersection_over_union, precision_recall_metrics


@click.group()
def cli():
    pass


@cli.command("evaluate")
@click.option('--evaluate', required=False, help="Evaluate precision Deep Learning Model")
def evaluate(evaluate):
    print("Hello World")


@cli.command("iou")
@click.option('--iou', required=False, help="Calculate Intersection Over Union")
def iou(iou):
    iou = precision_recall_metrics(true_positive=1., false_positive=1., false_negative_positive=1., save=True)

    print(iou)


if __name__ == "__main__":
    cli()
