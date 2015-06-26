# -*- coding: cp936 -*-

from graphics import *
from random import *
import time
import button

class myWin(GraphWin):
    '''
    窗口类
    继承自Graphics.GraphWin，
    增加一些默认参数(见构造函数)，
    增加hide()和show()方法
    loop()模拟消息循环
    '''
    def __init__(self, title="",
                 width=800, height=600, autoflush=True):
        '默认大小800x600，初在屏幕左上角，创建窗口时窗口置顶'
        GraphWin.__init__(self, title, width, height, autoflush)
        self.buttonlist = []
        self.master.resizable ( width=False, height=False )
        self.master.lift()
        self.master.geometry(str(width)+'x'+str(height)+\
                             '+'+str((800-width)/2)+'+'+str((600-height)/2))
    
    def addButton(self, button):
        '给窗口增加一个button'
        self.buttonlist.append(button)

    def hide(self):
        '隐藏窗口'
        self.master.withdraw()

    def show(self):
        '显示窗口'
        self.master.deiconify()

    def loop(self):
        '模拟消息循环，相应self.buttonlist中的button的点击'
        while self.isOpen():
            if self.isClosed():
                self.show()
            p=self.checkMouse()
            if p!=None:
                for button in self.buttonlist:
                    if button.clicked(p):
                        button.func()
                    
class flashText(Text):
    '''
    闪动文字，可在屏幕闪现一定时间后消失
    继承自graphics.Text
    增加默认参数
    增加方法flash()
    '''
    def __init__(self, text, color):
        '初始大小36，初始加粗斜体，增加color参数'
        Text.__init__(self, Point(400, 300), text)
        self.setSize(36)
        self.setTextColor(color)
        self.setStyle('bold italic')
    def flash(self, win, t):
        '在win窗口中出现t秒后消失'
        if win.isOpen():
            self.draw(win)
        t = t*100
        x = 1
        while x<=t and win.isOpen():
            time.sleep(0.01)
            x = x+1
        self.undraw()
        
class NumText(Text):
    '''
    数字文本，用来显示文本或数字
    继承自graphics.Text
    增加默认参数
    增加方法inc(),dec()
    重命名update=setText, get=getText
    '''
    def __init__(self, p, text, color='yellow'):
        '默认颜色黄色，初始大小30，初始加粗'
        Text.__init__(self, p, text)
        self.setSize(30)
        self.setTextColor('yellow')
        self.setStyle('bold')
    def inc(self, w=1):
        '自加w'
        self.setText(self.getText()+w)
    def dec(self, w=1):
        '自减w'
        self.setText(self.getText()-w)
    def update(self, text):
        self.setText(text)
    def get(self):
        return self.getText()

class Button(button.Button):
    '''
    按钮类
    重载button.Button
    增加默认高宽
    绑定函数func
    '''
    def __init__(self, win, center, width=100, height=40, label="", func=None):
        button.Button.__init__(self, win, center, width, height, label)
        self.win = win
        self.func = func or self.nofunc
        self.activate()
    def nofunc(self):
        return
        
 
class CallButton(Button):
    '功能为调用新窗口的按钮'
    def __init__(self, win, center, width=100, height=40, label="", func=None):
        Button.__init__(self, win, center, width, height, label)
        self.func = self.callfunc
        self.subcall = func or self.nofunc
    def callfunc(self):
        self.win.hide()
        self.subcall()
        self.win.show()
        

class QuitButton(Button):
    '功能为关闭窗口的按钮'
    def __init__(self, win, center, width=100, height=40, label=u"退出"):
        Button.__init__(self, win, center, width, height, label, win.close)




#----------just for debug--------------
def _test():
    def f():
        nT.dec(5)
        print('clicked')
    def callf():
        win=myWin("sub")
        win.addButton(QuitButton(win,Point(100,100)))
        win.loop()
    win=myWin("main")
    rT=readyText('Ready?\n3','yellow')
    nT=NumText(Point(50,20),30)
    rT.draw(win)
    nT.draw(win)
    win.addButton(QuitButton(win,Point(300,200)))
    win.addButton(CallButton(win,Point(200,200), label="start", func=callf))
    win.addButton(Button(win,Point(100,200), label="click", func=f))
    win.loop()

if __name__=="__main__":
    _test()
