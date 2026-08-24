# NOTES.md gradebook-TeamETC

Generalized notes

---

## Stage 1

**B's rejection message:**
```
! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/...'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref.
```
**What `(fetch first)` means:** `(fetch first)` is git telling you to pull the missing commits down before trying again, rather than silently overwriting or discarding them.

**Conflict markers B saw in README.md:**
```
## Team
<<<<<<< HEAD
- B
=======
- A
>>>>>>> <A's commit hash>
```
*(representative)*

The `HEAD` side (above `=======`) is whatever's on the puller's own branch after the pull. The side after `=======`, labeled with the incoming commit's hash, is A's work, since A's commit is what's being merged in.

**Why git refused the push instead of accepting it:** Git only allows a push to fast-forward

---

## Stage 2

**A's merge was a fast-forward.** Actual terminal output:
```
$ git merge feature/roster
Updating 151c050..2b9c3da
Fast-forward
 gradebook/errors.py |  9 ++++++++-
 gradebook/roster.py | 17 ++++++++++++++++-
 main.py             |  2 ++
 3 files changed, 26 insertions(+), 2 deletions(-)
```
No merge commit was created because `main` hadn't moved since A branched off it

**B's conflicted errors.py (markers included):**
```python
<<<<<<< HEAD
class StorageError(GradebookError):
    """Raised an error when loading roster data."""
=======
class InvalidGrade(GradebookError):
    """Raised when a grade is invalid"""
>>>>>>> 2b9c3dafa7c9959b888b98a704e5b993a8be571d
```
Resolved by keeping both classes, removing all marker lines.

**B's conflict vs. C's:** *(representative)* C's conflict was larger, since by the time C merged, `main` already contained both A's and B's additions

**Why "Accept Current" / "Accept Incoming" would both be wrong:** Both options assume one side should fully overwrite the other.

---

## Stage 3

**Did git report a conflict?** No. `git merge` completed cleanly with no conflict markers, because C's change (inside `reports.py`, deleting `average`, adding `mean`) and A's change (inside `main.py`, adding `top` and importing `average`) never touched the same lines of text. Git's conflict detection is purely line-based.

**What happened running `python3 main.py`:**
```
ImportError: cannot import name 'average' from 'gradebook.reports'
```
This surfaced only at runtime, once Python actually tried to resolve the import after the merge had already completed successfully.

**Why git couldn't have caught it:** Git tracks text, not code logic.

**Two things that could have caught this before it reached main:**
1. Running the program immediately after merging, before treating the merge as "done".
2. **(non-git)** Direct communication with C mentioning the planned rename to the team before pushing it, so A could update the import at the same time.

---

## Stage 4

**Abort before resolving:**
```
git merge --abort
git status
```
Confirmed we were returned cleanly to the pre-merge state

**Abort after a merge is already committed:**
```
git merge --abort
```
Git refuses, since there's no merge in progress to abort once it's been committed.

**Stash:** *(representative)*
- Before stash (uncommitted edit present): `M storage.py`
- After `git stash`: `git status --short` shows nothing
- After switching branches and back: still clean
- After `git stash pop`: `M storage.py` reappears, edit restored

**Revert:** After merging a commit that broke the program, `git revert <hash>` created a new commit undoing its changes. `git log --oneline` afterward still showed the original bad commit alongside the new revert commit.

**Review (before the final merge):**
```
git diff --name-only main..<branch>
git diff main..<branch>
```
Three things checked by hand that neither command reveals:
1. Whether the code actually **runs**.
2. Whether the logic is **correct**.
3. Whether the change **duplicates or conflicts with something elsewhere in the codebase** that isn't visible in this diff.

---
