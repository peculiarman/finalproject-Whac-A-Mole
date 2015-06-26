# -*- coding: cp936 -*-

from myuilib import *
from mouse import *
from random import *
 
class Hole():
    '''
    地洞类
    用来管理同一个洞中可能出现的地鼠地鼠
    '''
    def __init__(self, x, y, win):
        self.p = Point(x, y)
        self.win = win
        self.SumWeight = 10000
        self.mice = []
        self._addMouse(Mouse(x, y, 1, 'mouse', 10, 1, win))
        self._addMouse(Mouse(x, y, 3, 'mice', 3, 3, win))
        self._addMouse(Mouse(x, y, 1, 'mm', 4, -5, win))
        self.state = None
        self.mt = 0
        self.ft = 0
    def _addMouse(self, mouse):
        self.mice.append(mouse)
        self.SumWeight = self.SumWeight + mouse.getPw()
    def loop(self, p, Score):
        '主循环，p为鼠标指针，Score为当前分数的引用'
        if self.state == None:
            rand = randint(1,self.SumWeight)
            self.mt = randint(30, 150)
            self.ft = randint(2,10)
            for mouse in self.mice:
                if rand <= mouse.getPw():
                    self.state = mouse
                    break
                rand = rand - mouse.getPw()
        if self.state != None:
            score = self.state.loop(self.mt, self.ft, p)
            if  score == None:
                self.state = None
            elif score != 0:
                Score.inc(score)
            

#----------just for debug--------------
def _test():
    win = myWin()
    Hole(1,1,win)
    win.loop()
if __name__=='__main__':
    _test()
