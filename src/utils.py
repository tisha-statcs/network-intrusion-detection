"""
Shared utilities used across the Task1-4 notebooks.

Most of the analysis in this project is intentionally kept inline in the
notebooks (dataset exploration, model training, plotting), since each task
builds on state defined earlier in the same notebook. This module holds the
small pieces of logic that are generic enough to be reused as-is.
"""

import os
import random

import matplotlib.pyplot as plt
import numpy as np
import torch


def set_seed(seed: int) -> None:
    """Seed python, numpy and torch (CPU + CUDA) for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)


def get_device() -> torch.device:
    """Return the CUDA device if available, otherwise CPU."""
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def save_figure(filename: str, output_dir: str, dpi: int = 300, bbox_inches: str = "tight") -> str:
    """
    Save the current matplotlib figure under `output_dir`.

    Args:
        filename: target filename, e.g. 'task1_class_distribution.png'.
        output_dir: directory the figure is written to (created if missing).
        dpi: resolution to save at.
        bbox_inches: passed through to plt.savefig.

    Returns:
        Full path the figure was saved to.
    """
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, filename)
    plt.savefig(path, dpi=dpi, bbox_inches=bbox_inches)
    return path


def autopct_format(values):
    """Pie-chart autopct formatter showing both percentage and raw count."""

    def my_format(pct):
        total = len(values)
        val = int(round(pct * total / 100.0))
        return f"{pct:.1f}%\n({val:d})"

    return my_format
