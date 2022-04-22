import io
import sys

_INPUT = """\
6
1080 1920
1080 1920
1080 1920
1920 1080
334 668
668 1002
100 200
300 150
120 120
240 240
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  if len(set(list(map(int,input().split())))&set(list(map(int,input().split()))))>0: print('YES')
  else: print('NO')
