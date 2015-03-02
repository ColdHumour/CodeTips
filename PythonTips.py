# -*- coding: utf-8 -*-

# 地图寻路，给定二维数组作为地图
# 邻接坐标：
def get_neighbor(p, xlim, ylim, constraint):
    all_constraint = lambda p: 0 <= p[0] < xlim and 0 <= p[1] < ylim and constraint(*p)
    plist = [(p[0]+i, p[1]+j) for i in [-1,0,1] for j in [-1,0,1]][1::2]
    # plist = [(p[0]+i, p[1]+j) for i in [-1,0,1] for j in [-1,0,1] if i or j]
    return filter(all_constraint, plist)
    
# 简单寻路，判断是否相通，广度优先搜索：
from collections import deque

def is_accessible(p1, p2, region):        
    xlim, ylim = len(region), len(region[0])
    visited, to_search = set([]), deque([p1])
    
    # 根据问题不同修改constraint
    constraint = lambda i,j: (region[i][j] in '.') and ((i,j) not in visited)
    
    while to_search and p2 not in to_search:
        cur_p = to_search.popleft()
        plist = get_neighbor(cur_p, xlim, ylim, constraint)
        visited.add(cur_p)
        to_search += plist
    return p2 in to_search

# 简单寻路，记录路径，广度优先搜索：
from collections import deque

def find_path(p1, p2, region):        
    xlim, ylim = len(region), len(region[0])
    visited, to_search = {p1: None}, deque([p1])
    
    # 根据问题不同修改constraint
    constraint = lambda i,j: (region[i][j] in '.') and ((i,j) not in visited)
    
    while to_search and p2 not in to_search:
        cur_p = to_search.popleft()
        plist = get_neighbor(cur_p, xlim, ylim, constraint)
        for p in plist:
            visited[p] = cur_p
        to_search += plist
    
    if p2 not in to_search: return []
    
    trace = [cur_p, p2]
    while p1 not in trace:
        trace = [visited[trace[0]]] + trace
    return trace

# A*寻路算法，记录路径，深度优先搜索
# 需要定义距离函数h_score
def h_score(p1, p2):
    return 

def find_path_a_star(start, end, region):
    xlim, ylim = len(region), len(region[0])
    visited, to_search = {}, {start: (h_score(start, end), 0, None)}
    
    # 根据问题不同修改constraint
    constraint = lambda i,j: (region[i][j] in '.') and ((i,j) not in visited)
    
    while to_search and (end not in to_search):
        cur_p = sorted(to_search.keys(), key = lambda x: x[0])[0]
        _, g, pre_p = to_search.pop(cur_p)
        visited[cur_p] = pre_p
        for p in get_neighbor(cur_p, xlim, ylim, constraint):
            h = h_score(p, end)
            if (p not in to_search) or (g + h + 1 < to_search[p][0]):
                to_search[p] = (g + h + 1, g + 1, cur_p)

    if end not in to_search: return []

    trace = [cur_p, end]
    while start not in trace:
        trace = [visited[trace[0]]] + trace
    return trace



# Dijkstra Algorithm
# 输入为距离矩阵，默认第一个为起始点，最后一个为结束点
def dijkstra(distance):
    n = len(distance)
    D = dict(zip(range(1, n), distance[0][1:]))
    while 1:
        p_move = min(D.keys(), key = D.get)
        if p_move == n-1:
            return D[n-1]
        for p_togo in D:
            D[p_togo] = min(D[p_togo], D[p_move] + distance[p_move][p_togo])
        del D[p_move]



# 根据邻接关系搜索，记录路径
# 边不重复，深度优先
from collections import deque

def find_path(p1, p2, dictionary):
    to_search = deque([(p1, p)] for p in dictionary[p1])
    while to_search:
        trace = to_search.popleft()
        cur_p = trace[-1][1]
        for p in dictionary[cur_p]:
            if (cur_p, p) not in trace and (p, cur_p) not in trace:
                if 1:           # add stop conditions here
                    nodes = [e[0] for e in trace] + [cur_p, p]
                    return      # return any format you want
                else: 
                    to_search.appendleft(trace + [(cur_p, p)])

# 边不重复，广度优先
from collections import deque

def find_path(p1, p2, dictionary):
    to_search = deque([(p1, p)] for p in dictionary[p1])
    while to_search:
        trace = to_search.popleft()
        cur_p = trace[-1][1]
        for p in dictionary[cur_p]:
            if (cur_p, p) not in trace and (p, cur_p) not in trace:
                if 1:           # add stop conditions here
                    nodes = [e[0] for e in trace] + [cur_p, p]
                    return      # return any format you want
                else: 
                    to_search.append(trace + [(cur_p, p)])



# 并查集，根据二元关系分组
from collections import defaultdict

class UF:
    def __init__(self, elements):
        self.idxmap = dict(zip(elements, elements))
        self.size   = dict(zip(elements, [1]*len(elements)))

    def find(self, p):
        c = self.idxmap[p]
        if p != c:
            c = self.idxmap[p] = self.find(c)
        return c
    
    def union(self, p, q):
        p, q = self.find(p), self.find(q)
        if p != q and self.size[p] < self.size[q]:
            self.idxmap[p] = q
            self.size[q] += self.size[p]
        elif p != q and self.size[p] >= self.size[q]:
            self.idxmap[q] = p
            self.size[p] += self.size[q]
    
    @property
    def n_groups(self):
        return sum(p==q for p, q in self.idxmap.items()) 

    @property
    def groups(self):
        gdict = defaultdict(set)
        for p in self.idxmap:
            gdict[self.find(p)].add(p)
        return gdict.values()