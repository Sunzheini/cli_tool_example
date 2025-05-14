# cli_tool_example


**Objective**:

Build a Python CLI tool that:
1. Fetches data from multiple URLs concurrently.
2. Implements caching to avoid redundant HTTP calls.
3. Handles errors gracefully (retries, timeouts).
4. Is extensible (easy to add new data processors).
5. Includes tests and performance benchmarks.


**Requirements**:

_Concurrency Model_
1. Use asyncio (preferred) or multiprocessing to fetch URLs in parallel.
2. Limit max concurrent requests (e.g., 5 at a time).

_Caching_
1. Cache responses (e.g., using functools.lru_cache or Redis).
2. Cache should expire after 1 hour.

_Error Handling_
1. Retry failed requests (max 3 retries).
2. Skip URLs that fail permanently.

_Extensibility_
1. Allow adding custom response processors (e.g., extract titles, count words).

_Testing_
1. Write unit tests (pytest) for core logic.
2. Mock HTTP requests (e.g., pytest-httpx).

_CLI Interface_
1. Accept URLs from a file or command line.
2. Output results in JSON/CSV.


**What the Interviewer Evaluates:**

Architecture
1. Is the code modular (e.g., separate caching, fetching, error handling)?
2. Can it scale to 10,000 URLs?

Performance
1. Does it avoid blocking I/O?
2. Is caching implemented efficiently?

Robustness
1. How are network errors/timeouts handled?
2. Are edge cases (malformed URLs, empty responses) covered?

Testing
1. Are there tests for concurrency, caching, and error paths?

Extensibility
1. Can new processors (e.g., HTML parsers) be added without modifying core logic?

Bonus Points For:
1. Using httpx instead of aiohttp for HTTP/2 support.
2. Adding a progress bar (tqdm).
3. Supporting rate limiting (e.g., 10 requests/second).
4. Dockerizing the scraper.


