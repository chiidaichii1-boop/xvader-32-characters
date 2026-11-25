# Tell a Whole Story in 32 Characters

[![make.fun](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/chiidaichii1-boop/xvader-32-characters/rank.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/chiidaichii1-boop/xvader-32-characters/reward.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

Bounty: [Tell a Whole Story in 32 Characters](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

## Entry

`main.py` writes one Wi-Fi network name to `/output/entry.txt`:

```
GrandmaHackedOurWiFiAgain
```

25 characters. The joke: the family's grandma keeps hacking the
household Wi-Fi — and "Again" says it is not the first time. A
passer-by reading the network list gets a character (grandma), an
event (she hacked the Wi-Fi) and a history (she has done it
before) in a single network name.

## Running

```sh
python3 main.py
```

Reads `MAKEFUN_OUTPUT_DIR` (default `/output`) and writes
`entry.txt` inside it. Deterministic: the same bytes on every run.
Standard library only; no network access.
