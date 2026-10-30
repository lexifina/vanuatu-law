# Vanuatu: law history in git

The law of Vanuatu as a git repository: one file per provision, and the law that made each change as the commit's author. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `vu/`. The language is English, one of Vanuatu's three official languages with Bislama and French.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution of the Republic of Vanuatu | 1 | The Consolidated Edition 2020, the oldest version available here |

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What does Article 5 say? | `git show main:constitution/art-005.md` |
| Every commit in the record | `git log --reverse --format="%ad %an" --date=short main` |

## Dates

- The one version is dated **29 April 2020**, the day the Consolidated Edition 2020 says its order commenced. It is "oldest version available", credited to the publisher, the Parliament of Vanuatu. It is the Constitution as in force on that day, not as enacted on 30 July 1980.

## How it is checked

- The text of every article and both schedules is read back from git and compared with `corpus.json` (`REPRODUCE.md`).
- The 2020 PDF carries a text layer; no OCR was used.

## What it does not show

- **History.** The Constitution has been amended by Acts 10 of 1980, 15 of 1981, 20 of 1983, 24 of 2006 and 27 of 2013, all folded into the 2020 text. Their dates are not replayed here.
- **The 2023 amendment.** The Constitution (Eighth) (Amendment) Act No. 21 of 2023 (Articles 17A and 17B), approved by referendum on 29 May 2024, is not in the 2020 text and is not here.
- **Other laws.** Only the Constitution is in this first build.

The legal text is from the Parliament of the Republic of Vanuatu; see `LICENSE`.
