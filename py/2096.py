import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
Mdp = list(map(int, input().split()))
mdp = deepcopy(Mdp)

for _ in range(n-1):
    temp = list(map(int, input().split()))
    Mtemp = deepcopy(Mdp)
    mtemp = deepcopy(mdp)

    Mdp[0] = max(Mtemp[0], Mtemp[1]) + temp[0]
    mdp[0] = min(mtemp[0], mtemp[1]) + temp[0]
    
    Mdp[1] = max(Mtemp[0], Mtemp[1], Mtemp[2]) + temp[1]
    mdp[1] = min(mtemp[0], mtemp[1], mtemp[2]) + temp[1]
    
    Mdp[2] = max(Mtemp[2], Mtemp[1]) + temp[2]
    mdp[2] = min(mtemp[2], mtemp[1]) + temp[2]

print(max(Mdp), min(mdp))