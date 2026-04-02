"""Visualization helpers for the experimental run summary."""

from __future__ import annotations

import os

import matplotlib.pyplot as plt


def plot_agent_influence(agent_weights: dict[str, float], out_path: str) -> None:
    """Bar chart of how often each department 'won' the coordinator merge."""
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    names = list(agent_weights.keys())
    values = [agent_weights[k] for k in names]
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.bar(names, values, color="#2c3e50", edgecolor="#111111", linewidth=0.6)
    ax.set_title("Coordinator merge outcomes by department (experimental PoC)")
    ax.set_ylabel("Share of winning proposals")
    ax.set_ylim(0, max(values + [0.01]) * 1.15)
    for i, v in enumerate(values):
        ax.text(i, v + 0.01, f"{v:.2f}", ha="center", va="bottom", fontsize=9)
    fig.tight_layout()
    fig.savefig(out_path, dpi=140)
    plt.close(fig)


def plot_slippage_timeline(slippage_per_step: list[int], out_path: str) -> None:
    """Line plot of cumulative schedule slip across staged incidents."""
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    cumulative: list[int] = []
    total = 0
    for m in slippage_per_step:
        total += m
        cumulative.append(total)
    fig, ax = plt.subplots(figsize=(8, 4.2))
    steps = list(range(1, len(cumulative) + 1))
    ax.plot(steps, cumulative, marker="o", color="#c0392b", linewidth=1.8)
    ax.fill_between(steps, cumulative, alpha=0.12, color="#c0392b")
    ax.set_title("Cumulative minutes shifted (synthetic day)")
    ax.set_xlabel("Incident step")
    ax.set_ylabel("Cumulative minutes")
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(out_path, dpi=140)
    plt.close(fig)
