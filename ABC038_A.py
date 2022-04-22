import io
import sys

_INPUT = """\
6
ICEDT
MUGICHA
OOLONGT
T
TEA
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  if S[-1]=='T': print('YES')
  else: print('NO')