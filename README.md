# ShootMesh-AI

**Experimental multi-agent coordination for a synthetic film and television production day**

ShootMesh-AI is a small, transparent Python experiment that models how specialized “department” agents can propose competing actions when a staged shooting day hits unexpected incidents, how a coordinator merges those proposals with an explicit priority policy, and how a ledger records the resulting sequence of decisions. The repository is a personal proof of concept: it is not on-set software, not production guidance, and not affiliated with any studio or employer.

![Title diagram](https://raw.githubusercontent.com/aniket-work/ShootMesh-AI/3aaadfb4cf706bf2729c7105deae15d64faf9da2/images/title_diagram.png)

## Why this exists

On-location production days combine tight timing, overlapping crafts, and unpredictable constraints. In my experiments, I wanted a reproducible sandbox where I could think about coordination patterns that resemble how a production office reasons about trade-offs without relying on opaque monoliths. The design goal was to keep the merge policy inspectable, log every decision, and emit both terminal-friendly summaries and simple charts so a run can be reviewed quickly.

## What you get

1. **Department-style agents** that emit ranked proposals for weather, talent, gear, location, and permit-style incidents.
2. **A deterministic coordinator** that selects a winning proposal using a fixed priority order: safety first, then schedule, then creative considerations, then cost.
3. **A decision ledger** that stores each step with the department credited and the minutes shifted by the chosen action.
4. **Charts** written to `output/` that summarize how often each department’s proposal won the merge and how cumulative schedule slip evolves across the synthetic day.

![Architecture](https://raw.githubusercontent.com/aniket-work/ShootMesh-AI/3aaadfb4cf706bf2729c7105deae15d64faf9da2/images/architecture_diagram.png)

## Architecture at a glance

The pipeline is intentionally linear: incidents arrive from a small scenario list, every agent proposes, the coordinator merges, and the ledger grows. The diagram below mirrors the runtime shape used in `main.py`.

![Sequence](https://raw.githubusercontent.com/aniket-work/ShootMesh-AI/3aaadfb4cf706bf2729c7105deae15d64faf9da2/images/sequence_diagram.png)

## Workflow

![Flow](https://raw.githubusercontent.com/aniket-work/ShootMesh-AI/3aaadfb4cf706bf2729c7105deae15d64faf9da2/images/flow_diagram.png)

## Quick start

Requirements: Python 3.10 or newer.

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Artifacts land in `output/`:

- `agent_influence.png` — share of merge wins by department label.
- `slippage_timeline.png` — cumulative minutes shifted after each staged incident.

## Repository layout

```text
ShootMesh-AI/
├── LICENSE
├── README.md
├── main.py
├── requirements.txt
├── images/
│   ├── title_diagram.png
│   ├── architecture_diagram.png
│   ├── sequence_diagram.png
│   ├── flow_diagram.png
│   └── title-animation.gif
└── src/shootmesh/
    ├── agents.py
    ├── coordinator.py
    ├── engine.py
    ├── plots.py
    ├── reporting.py
    ├── scenario.py
    └── types.py
```

## Design notes

### Priority policy

The coordinator does not attempt to learn weights from data in this repository. Instead, it exposes a explicit ordering (`safety`, `schedule`, `creative`, `cost`) and breaks ties with confidence scores and minute shifts. From my perspective, that choice made regressions easier to reason about while I iterated on the PoC.

### Ledger

Each ledger row ties an incident description to the department whose proposal won. In a richer system, I would attach IDs for scenes, setups, and cast members; here the focus stays on the coordination skeleton.

### Extensibility

The agents return Python objects, not strings destined for an LLM. That kept the demo lightweight. A natural extension—outside the scope of this repo—is to generate proposals from retrieval over call sheets or to score proposals with a small model; the merge layer would stay the same.

## Animated overview

The animated GIF below is a stylized walkthrough: a terminal-style segment shows the ASCII summary table, then crossfades into a bar chart of merge outcomes.

![Title animation](https://raw.githubusercontent.com/aniket-work/ShootMesh-AI/3aaadfb4cf706bf2729c7105deae15d64faf9da2/images/title-animation.gif)

## Ethics and limits

This code simulates a day with synthetic incidents. It does not process personal data about performers or crew, and it should not be mistaken for labor-relations, safety-compliance, or union-rule tooling. Any real deployment would need domain experts, on-set authority structures, and jurisdiction-specific rules.

## License

MIT — see `LICENSE`.

## Disclaimer

The views and opinions expressed in documentation here are solely my own and do not represent the views, positions, or opinions of my employer or any organization I am affiliated with. This repository is an experimental artifact and may be incomplete or incorrect.
