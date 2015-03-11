PYQT4 TIPS
=================

---

参考资料：

http://www.cnblogs.com/rollenholt/archive/2011/11/16/2251904.html

http://zetcode.com/gui/pyqt4/introduction/

http://pyqt.sourceforge.net/Docs/PyQt4/classes.html

---

运行
-------------

- 首先要建立app实例，类为QtGui.QApplication

        app = QtGui.QApplication(sys.argv)

- 为了能够反复调用，一般这么写

        app = QtGui.QApplication.instance() 
        if not app: app = QtGui.QApplication(sys.argv)

- 对于已定义的类，创建实例之后调用show()方法

- 最后加上

        app.exec_() # 或者 sys.exit(app.exec_())

窗口
-------------

- 空白窗口，父类：QtGui.QWidget

        import sys
        from PyQt4 import QtCore, QtGui

        class MyWindow(QtGui.QWidget):
            def __init__(self):
                QtGui.QtGui.QWidget.__init__(self)
                self.setWindowTitle("PyQt")  # 窗口名
                self.resize(300, 200)        # 窗口大小
                
                # self.setToolTip('This is a <b>QWidget</b> widget') # 信息提示
                # QtGui.QToolTip.setFont(QtGui.QFont('Courier New', 10)) # 字体

        app = QtGui.QApplication.instance() 
        if not app: app = QtGui.QApplication(sys.argv)

        mywindow = MyWindow()
        mywindow.show()
        app.exec_()

- 窗口居中，move
        
        def __init__(self):
            self.center()

        def center(self):
            screen = QtGui.QDesktopWidget().screenGeometry()  # 屏幕分辨率
            size = self.geometry() # 窗口分辨率
            self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2) # 移动

- 标签（即窗口上的固定字符串），QtGui.QLabel

        class MyWindow(QtGui.QWidget):
            def __init__(self):
                super(MyWindow, self).__init__()  # 与QtGui.QWidget.__init__(self)效果一样，好处是改变父类时不用改这个语句
                self.setWindowTitle("PYQT")
                self.resize(200, 300)
                
                label = QtGui.QLabel('label')
                label.setAlignment(QtCore.Qt.AlignCenter)
                self.setCentralWidget(label)

                # 与QtCore.Qt.AlignCenter类似的还有AlignBottom, AlignLeft, AlignRight, AlignTop, AlignHCenter, AlignVCenter...

- 布局，QtGui.QGridLayout，QtGui.QHBoxLayout，QtGui.QVBoxLayout

    QGridLayout可以按相对坐标指定widgets的位置，其余两个只能沿单一方向addWidget

    注意一定要self.setLayout

       class MyWindow(QtGui.QWidget):
            def __init__(self):
                super(MyWindow, self).__init__()
                self.setWindowTitle("PYQT")
                self.resize(500, 500)
                # self.setGeometry(30, 40, 100, 30) # 前两个数字为左上角坐标，后两个数字为长和宽
                
                label1 = QtGui.QLabel('label1') # (u'你好')
                label2 = QtGui.QLabel('label2')
                label3 = QtGui.QLabel('label3')
                label4 = QtGui.QLabel('label4')
                
                gridLayout = QtGui.QGridLayout()
                gridLayout.addWidget(label1, 0, 0)
                gridLayout.addWidget(label2, 0, 2)
                gridLayout.addWidget(label3, 1, 0)
                gridLayout.addWidget(label4, 2, 1)
                self.setLayout(gridLayout)

                # hBoxLayout = QtGui.QHBoxLayout()
                # hBoxLayout.addWidget(label)
                # self.setLayout(hBoxLayout)

                # vBoxLayout = QtGui.QVBoxLayout()
                # vBoxLayout.addWidget(label)
                # self.setLayout(vBoxLayout)

- 按钮，QtGui.QPushButton

        button1 = QtGui.QPushButton('button1')
        button2 = QtGui.QPushButton('button2')
        button2.setFlat(1) # setFlat表示未按下时是否显示为按钮样式
        button2.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold)) # 字体
        
        gridLayout.addWidget(button1, 0, 0, 1, 3)
        gridLayout.addWidget(button2, 1, 2)
        # 后四个参数分别为row, column, rowSpan, columnSpan

- 占位符，Qt.QSpacerItem

        spacer = QtGui.QSpacerItem(200, 80)
        gridlayout.addItem(spacer, 3, 1, 1, 5)
        # 后四个参数分别为row, column, rowSpan, columnSpan

- 文本输入框，QtGui.QLineEdit()，QtGui.QTextEdit()

        textFile = QtGui.QLineEdit() # 单行
        gridLayout.addWidget(textFile)
        
        passwordFile = QtGui.QLineEdit()
        passwordFile.setEchoMode(QtGui.QLineEdit.Password) # 隐藏输入
        gridLayout.addWidget(passwordFile)
        
        textArea = QtGui.QTextEdit() # 多行
        textArea.setText("preset text")
        gridLayout.addWidget(textArea)
                
- 单选和复选框，QRadioButton，QCheckBox

        radio1 = QtGui.QRadioButton("radio1")
        gridLayout.addWidget(radio1)
        
        radio2 = QtGui.QRadioButton("radio2")
        radio2.setChecked(True)    # 预选
        gridLayout.addWidget(radio2, 0, 1)
        
        checkbox1 = QtGui.QCheckBox("checkbox1")
        gridLayout.addWidget(checkbox1, 1, 0)
        
        checkbox2 = QtGui.QCheckBox("checkbox2")
        checkbox2.setChecked(True) # 预选
        gridLayout.addWidget(checkbox2, 1, 1)

- 信号与信号槽，connect

        self.radio = QtGui.QRadioButton("radio")
        gridLayout.addWidget(self.radio)
        
        button = QtGui.QPushButton("OK")
        self.connect(button, QtCore.SIGNAL('clicked()'), self.OnButton)
        # 将信号（按钮按下）和信号槽（OnButton方法）和连接起来
        gridLayout.addWidget(button)
        
        # self.connect(QLineEdit, QtCore.SIGNAL("returnPressed()"), QSLOT)
        # 回车信号

        self.setLayout(gridLayout)
        
        def OnButton(self):
            if self.radio.isChecked(): # 根据选框状态改变选框文字 
                self.radio.setText("here")

- 关闭窗口（ipython notebook不可用）

        button = QtGui.QPushButton("OK")
        self.connect(button, QtCore.SIGNAL("clicked()"),
                     QtGui.qApp, QtCore.SLOT("quit()"))

- 菜单栏，QtGui.QMenuBar（ipython不可用动作部分）

        menuBar = QtGui.QMenuBar(self)
        self.myQMenuBar.setFixedSize(width, 25) # 美观，宽度最好与窗口的宽度相等或略大，高度25能够正好放下字
        
        # 使用占位符，为了美观
        menu_spacer = QtGui.QSpacerItem(width, 25) # width最好比窗口宽度略小
        gridlayout.addItem(menu_spacer, 0, 0, 1, -1) # 第四个参数置-1表示延伸到最右边

        exitAction = QtGui.QAction('Exit', self) # 动作
        exitAction.triggered.connect(QtGui.qApp.quit) # 信号，也可以接自定义函数
        exitAction.setShortcut('Ctrl+Q') # 快捷键

        file_menu = menuBar.addMenu('File') # 菜单名称，中文需要加u
        file_menu.addAction(exitAction) # 添加菜单内容

- LCD数字，QtGui.QLCDNumber

        lcd = QtGui.QLCDNumber(5) # 参数表示位数

- 滑块，QtGui.QSlider
        
        slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        # slider = QtGui.QSlider(QtCore.Qt.Vertical)
        slider.setRange(0, 99) # 滑块变化范围，只接受整数
        slider.setValue(0)     # 滑块初始值

        slider.setPageStep(10) # 翻页范围
        slider.valueChanged[int].connect(some slot) # 获得滑块的值

        self.connect(slider, QtCore.SIGNAL("valueChanged(int)"),
                     lcd, QtCore.SLOT("display(int)")) # 直接connect的写法

- 图片，使用QLabel.setPixmap

        label = QtGui.QLabel()
        label.setPixmap(QtGui.QPixmap.fromImage(self.loadqimage(url...)))
        gridlayout.addWidget(label)
        
        def loadqimage(self, url):
            try:
                im_p = Image.open(url)
            except:
                raise ValueError('Invalid URL!')
            
            fs = StringIO.StringIO()
            im_p.save(fs, 'png')
            im_q = QtGui.QImage()
            im_q.loadFromData(fs.getvalue(), 'png')
            return im_q

- Matplotlib绘图，FigureCanvas
        
    参考资料：http://www.myext.cn/other/a_29050.html

        from matplotlib.figure import Figure
        from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
        import matplotlib.pyplot as plt

        figure = plt.gcf()
        canvas = FigureCanvas(figure) # 这样canvas可以当widget来用
        
        # 使用plt.plot等一系列方法进行绘图
        # 如果要重绘需要plt.gcf().clear()

        canvas.draw()

    多子图，这种方法更加robust

        figure = plt.figure() 
        self.canvas = FigureCanvas(figure)
#         self.canvas.setFixedSize(500, 500)  # 如不指定大小则自动铺满窗口
        self.sp1 = figure.add_subplot(211)
        self.sp2 = figure.add_subplot(212)
        self.draw(self.sp1, ...)

    动态绘图，利用QtCore.QThread

        class MyThread(QtCore.QThread):
            def __init__(self, MyWindow):
                super(MyThread, self).__init__()
                self.window = MyWindow
                
            # 重载方法，名字必须是run
            def run(self):
                do something

        window = MyWindow()
        window.show()

        # 或者在window中调用，以便实现更多控制
        # self.thread = MyWindow(self)
        # self.thread.start() # 可做信号槽用
        # self.thread.quit()  # 可做信号槽用

        class MyWindow(QtGui.QWidget):

            ...

            # 重载退出事件，保证thread退出
            def closeEvent(self, event):
                self.pause_flag = 1
                event.accept()

- 消息框，QtGui.QMessageBox

        # 主要用作信号槽的触发后续

        def OnButton1(self):
            QtGui.QMessageBox.about(self, "PyQt", "about")
            # 默认带OK，按下关闭，第二个参数为窗口名称，第三个参数为显示内容

        def OnButton2(self):    
            QtGui.QMessageBox.information(self, "Pyqt", "information", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            # 与上一消息框类似，不过会带information图标

        def OnButton3(self):
            r = QtGui.QMessageBox.question(self, "PyQt", "question", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No, QtGui.QMessageBox.Cancel)
            # 前三个参数类似，会带question图标
            # 后面跟的是预设按钮yes, no, cancel，实际使用中会把值返回给r，随后可以对r进行判断和处理

            if r == QtGui.QMessageBox.Yes:
                do something
            elif r == ...:
                ...

        def OnButton4(self):
            r = QtGui.QMessageBox.warning(self, "PyQT", "warning", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            # 与上一消息框类似，不过会带会带warning图标和音效

        def OnButton5(self):
            r = QtGui.QMessageBox.critical(self, "PyQT", "critical", QtGui.QMessageBox.Abort, QtGui.QMessageBox.Retry, QtGui.QMessageBox.Ignore)
            # 前三个参数类似，会带critical图标
            # 后面跟的是预设按钮abort, retry, ignore，实际使用中会把值返回给r，随后可以对r进行判断和处理

- 嵌套消息框

        class MyDialog1(QtGui.QDialog):
            def __init__(self):
                super(MyDialog1, self).__init__()

            def OnOk(self):
                self.text = self.textField.text()
                self.done(1) # 关闭，返回值
            
            def OnCancel(self):
                self.done(0) # 关闭，返回值

        class MyWindow(QtGui.QWidget):
            def __init__(self):
                super(MyWindow, self).__init__()

            def OnButton(self):
                dialog = MyDialog()
                r = dialog.exec_() # 执行，获取返回的值
                if r:
                    self.creatDialogButton.setText(dialog.text)

- 文件、字体、颜色，QtGui.QFileDialog，QtGui.QFontDialog，QtGui.QColorDialog

        def OnButton1(self):
            fileName = QtGui.QFileDialog.getOpenFileName(self, 'Open')
            if not fileName.isEmpty():
                self.setWindowTitle(fileName)    
             
        def OnButton2(self):
            font, ok = QtGui.QFontDialog.getFont()
            if ok:
                self.setWindowTitle(font.key())
         
        def OnButton3(self):
            color = QtGui.QColorDialog.getColor()
            if color.isValid():
                self.setWindowTitle(color.name())