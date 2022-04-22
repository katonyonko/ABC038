import io
import sys

_INPUT = """\
6
5
1 2 3 2 1
4
1 2 3 4
6
3 3 4 1 2 2
6
1 5 2 3 4 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  ans=0
  l,r=0,0
  while l<N:
    while r+1<N and A[r]<A[r+1]:
      r+=1
    ans+=r-l+1
    l+=1
    r=max(r,l)
  print(ans)