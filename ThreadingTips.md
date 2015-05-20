THREADING TIPS
=============

---

简单使用
-----------

## 导入模块

    import threading

## 创建线程库

    def f1(*args):
        ...

    def f2(*args):
        ...

    threads = []
    t1 = threading.Thread(target=f1,args=args1)
    threads.append(t1)
    t2 = threading.Thread(target=f2,args=args2)
    threads.append(t2)
    ...

## 启动线程

    t.start()

    # 父子线程分开运行，如果父线程先运行完，则等待子线程运行完后再结束

## 等待线程

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    # 如果一个线程或者一个函数在执行过程中产生了另外一个线程t，则t.join()的意思
    # 是暂时阻塞t线程的父线程或父函数，等t执行完之后再执行
    
    # join()有个参数为timeout，即等待如果超过这个时间t仍没执行完，也不再等待

## 守护线程

    t.setDaemon(True)

    # 守护线程需要在start()方法调用之前设置，如果不设置则该线程会被无限挂起
    # 此方法为True，则当父线程执行完后，不等待子线程执行完，强制一同结束

## threading.Thread方法
    
    t.isAlive()        # 该线程是否在运行
    t.isDaemon()       # 该线程是否随主线程一起结束

    t.setname('tName') # 线程命名
    t.getname()        # 获得线程名字

## threading方法

    threading.activeCount()  # 包含了父线程在内的线程个数
    threading.enumerate()    # 当前运行中的Thread对象列表

---

高级方法
-----------------

## 继承threading.Thread

    class MyThread(threading.Thread):
        def __init__(self, threadname):
            super(MyThread, self).__init__(name=threadname)
            self.id = threadname
        
        def run(self):
            '''线程运行时做的事情'''

## 线程调度，锁

    """锁对象由threading.Lock类创建。线程可以使用锁的acquire()方法获得锁，这样锁就进入"locked"状态。每次只有一个线程可以获得锁。如果当另一个线程试图获得这个锁的时候，就会被系统变为"blocked"状态，直到那个拥有锁的线程调用锁的release()方法来释放锁，这样锁就会进入"unlocked"状态。"blocked"状态的线程就会收到一个通知，并有权力获得锁。如果多个线程处于"blocked"状态，所有线程都会先解除"blocked"状态，然后系统选择一个线程来获得锁，其他的线程继续"blocked"。
    """

    mutex = threading.Lock()  # 锁是全局的，只有一把

    class MyThread(threading.Thread):
        ...

        def run(self):
            mutex.acquire()   # 本线程获得锁
                        
            "do something..."

            mutex.release()   # 本线程释放锁

        # 上面这种写法是死等锁释放，如果想在拿不到锁的时候做其他事情，可以这样：
        # acquire有一个timeout的参数可供设置，如果过了timeout，则有False作为返回值
        # 所以可以这么写

        def run(self):
            if mutex.acquire(sometime):
                        
                "do something..."

                mutex.release()
            else:

                "do something else..."

## 线程调度，多重锁


## 线程调度，条件同步