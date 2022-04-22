import io
import sys

_INPUT = """\
6
3
3 3
1 1
2 2
2
4 5
4 3
4
2 5
3 3
4 5
6 6
5
8 8
5 3
2 2
4 2
2 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from bisect import bisect_left
  def LIS(A: list):
    L = [A[0]]
    ID=[0]*len(A)
    for i in range(1,len(A)):
        if A[i] > L[-1]:
            L.append(A[i])
            ID[i]=len(L)-1
        else:
            tmp=bisect_left(L, A[i])
            L[tmp] = A[i]
            ID[i]=tmp
    L2=[]
    L3=[]
    m=len(L)-1
    for i in range(len(A)-1,-1,-1):
      if ID[i]==m:
          L2.append(A[i])
          L3.append(i)
          m-=1
    return len(L) #それぞれ最長増加部分列の長さ、復元した部分列、そのインデックス
  N=int(input())
  box=[list(map(int,input().split())) for _ in range(N)]
  box.sort(key=lambda x: (x[0],-x[1]))
  print(LIS([box[i][1] for i in range(N)]))