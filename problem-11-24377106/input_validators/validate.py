#!/usr/bin/env python3
"""Strict input validator: Kattis/problemtools success exit code is 42.

Accept exactly the documented number of lines and integer fields; reject
out-of-range endpoints, self-loops and tolls. Parallel roads are permitted.
"""
import re
import sys

INTEGER = re.compile(rb"(?:0|[1-9][0-9]*)\Z")


def require(condition, message):
    if not condition:
        print(message, file=sys.stderr)
        sys.exit(43)


def integers(line, count, number):
    require(bool(line), "Missing line {}".format(number))
    require(line.endswith(b"\n"), "Line {} must end with newline".format(number))
    fields = line.split()
    require(len(fields) == count, "Wrong field count on line {}".format(number))
    require(all(INTEGER.fullmatch(x) for x in fields),
            "Invalid nonnegative integer on line {}".format(number))
    return [int(x) for x in fields]


n, m = integers(sys.stdin.buffer.readline(), 2, 1)
require(1 <= n <= 200000, "n out of range")
require(0 <= m <= 300000, "m out of range")
for i in range(m):
    u, v, w = integers(sys.stdin.buffer.readline(), 3, i + 2)
    require(1 <= u <= n and 1 <= v <= n, "Endpoint out of range")
    require(u != v, "Self-loops are not permitted")
    require(0 <= w <= 10**9, "Toll out of range")
require(sys.stdin.buffer.read() == b"", "Extra input after the last road")
sys.exit(42)
