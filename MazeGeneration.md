MAZE GENERATION
===================

参考文献
---------

http://www.redblobgames.com/articles/noise/introduction.html
http://www-cs-students.stanford.edu/~amitp/game-programming/polygon-map-generation/
http://en.wikipedia.org/wiki/Maze_generation_algorithm
http://devmag.org.za/2009/04/25/perlin-noise/
http://paulbourke.net/fractals/noise/
http://www.redblobgames.com/articles/noise/2d/



关于噪声与迷宫
----------------

## 1. 一维随机地图

simple

    import random

    def mazegen():
        maze = ['.'] * 20
        pos = random.randint(0, 19)
        maze[pos] = 'x'
        return ''.join(maze)

# treasures more likely to be on the left than the right

    def mazegen():
        maze = ['.'] * 20
        pos = random.randint(0, 19) / 2
        maze[pos] = 'x'
        return ''.join(maze)

# treasures to sometimes be on the right, but more often on the left

    def mazegen():
        maze = ['.'] * 20
        pos = random.randint(0, 19)
        pos = pos**2 / 19
        maze[pos] = 'x'
        return ''.join(maze)

    def mazegen():
        maze = ['.'] * 20
        limit = random.randint(0, 19)
        pos = random.randint(0, limit)
        maze[pos] = 'x'
        return ''.join(maze)


## 2. 噪声

    %pylab inline
    import seaborn
    import random
    from matplotlib import pylab

山谷

    for i in range(5):
        random.seed(i)  # give the same results each run
        fig = pylab.figure(figsize = (20, 3))
        pylab.plot([random.randint(1, 3) for i in range(80)])
        pylab.show()
    
较为集中的山谷

    for i in range(5):
        random.seed(i)  # give the same results each run
        fig = pylab.figure(figsize = (20, 3))
        pylab.plot([random.randint(1, random.randint(1, 3)) for i in range(80)])
        pylab.show()

山谷 with coherence 

    def adjacent_min(noise): # 谷较多
        return [min(noise[i], n) for i,n in enumerate(noise[1:])]

    for i in range(5):
        random.seed(i)
        fig = pylab.figure(figsize = (20, 3))
        noise = [random.randint(1, 3) for i in range(80)]
        pylab.plot(adjacent_min(noise))
        pylab.show()

山较多可以用max，山谷差不多多可以用求均值；可以进行多次noise modification获得更加平滑的山谷
平滑(smoothing)作为滤子在信号处理中被称作Low-pass filter（柔化？）
还有求和、求差等滤子


## 3. 制造噪声

Some of the basic 1D/2D noise generators are:

- Use random numbers directly for the output. This is what we did for valleys/hills/mountains.

- Use random numbers as parameters for sines and cosines, which are used for the output.

- Use random numbers as parameters for gradients, which are used for the output. This is used in Perlin Noise.

Some of the common ways to modify noise are:

- Apply a filter to reduce or amplify certain characteristics. For valleys/hills/mountains we used smoothing to reduce the bumpiness, increase the size of valleys, and make mountains occur near valleys.

- Add multiple noise functions together, typically with a weighted sum so that we can control how much each noise function contributes to the total.

- Interpolate between the noise values the noise function gives us, to generate smooth areas.


## 4. 使用噪音

Instead of using noise for elevation you might be using it for audio.

Or maybe you’re using it to make a shape. For example, you can use noise as a radius in a polar plot. You can convert a 1D noise function like this into a polar form by using the output as a radius instead of as an elevation. Here is what that same function looks like in polar form.

Or you might be using noise as a graphical texture. Perlin noise is often used for this.

You might use noise to choose the locations of objects, such as trees or gold mines or volcanos or earthquake fault lines. In an earlier example, I used a random number to choose the location of the treasure chest.

You might use noise as a threshold function. For example, you can say that any time the value is greater than 3, then one thing happens, otherwise something else happens. One example of this is using 3D Perlin noise to generate caves. You can say that anything above a certain density threshold is solid earth and anything below that threshold is open air (cave).


## 5. 噪音的颜色

参考资料：http://en.wikipedia.org/wiki/Colors_of_noise

- 白噪声：各种频率对噪声的贡献差不多

        for i in range(5):
            random.seed(i)
            fig = pylab.figure(figsize = (20, 3))
            noise = [random.uniform(-1, +1) for i in range(80)]
            pylab.plot(noise)
            pylab.show()

- 红噪声：又称为Brownian noise，低频占主要地位

        def smoother(noise):
            return [0.5 * (noise[i] + n) for i,n in enumerate(noise[1:])]
        
        for i in range(5):
            random.seed(i)
            fig = pylab.figure(figsize = (20, 3))
            noise = [random.uniform(-1, +1) for i in range(mapsize)]
            pylab.plot(smoother(noise))
            pylab.show()

- 粉噪声：介于白噪声和红噪声之间，自然界出现最多的噪声，呈现山谷clustering的现象

- 紫噪声：和红噪声相反，高频占主要地位

        def smoother(noise):
            return [0.5 * (noise[i] - n) for i,n in enumerate(noise[1:])]
        
        for i in range(5):
            random.seed(i)
            fig = pylab.figure(figsize = (20, 3))
            noise = [random.uniform(-1, +1) for i in range(mapsize)]
            pylab.plot(smoother(noise))
            pylab.show()

- 蓝噪声：介于白噪声和紫噪声之间，低高频分布得比较均匀，城市格局常见噪声

- 白、粉、蓝用的最多


## 6. 混合噪声

- Instead of choosing an array of random numbers, we’re choosing a single random number, and using it to shift a sine wave left or right.

- We can make noise by taking a weighted sum of other noise functions that have different frequencies.

- We can choose the characteristics of the noise by choosing the weights for the weighted sum.

- We can generate noise by a weighted sum of sine waves at different frequencies.

- The various colors of noise have weights (amplitudes) that follow a function f^c. （c从负到正，对应权重分布从单调减到单调增，频率越来越高）

- By changing the exponent you can get different colors of noise from the same set of random numbers.


迷宫生成
-----------------

示例1：

    from random import shuffle, randrange
    import numpy
    from numpy.random import random_integers as rand
    import matplotlib.pyplot as pyplot
     
    def maze(width=81, height=51, complexity=.75, density=.75):
        # Only odd shapes
        shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
        # Adjust complexity and density relative to maze size
        complexity = int(complexity * (5 * (shape[0] + shape[1])))
        density    = int(density * (shape[0] // 2 * shape[1] // 2))
        # Build actual maze
        Z = numpy.zeros(shape, dtype=bool)
        # Fill borders
        Z[0, :] = Z[-1, :] = 1
        Z[:, 0] = Z[:, -1] = 1
        # Make aisles
        for i in range(density):
            x, y = rand(0, shape[1] // 2) * 2, rand(0, shape[0] // 2) * 2
            Z[y, x] = 1
            for j in range(complexity):
                neighbours = []
                if x > 1:             neighbours.append((y, x - 2))
                if x < shape[1] - 2:  neighbours.append((y, x + 2))
                if y > 1:             neighbours.append((y - 2, x))
                if y < shape[0] - 2:  neighbours.append((y + 2, x))
                if len(neighbours):
                    y_,x_ = neighbours[rand(0, len(neighbours) - 1)]
                    if Z[y_, x_] == 0:
                        Z[y_, x_] = 1
                        Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                        x, y = x_, y_
        return Z
     
    pyplot.figure(figsize=(10, 5))
    pyplot.imshow(maze(80, 40), cmap=pyplot.cm.binary, interpolation='nearest')
    pyplot.xticks([]), pyplot.yticks([])
    pyplot.show()
 
示例2：

    def make_maze(w = 16, h = 8):
        vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
        ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
        hor = [["+--"] * w + ['+'] for _ in range(h + 1)]
     
        def walk(x, y):
            vis[y][x] = 1
     
            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(d)
            for (xx, yy) in d:
                if vis[yy][xx]: continue
                if xx == x: hor[max(y, yy)][x] = "+  "
                if yy == y: ver[y][max(x, xx)] = "   "
                walk(xx, yy)
     
        walk(randrange(w), randrange(h))
        for (a, b) in zip(hor, ver):
            print(''.join(a + ['\n'] + b))
     
    make_maze()

示例3：

    import random

    DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
    ALL_DIRECT = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))

    def printMaze(maze):
        for line in maze:
            print(' '.join(['X' if ch == 1 else "-" for ch in line]))

    def neighbours(coor, maze, direct=DIRECTIONS):
        x, y = coor
        N = len(maze)
        res = []
        for d in direct:
            nx = x + d[0]
            ny = y + d[1]
            if 0 < nx < N - 1 and 0 < ny < N - 1:
                res.append((nx, ny))
        return res

    def carve(coor, maze):
        maze[coor[0]][coor[1]] = 0

    def isOpen(coor, maze):
        return not maze[coor[0]][coor[1]]

    def generateMaze(N):
        maze = [[1] * N for _ in range(N)]
        start = (1, 1)
        exit = (N - 2, N - 2)
        queue = [start]
        good_neighs = []
        while queue or good_neighs:
            if good_neighs:
                current = random.choice(good_neighs)
                queue.append(current)
            else:
                current = queue[-1]
            carve(current, maze)
            neighs = [n for n in neighbours(current, maze) if not isOpen(n, maze)]
            good_neighs = []
            for n in neighs:
                new_neighs = neighbours(n, maze, ALL_DIRECT)
                all_current_neighs = neighbours(current, maze)
                for cn in all_current_neighs:
                    if cn in new_neighs:
                        new_neighs.remove(cn)
                if len([1 for x, y in new_neighs if maze[x][y] == 0]) <= 1:
                    good_neighs.append(n)
            if not good_neighs:
                queue.remove(current)
        maze[10][10] = 0
        return maze

    def generateGoodMaze(N):
        while True:
            mz = generateMaze(12)
            if mz[9][10] and mz[10][9]:
                continue
            return mz

示例4：

    import random

    DIRECT_4 = ((1, 0), (-1, 0), (0, 1), (0, -1))
    DIRECT_8 = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))

    def show_maze(maze):
        for line in maze:
            print ' '.join([u'@' if ch == 1 else " " for ch in line])

    def get_neighbor(p, xlim, ylim, directions):
        constraint = lambda p: 0 < p[0] < xlim-1 and 0 < p[1] < ylim-1
        plist = [(p[0]+i, p[1]+j) for i,j in directions]
        return set(filter(constraint, plist))

    def generateMaze(w, h):
        maze = [[1] * w for _ in range(h)]
        to_search = [(random.randint(1, h-1), random.randint(1, w-1))]
        while to_search:
            cur_p = to_search[-1]
            maze[cur_p[0]][cur_p[1]] = 0
            
            neighbors = [p for p in get_neighbor(cur_p, h, w, DIRECT_4) if maze[p[0]][p[1]]]
            
            available = []
            for p in neighbors:
                new_neighs = get_neighbor(p, h, w, DIRECT_8).difference(get_neighbor(cur_p, h, w, DIRECT_4))
                if sum([maze[i][j] == 0 for i,j in new_neighs]) <= 1:
                    available.append(p)
            
            if available:
                to_search.append(random.choice(available))
            else:
                to_search.pop()
        return maze