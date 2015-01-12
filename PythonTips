# -*- coding: utf-8 -*-

# 邻接坐标：
def get_neighbor(p, xlim, ylim, constraint):
    plist = [(p[0]+i, p[1]+j) for i in [-1,0,1] for j in [-1,0,1]][1::2]
    # plist = [(p[0]+i, p[1]+j) for i in [-1,0,1] for j in [-1,0,1] if i or j]
    return [p for p in plist if 0 <= p[0] < xlim and 0 <= p[1] < ylim and constraint(*p)]

# 简单寻路1，判断是否相通：
from collections import deque

def is_accessible(p1, p2, region):        
    xlim, ylim = len(region), len(region[0])
    visited, to_search = set([]), deque([p1])
    constraint = lambda i,j: (region[i][j] in '.') and ((i,j) not in visited)
    while to_search and p2 not in to_search:
        cur_p = to_search.popleft()
        plist = get_neighbor(cur_p, xlim, ylim, constraint)
        visited.add(cur_p)
        to_search += plist
    return p2 in to_search

# 简单寻路2，记录路径：
from collections import deque

def find_path(p1, p2, region):        
    xlim, ylim = len(region), len(region[0])
    visited, to_search = {p1: None}, deque([p1])
    constraint = lambda i,j: (region[i][j] in '.') and ((i,j) not in visited)
    while to_search and p2 not in visited:
        cur_p = to_search.popleft()
        plist = get_neighbor(cur_p, xlim, ylim, constraint)
        for p in plist:
            visited[p] = cur_p
        to_search += plist
    
    if p2 not in visited: return []
    
    trace = [p2]
    while p1 not in trace:
        trace = [visited[trace[0]]] + trace
    return trace
