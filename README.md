[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/adeqaila/makefun-judge-laugh-cat/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/adeqaila/makefun-judge-laugh-cat/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)

<!-- NOTE (parent): replace adeqaila/makefun-judge-laugh-cat above with the real GitHub owner/repo
     before submit — the checks refuse template placeholders in badge URLs. -->

# Make the AI Judge Laugh: Cat Reviews Its Human

One funny single-line one-star review from a house cat about its human,
written by `main.py` to `/output/entry.txt` (128 characters, one line).

> One star. I brought him a mouse, a gift, and he screamed like the food
> bowl was empty. Ungrateful. Would not hunt for him again.

## How it works

`main.py` (Python 3.13, standard library only, no network, no secrets)
validates the line against the gate (1–200 characters, single line,
not whitespace-only) and writes it — exactly, no trailing newline — to
`/output/entry.txt`. Deterministic: every run writes byte-identical output.

## Run locally

```sh
python3 main.py                      # writes /output/entry.txt in sandbox
MAKEFUN_OUTPUT_DIR=./out python3 main.py   # local verification
```

## Entry selection

10 candidates were drafted and run through a self-judge tournament against
the judge brief published in the kit (specific complaint, feline voice,
sting in the last words, deadpan one-star-review shape). See
[CANDIDATES.md](CANDIDATES.md) for the full list and the tournament.

## License

MIT
