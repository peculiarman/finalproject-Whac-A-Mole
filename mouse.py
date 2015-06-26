# -*- coding: cp936 -*-

from myuilib import *

class Mouse():
    '''
    地鼠类 
    3帧模拟地鼠钻出来和钻回去的动画
    用self.state表示动画状态，
    self.state为负表示被打，为0表示没有出来
    '''
    def __init__(self, x, y, clickneed, f, weight, score, win):
        '参数意义：中点横坐标，纵坐标，需要点几下可以打死，文件名，概率权重，得分，显示的窗口'
        self.x = x
        self.y = y
        self.LT = Point(x-60, y-80)
        self.RB = Point(x+60, y+80)
        self.Pw = weight
        self.score = score
        self.win = win
        self.img0 = Image(Point(x,y), 'gif\\nomouse.gif')
        self.img1 = Image(Point(x,y), 'gif\\'+f+'_1.gif')
        self.img2 = Image(Point(x,y), 'gif\\'+f+'_2.gif')
        self.img3 = Image(Point(x,y), 'gif\\'+f+'_3.gif')
        self.img1x = Image(Point(x,y), 'gif\\'+f+'_1_x.gif')
        self.img2x = Image(Point(x,y), 'gif\\'+f+'_2_x.gif')
        self.img3x = Image(Point(x,y), 'gif\\'+f+'_3_x.gif')
        self.img = self.img0
        if win.isOpen():
            self.img.draw(win)
        self.state = 0
        self.clickneed = clickneed
        self.click = 0
        self.time = 0
    def getPw(self):
        '返回概率权重'
        return self.Pw
    def _changestate(self, state):
        self.state = state
        self.img.undraw()
        if state == 0:
            self.img = self.img0
        elif state == 1:
            self.img = self.img1
        elif state == 2:
            self.img = self.img2
        elif state == 3:
            self.img = self.img3
        elif state == -1:
            self.img = self.img1x
        elif state == -2:
            self.img = self.img2x
        elif state == -3:
            self.img = self.img3x
        if self.win.isOpen():
            self.img.draw(self.win)
        if state == 0:
            self.click = 0
        if state <= 0:
            self.time = 0
    def _actived(self):
        return self.state!=0
    def _clicked(self, p):
        return self._actived() and p!=None and\
               self.LT.x <= p.getX() <= self.RB.x and\
               self.LT.y <= p.getY() <= self.RB.y
    def loop(self, mt, ft, p):
        '主循环，mt为显示时间(单位0.01s)，ft为出现和消失速度，p为鼠标'
        if self.state>0:
            if self._clicked(p):
                self.click = self.click + 1
            if self.click == self.clickneed:
                self._changestate(-self.state)
                return self.score*(4-(-self.state))
        if self.state == 0:
            self._changestate(1)
        self.time = self.time+1
        if self.state == 1:
            if self.time == ft:
                self._changestate(2)
            if self.time == mt + ft*4:
                self._changestate(0)
                return
        elif self.state == 2:
            if self.time == ft*2:
                self._changestate(3)
            if self.time == mt + ft*3:
                self._changestate(1)
        elif self.state == 3:
            if self.time > mt + ft*2:
                self._changestate(2)
        elif self.state < 0:
            if self.time > 100:
                self._changestate(0)
                return
        return 0


#----------just for debug--------------
def _test():
    win = myWin()
    Mouse(1,1,1,'mouse',1,1,win)
    win.loop()
if __name__=='__main__':
    _test()
