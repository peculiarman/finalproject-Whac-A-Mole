# -*- coding: cp936 -*-

from myuilib import *
from gamepage import *
from helppage import *

'主界面'
 

win = myWin(title=u"打地鼠", width = 300, height=400)
win.addButton(CallButton(win, Point(150,100), label=u"开始游戏", func=Game))
win.addButton(CallButton(win, Point(150,200), label=u"帮助", func=Help))
win.addButton(QuitButton(win, Point(150,300), label=u"退出游戏"))
win.loop()
