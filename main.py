# -*- coding: cp936 -*-

from myuilib import *
from gamepage import *
from helppage import *

'������'
 

win = myWin(title=u"�����", width = 300, height=400)
win.addButton(CallButton(win, Point(150,100), label=u"��ʼ��Ϸ", func=Game))
win.addButton(CallButton(win, Point(150,200), label=u"����", func=Help))
win.addButton(QuitButton(win, Point(150,300), label=u"�˳���Ϸ"))
win.loop()
