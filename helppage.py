# -*- coding: cp936 -*-

from myuilib import *


 

def Help():
    '帮助页面'
    win = myWin(title=u"打地鼠 - 帮助")
    image = Image(Point(400,300),'gif\\help.gif')
    if win.isOpen():
        image.draw(win)
    win.addButton(QuitButton(win, Point(750,580),label=u"返回主菜单"))
    win.loop()

#----------just for debug--------------
if __name__ == '__main__':
    Help()
