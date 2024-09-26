import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input().strip())

total_score = 0

for _ in range(n):
    row = input().strip().split()
    for square in row:
        if square != '.':
            hex_value = int(square, 16)
            square_value = 2 ** hex_value
            total_score += square_value