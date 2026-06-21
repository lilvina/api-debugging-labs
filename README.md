# API Debugging Labs

A hands-on troubleshooting lab series for developers learning how to debug common API issues.

Each lab contains a small broken Flask API. Learners must run the app, reproduce the error, investigate the cause and apply a fix.

## Who this is for

This project is designed for:

- New backend developers
- API bootcamp students
- Developer education workshops
- DevRel/technical curriculum demos
- Instructors teaching debugging workflows

## Learning goals

By the end of these labs, learners should be able to:

- Read API error messages and logs more carefully
- Use HTTP status codes to guide debugging
- Identity common configuration and environment problems
- Debug authenication, CORS, rate limiting, JSON and database issues
- Explain the difference between symptoms and root causes
- Document a clear troubleshooting process

## Tech stack

- Python
- Flask
- SQLite
- Flask-CORS
- python-dotenv

## Getting started

Clone the repo:

```bash
git clone https://github.com/lilvina/api-debugging-labs.git
cd api-debugging-labs
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip3 install -r requirements.txt
```

Then test the endpoint with curl or Postman.

## Lab Test

| Lab | Topic | Primary Skill |
|---|---|---|
| Lab 1 | 401 Authentication Error | Debugging headers and API keys |
| Lab 2 | Missing Environment Variables | Debugging configuration issues |
| Lab 3 | Rate Limiting 429 | Understanding API limits |
| Lab 4 | Invalid JSON Responses | Debugging response formatting |
| Lab 5 | CORS Issues | Debugging browser/API communication |
| Lab 6 | Database Connection Failure | Debugging database setup |

## Sugguested learner workflow

For each lab:

1. Read the `problem.md` file.
2. Run the broken app.
3. Reproduce the issue.
4. Read the error message or API response.
5. Try the hints only if needed.
6. Fix the bug.
7. Compare your answer with `solution-guide.md`.
8. Review `instructor-notes.md` for teaching ideas.

## Instructor use

These labs can be used as:

- A live debugging workshop
- A take-home exercise
- Pair programming practice
- API onboarding material
- A technical curriculum portfolio sample

## Recommended workshop format

| Time | Activity |
|---|---|
| 5 min | Introduce the debugging strategy |
| 10 min | Learners reproduce the bug |
| 15 min | Learners investigate and fix |
| 10 min | Group debrief |
| 5 min | Instructor explains production relevance |

## Debugging checklist

Before jumping to the solution, ask:

- What status code am I getting?
- Is the request formatted correctly?
- Are headers missing?
- Are environment variables loaded?
- Is the server returning valid JSON?
- Is the database connected?
- Is this a browser-only issue or an API issue?

## License

MIT
