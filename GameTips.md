GAME TIPS
===================

监听方向键：

    import sys, msvcrt

    command = ''
    while True:
        ch = msvcrt.getch()
        print [ch]

        if ch == 'q':
            print "\nBye."
            break
        else:
            command += ch
            if len(command) > 2:
                command = command[-2:]

        if command == '\xe0H': # 上键实际上是两个字符
            print 'up'

分次同行输出避免自动加入空格

    from __future__ import print_function

    print('abc', end='')

中文及其他unicode字符

    # -*- coding: utf-8 -*-
    # 这一句意味着可以在代码里直接使用unicode字符

    print u'一二三四五六七八九'
    print(u'now: 一')
    # 只有中文或中英文混合的话，直接打印unicode形式的即可

    input('now: ' + u'一'.encode('gbk'))
    # input或者raw_input函数的字符必须事先转码



