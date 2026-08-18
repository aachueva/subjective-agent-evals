# Evaluation Rubric

## Hard constraints

Use deterministic checks whenever the requirement has an objective answer. Examples:

- exact or bounded track count
- maximum duration
- excluded artists or genres
- minimum representation by genre
- instrumental-only requirement when reliable metadata is available

Hard constraints should not be delegated to a model judge if ordinary code can verify them.

## Subjective dimensions

### Mood fit

**5:** Strong match to the requested mood throughout.  
**3:** Generally appropriate with noticeable mismatches.  
**1:** Mostly inconsistent with the requested mood.

### Coherence

**5:** The sequence feels intentional and transitions are sensible.  
**3:** Individual tracks fit but the sequence is uneven.  
**1:** The result feels like an unrelated collection of tracks.

### Variety

**5:** Good diversity without sacrificing coherence.  
**3:** Some repetition or narrowness.  
**1:** Highly repetitive.

## Judge design

A production evaluator should:

1. use the same rubric across variants
2. hide model/prompt identity when possible
3. calibrate model-judge scores against human examples
4. inspect disagreements rather than trusting aggregate scores alone
5. preserve examples of important failures in the dataset

## Decision rule

Do not collapse every metric into one number too early. A candidate can improve average subjective quality while violating a launch-blocking hard constraint. Compare the scorecard, failure examples, latency, and cost together.
