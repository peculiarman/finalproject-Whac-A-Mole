# -*- coding: cp936 -*-

from myuilib import *

class Mouse():
    '''
    ������ 
    3֡ģ���������������ȥ�Ķ���
    ��self.state��ʾ����״̬��
    self.stateΪ����ʾ����Ϊ0��ʾû�г���
    '''
    def __init__(self, x, y, clickneed, f, weight, score, win):
        '�������壺�е�����꣬�����꣬��Ҫ�㼸�¿��Դ������ļ���������Ȩ�أ��÷֣���ʾ�Ĵ���'
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
        '���ظ���Ȩ��'
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
        '��ѭ����mtΪ��ʾʱ��(��λ0.01s)��ftΪ���ֺ���ʧ�ٶȣ�pΪ���'
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
