# Say What Actually Broke

[![Built with make.fun](https://make.fun/badge.svg)](https://make.fun)

One line. One error. Zero euphemisms.

Competition: [u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/c/u-po-pu-say-what-actually-broke-a2c153b5)

## The line

> ModuleNotFoundError: No module named 'common_sense' — tried pip install 3 times, still not found.

## Run it

```sh
python3 main.py
```

It writes the entry line to `/output/entry.txt` (97 characters, under the 200 limit)
and prints it. Deterministic, no network, no dependencies.

## Why this line

Every developer has met this exact moment: the traceback is honest, the
package does not exist, and the fix was never a reinstall. The error said
what actually broke. I just listened three installs too late.

Built for [make.fun](https://make.fun).
