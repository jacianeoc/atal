import sys
sys.setrecursionlimit(100000)
from math import *
 
 
def ints_input():
    return [int(i) for i in sys.stdin.readline().strip("\n").split(" ")]
 
 
def print_list(arr):
    sys.stdout.writelines(str(x)+" " for x in arr)
    sys.stdout.write("\n")
 
 
def fast_input(type=str):
    return type(sys.stdin.readline().strip("\n"))
 
 
def valid(i, j):
    return i >= 0 and j >= 0 and i < n and j < m
 
def dfs(i, j, p1, p2):
    if visited[i][j]:
        return
    visited[i][j] = 1
    for k in range(4):
        cx = i +dx[k]
        cy = j+ dy[k]
        if valid(cx, cy):
            if grid[i][j] == grid[cx][cy]:
                if not visited[cx][cy]:
                    dfs(cx, cy, i, j)
                else:
                    if cx != p1 or cy != p2:
                        global ans
                        ans = 1
                        return
            
ans = 0
n, m = ints_input()
grid = []
for i in range(n):
    grid.append(fast_input())
 
visited = [[0 for i in range(m)] for i in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
 
for i in range(n):
    for j in range(m):
        dfs(i, j, 0, 0)
        
if ans:
    print("Yes")
else:
    print("No")