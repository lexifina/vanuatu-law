# How this repository was made (Vanuatu)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Parliament of Vanuatu: Constitution (Consolidated Edition 2020) | <https://parliament.gov.vu/images/constitution.pdf> | 2026-10-30 | Official text of the Constitution published by the Parliament; site states no reuse terms. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of the Republic of Vanuatu | 1 | 2020-04-29 to 2020-04-29 |

The build made 1 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 3 laws in the record.
- 1 tags.

## Dates

Each commit is dated at noon (Pacific/Efate) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Interpretation Act [Cap 132]: an Act commences on publication in the Gazette unless it provides otherwise (to verify) http://www.paclii.org/vu/legis/consol_act/ia138/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `69b68adc35169b86b4031ed606a331286d2663335ab9009b0c1efe7c2f1c98c1` (66436 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- English text built; French and Bislama official texts exist.
- Phase 1 stub: the Constitution as in the Consolidated Edition 2006 is the oldest version available, credited to the publisher; it is dated 2006-08-31, the earliest Internet Archive capture of that edition on PacLII, because the edition carries no day of its own.
- Not yet applied: Constitution (Fifth Amendment) Act 2006 (Act 24 of 2006), Constitution (Sixth)(Amendment) Act 2013 (Act 27 of 2013), and the Constitution (Eighth)(Amendment) Act No. 21 of 2023 approved at the 29 May 2024 referendum.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none: parsing is deterministic code; no model wrote or edited legal text.
