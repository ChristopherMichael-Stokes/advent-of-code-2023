# Advent of Code 2023

I missed the boat on this one, so am coming back to do a few as warmup for the 2024 series.  We'll see if I actually get around to these either 🥲.

## Setup

I've tried to write as much as possible in standard python3.12, only using extra dependencies for non-functional code (i.e. tqdm (progress bars), numba (computational optimisation), ...) and where it would *significantly* improve the tidyness of the solution without doing too much for me.

### Python Environment

The environment is managed through [uv](https://github.com/astral-sh/uv), which you will need to install if not already.
We can setup the environment then run any implemented solution as follows:

```sh
# Setup env, installing python3.12 if missing + all dependencies
uv sync

# Run day01.py solutions
uv run python problems.py 1

...

# Run day25.py solutions
uv run python problems.py 25
```