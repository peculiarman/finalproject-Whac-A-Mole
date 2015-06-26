# -*- coding: cp936 -*-

from graphics import *
from random import *
import time
import button

class myWin(GraphWin):
    '''
    ������
    �̳���Graphics.GraphWin��
    ����һЩĬ�ϲ���(�����캯��)��
    ����hide()��show()����
    loop()ģ����Ϣѭ��
    '''
    def __init__(self, title="",
                 width=800, height=600, autoflush=True):
        'Ĭ�ϴ�С800x600��������Ļ���Ͻǣ���������ʱ�����ö�'
        GraphWin.__init__(self, title, width, height, autoflush)
        self.buttonlist = []
        self.master.resizable ( width=False, height=False )
        self.master.lift()
        self.master.geometry(str(width)+'x'+str(height)+\
                             '+'+str((800-width)/2)+'+'+str((600-height)/2))
    
    def addButton(self, button):
        '����������һ��button'
        self.buttonlist.append(button)

    def hide(self):
        '���ش���'
        self.master.withdraw()

    def show(self):
        '��ʾ����'
        self.master.deiconify()

    def loop(self):
        'ģ����Ϣѭ������Ӧself.buttonlist�е�button�ĵ��'
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
    �������֣�������Ļ����һ��ʱ�����ʧ
    �̳���graphics.Text
    ����Ĭ�ϲ���
    ���ӷ���flash()
    '''
    def __init__(self, text, color):
        '��ʼ��С36����ʼ�Ӵ�б�壬����color����'
        Text.__init__(self, Point(400, 300), text)
        self.setSize(36)
        self.setTextColor(color)
        self.setStyle('bold italic')
    def flash(self, win, t):
        '��win�����г���t�����ʧ'
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
    �����ı���������ʾ�ı�������
    �̳���graphics.Text
    ����Ĭ�ϲ���
    ���ӷ���inc(),dec()
    ������update=setText, get=getText
    '''
    def __init__(self, p, text, color='yellow'):
        'Ĭ����ɫ��ɫ����ʼ��С30����ʼ�Ӵ�'
        Text.__init__(self, p, text)
        self.setSize(30)
        self.setTextColor('yellow')
        self.setStyle('bold')
    def inc(self, w=1):
        '�Լ�w'
        self.setText(self.getText()+w)
    def dec(self, w=1):
        '�Լ�w'
        self.setText(self.getText()-w)
    def update(self, text):
        self.setText(text)
    def get(self):
        return self.getText()

class Button(button.Button):
    '''
    ��ť��
    ����button.Button
    ����Ĭ�ϸ߿�
    �󶨺���func
    '''
    def __init__(self, win, center, width=100, height=40, label="", func=None):
        button.Button.__init__(self, win, center, width, height, label)
        self.win = win
        self.func = func or self.nofunc
        self.activate()
    def nofunc(self):
        return
        
 
class CallButton(Button):
    '����Ϊ�����´��ڵİ�ť'
    def __init__(self, win, center, width=100, height=40, label="", func=None):
        Button.__init__(self, win, center, width, height, label)
        self.func = self.callfunc
        self.subcall = func or self.nofunc
    def callfunc(self):
        self.win.hide()
        self.subcall()
        self.win.show()
        

class QuitButton(Button):
    '����Ϊ�رմ��ڵİ�ť'
    def __init__(self, win, center, width=100, height=40, label=u"�˳�"):
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
