import sys

# Read N
line = sys.stdin.readline()
assert line != ""

n = int(line.strip())
assert 1 <= n <= 200000

# Read the usefulness values
line = sys.stdin.readline()
assert line != ""

values = list(map(int, line.split()))

# There must be exactly N values
assert len(values) == n

# Every value must satisfy the problem constraints
for value in values:
    assert -10000 <= value <= 10000

# There should be no additional input
assert sys.stdin.read() == ""

sys.exit(42)

