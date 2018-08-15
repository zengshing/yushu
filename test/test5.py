#-*- coding:utf-8 _*-
"""
@author:star
@file: test5.py
@time: 2018/08/11
"""

import threading, time

def Seeker(cond, name):
    cond.acquire()
    print('{}: 我把眼睛蒙上了.'.format(name))
    cond.notify()
    cond.wait()
    for i in range(2):
        print('{}: is finding.'.format(name))
        time.sleep(2)
    cond.notify()
    cond.release()
    print('{}: i am winner'.format(name))

def Hider(cond, name):
    cond.acquire()
    for i in range(2):
        print('{}: is hidding'.format(name))
        time.sleep(2)
    cond.notify()
    cond.wait()
    cond.release()
    print('{}: i am loser'.format(name))

def main():
    cond = threading.Condition()
    seeker = threading.Thread(target=Seeker, args=(cond, 'seeker'))
    hider = threading.Thread(target=Hider, args=(cond, 'hidder'))
    seeker.start()
    hider.start()

if __name__ == "__main__":
    main()