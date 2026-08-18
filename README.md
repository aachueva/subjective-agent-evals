# Subjective Agent Evals

A small evaluation framework for a deceptively hard AI-product question: **how do you measure whether an agent is getting better when quality is partly subjective?**

The example domain is playlist generation because it makes the problem easy to understand: a playlist can satisfy hard constraints and still feel repetitive, incoherent, or poorly matched to the user's intent.

The project is adapted from an AI evaluation prototype I built while exploring agent-quality workflows. This public version is independent and contains no interview prompt or proprietary company material.

## Why this project

Many AI demos stop after the agent produces a plausible answer. Production teams need a repeatable way to answer:

- Did the new prompt actually improve quality?
- Which user journeys regressed?
- Is the more expensive model worth it?
- Can PMs and engineers agree on what “good” means?
- Which metrics can be deterministic and which need model or human judgment?

## Evaluation dimensions

This example separates hard constraints from subjective quality:

| Dimension | Type | Example |
|---|---|---|
| Duration | Deterministic | Playlist must be <= 30 minutes |
| Track count | Deterministic | Requested number of tracks |
| Explicit constraints | Deterministic | Required / excluded genres or artists |
| Variety | Heuristic / model judge | Avoid repetitive artists and near-duplicate tracks |
| Mood fit | Model / human judge | Does the result match “calm morning run”? |
| Coherence | Model / human judge | Does the playlist feel intentional as a sequence? |
| Safety | Policy / deterministic | Excluded content is not returned |

## Evaluation flywheel

```text
Production traces / curated examples
              |
              v
         Evaluation dataset
              |
              v
      Prompt / model variants
              |
              v
      Deterministic + judged scores
              |
              v
     Compare failures and trade-offs
              |
              v
       Ship + monitor online
              |
              +------> new hard cases
```

The value is not a one-time benchmark. It is a repeatable operating system for improving AI-product quality.

## Four-week pilot pattern

**Week 1 — Instrument**  
Capture representative traces and identify the user journeys that matter.

**Week 2 — Curate**  
Create a small, high-quality dataset from production-like examples and known failure modes.

**Week 3 — Define quality**  
Agree on a compact scorecard: hard constraints, subjective dimensions, latency, and cost.

**Week 4 — Compare and operationalize**  
Run prompt/model experiments, inspect failures, select a candidate, and define online monitoring.

## Repository roadmap

- [x] Example dataset
- [x] Deterministic scoring utilities
- [x] Variant-comparison script
- [ ] LLM-as-judge adapter
- [ ] Human-review rubric
- [ ] Trace ingestion example
- [ ] Online monitoring example

## What this demonstrates

This project is less about playlist generation than about **evaluation design and deployment judgment**: turning fuzzy product expectations into measurable criteria, building a dataset around important journeys, comparing changes consistently, and using failures to drive the next iteration.

— Anastasia Chueva
