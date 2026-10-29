# How this repository was made (Vanuatu)

This file is written by the build on 2026-10-29, the day the source data was retrieved. Everything below is enough to rebuild this repository hash for hash.

## Sources

| Source | Address | Retrieved | Requests | Licence |
| --- | --- | --- | ---: | --- |
| PacLII Vanuatu Consolidated Legislation 2006, via Internet Archive | <http://www.paclii.org/vu/legis/consol_act/> | 2026-10-29 | 1 | PacLII free access; legislation text is public law |

Every response is cached by the sha256 of its URL, and the table above lists every source with its retrieval date. Lexifina keeps its fetch scripts privately; `tools/parse.py` reads only the cache and writes `corpus.json`, so the same cache always gives the same corpus.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of the Republic of Vanuatu | 1 | 2006-08-31 to 2006-08-31 |

The build made 1 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-29.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 3 laws in the record.
- 1 tags.

## Dates

Each commit is dated at noon (Pacific/Efate) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Interpretation Act [Cap 132]: an Act commences on publication in the Gazette unless it provides otherwise (to verify) http://www.paclii.org/vu/legis/consol_act/ia138/

## Commands, in order

```sh
# fill the cache from the sources listed above (network; Lexifina's fetch scripts are kept privately)
python -X utf8 tools/parse.py                  # cache -> corpus.json (no network)
python -X utf8 tools/build.py <folder> --repo <empty folder> --docs-date 2026-10-29
python -X utf8 tools/check_repo.py <repo> --corpus <folder>/corpus.json --write
python -X utf8 tools/build.py <folder> --repo <another empty folder> --docs-date 2026-10-29 --compare <repo>
```

In the main Lexifina repository these files live as follows:
- `fetch.py`, `parse.py` and `repo/`: in `scripts/vanuatu-law/`.
- `build.py`, `check_repo.py` (`check.py` there) and `on.py`: in `scripts/gitlaw_common/`, with the corpus format in `SCHEMA.md`.

## Exact inputs

- `corpus.json` sha256 `35673ed2e180cde61b5d37ed3b11b943a1a3189dce39174671f254bc3fb656f5` (63266 bytes)
- Script blob hashes (`git hash-object`):

| Script | Blob |
| --- | --- |
| build.py | `5d40c3d38194a1920e89e6b0fc342f0171d10b0d` |
| check.py | `cd346c7ff9996d450240e3bab52bcae03b2bc865` |
| on.py | `644a6c0857fbcc72562032b58d57aa113fee0641` |
| fetch.py | `0c4e62ee702ef4f063a68daf7d2e1fc76b29efe1` |
| parse.py | `3a7b1c883d83f43e1717c274f4b4e74220486b05` |

- Tools:
  - Python 3.14.0
  - git version 2.52.0.windows.1
  - curl 8.21.0 (Windows) libcurl/8.21.0 Schannel zlib/1.3.2 WinIDN WinLDAP

## Checks

1 versions of 1 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

Not yet run for this build.

These results are from the check run on the build before this one, from the same corpus.

## Decisions made by hand

- English text built; French and Bislama official texts exist.
- Phase 1 stub: the Constitution as in the Consolidated Edition 2006 is the oldest version available, credited to the publisher; it is dated 2006-08-31, the earliest Internet Archive capture of that edition on PacLII, because the edition carries no day of its own.
- Not yet applied: Constitution (Fifth Amendment) Act 2006 (Act 24 of 2006), Constitution (Sixth)(Amendment) Act 2013 (Act 27 of 2013), and the Constitution (Eighth)(Amendment) Act No. 21 of 2023 approved at the 29 May 2024 referendum.

## What AI did and did not do

The fetch, parse and check scripts were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above, through code that anyone can rerun.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none: parsing is deterministic code; no model wrote or edited legal text.
