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
