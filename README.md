# CampusFlow — Campus IT Helpdesk

CampusFlow is a command-line helpdesk application for recording, prioritizing, assigning, and tracking campus IT support tickets. It was developed as a two-engineer Python engineering sprint project.

The application uses **Python's standard library only**. Ticket records are stored in a local JSON file; no web framework, database server, external package, or API key is required.

## Features

- **Create tickets:** capture a title, category, urgency, and number of affected users. New tickets start as `open` and unassigned.
- **Validate inputs:** reject blank titles, unsupported categories or urgency levels, and invalid affected-user counts.
- **Automatic priorities:** assign `critical`, `high`, `medium`, or `low` based on urgency and impact.
- **List and view tickets:** browse existing tickets or inspect one by ID.
- **Assign staff:** assign a nonblank staff name to an unresolved ticket.
- **Track progress:** move tickets through controlled status transitions and reopen resolved tickets.
- **Work queue:** show open tickets by priority, with lower ticket numbers first when priorities match.
- **Reports:** summarize ticket totals and counts by status and priority.
- **JSON persistence:** save and reload tickets between application sessions, while rejecting malformed data and duplicate ticket IDs on load.
- **Automated tests:** exercise ticket management, workflow, storage, and reporting behavior with `unittest`.

## Requirements

- Python 3
- A terminal or command prompt

No third-party dependencies are needed.

## Getting started

Clone the repository and enter its root directory:

```bash
 git clone https://github.com/el-ahavah/campusflow.git
 cd campusflow
```

Run the CLI:

```bash
python3 main.py
```

On Windows, `python main.py` may be appropriate if `python3` is unavailable.

Follow the on-screen menu to create, list, view, assign, update, reopen, queue, and report on tickets. The CLI also provides an exit option.

## Ticket fields

Each ticket is represented as a Python dictionary with these fields:

| Field | Meaning | Example |
| --- | --- | --- |
| `id` | Unique sequential ticket ID | `T001` |
| `title` | Brief description | `Wi-Fi unavailable` |
| `category` | `Network`, `Hardware`, `Software`, or `Other` | `Network` |
| `urgency` | `low`, `medium`, or `high` | `high` |
| `affected_users` | Positive integer | `12` |
| `priority` | Calculated impact priority | `critical` |
| `status` | `open`, `in_progress`, or `resolved` | `open` |
| `assigned_to` | Staff name or `None` | `None` |

### Priority rules

Rules are evaluated in order:

1. **Critical:** urgency is `high` **and** at least 10 users are affected.
2. **High:** urgency is `high` **or** at least 10 users are affected.
3. **Medium:** urgency is `medium` **or** at least 3 users are affected.
4. **Low:** all other valid tickets.

### Workflow rules

```text
open --(assigned to staff)--> in_progress --> resolved
 ^                                          |
 |------------------ reopen ----------------|
```

- A ticket must be assigned before it can move from `open` to `in_progress`.
- An `in_progress` ticket can move to `resolved`.
- A resolved ticket must be reopened before it can be assigned or progressed again.
- The queue contains **open** tickets only. Tickets of equal priority are ordered by numeric ticket ID.

## Run tests

From the repository root:

```bash
python3 -m unittest discover -s tests -v
```

This runs the available automated tests in the `tests/` directory. Run the suite again after merging both feature branches.

## Project structure

```text
campusflow/
├── README.md
├── .gitignore
├── main.py
├── campusflow/
│   ├── __init__.py
│   ├── tickets.py
│   ├── workflow.py
│   ├── storage.py
│   └── reports.py
├── tests/
│   ├── test_tickets.py
│   ├── test_workflow.py
│   ├── test_storage.py
│   └── test_reports.py
└── docs/
    ├── ai-learning-log.md
    └── design-decisions.md
```

`main.py` is the CLI entry point. The `campusflow/` package contains the application logic, and `tests/` contains the automated tests. The documentation folder records design choices and verified AI-learning interactions.

**Local data:** The application uses a JSON ticket file (typically `tickets.json`). Keep runtime ticket data and machine-specific development files out of Git, as configured in `.gitignore`.

## Team responsibilities

| Contributor | Main responsibility |
| --- | --- |
| Engineer A | Ticket creation, validation, priority calculation, ID generation, JSON storage, and related tests |
| Engineer B | Ticket listing/viewing, assignment, status workflow, work queue, reporting, and related tests |
| Both engineers | CLI integration, code review, integration checks, documentation, and final verification |

Development took place on separate feature branches with GitHub Pull Requests and peer reviews before merging.

## Additional documentation

- [Design decisions](docs/design-decisions.md)
- [AI learning log](docs/ai-learning-log.md)

## Final verification checklist

Before considering the project complete, confirm that all tests pass, that ticket creation and updates work from the CLI, that saved tickets survive a restart, that new IDs remain unique after reloading, and that the approved Pull Requests and documentation have been merged into `main`.