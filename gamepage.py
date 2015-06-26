# -*- coding: cp936 -*- 

from myuilib import *
from mouse import *
from hole import *
from time import *
from random import *

def Game():
    '��Ϸҳ��'
    seed = time()
    win = myWin(title=u"����� - ������Ϸ")
    bg = Image(Point(400,300),'gif\\bg.gif')
    bg.draw(win)
    win.addButton(QuitButton(win, Point(750,580),label=u"�������˵�"))
    Ready3 = flashText('Ready?\n3','yellow')
    Ready2 = flashText('Ready?\n2','yellow')
    Ready1 = flashText('Ready?\n1','yellow')
    Go = flashText('Go!','blue')
    maxTime = 60
    TimeText = NumText(Point(50,30),u'ʱ��')
    Time = NumText(Point(150,30), maxTime)
    ScoreText = NumText(Point(650,30),u'����')
    Score = NumText(Point(750,30), 0)
    if win.isOpen():
        TimeText.draw(win)
        ScoreText.draw(win)
        Time.draw(win)
        Score.draw(win)
        Ready3.flash(win,1)
        Ready2.flash(win,1)
        Ready1.flash(win,1)
        Go.flash(win,1)
    holes=[]
    holes.append(Hole(277,150, win))
    holes.append(Hole(650,98, win))
    holes.append(Hole(131,279, win))
    holes.append(Hole(495,236, win))
    holes.append(Hole(365,328, win))
    holes.append(Hole(678,370, win))
    holes.append(Hole(234,452, win))
    st = time()
    while win.isOpen() and Time.get()>0:
        p = win.checkMouse()
        for hole in holes:
            hole.loop(p, Score)
        sleep(0.01)
        now = time()
        Time.update(maxTime-int(now-st))
        if p!=None:
            for button in win.buttonlist:
                if button.clicked(p):
                    button.func()
    GameOver = NumText(Point(400,300),u'��Ϸ������\n��ĵ÷���'+str(Score.get()))
    if win.isOpen():
        GameOver.draw(win)
    win.loop()

def _test():
    Game()

if __name__=="__main__":
    _test()

