# -*- coding: cp936 -*-

from myuilib import *


 

def Help():
    '����ҳ��'
    win = myWin(title=u"����� - ����")
    image = Image(Point(400,300),'gif\\help.gif')
    if win.isOpen():
        image.draw(win)
    win.addButton(QuitButton(win, Point(750,580),label=u"�������˵�"))
    win.loop()

#----------just for debug--------------
if __name__ == '__main__':
    Help()
