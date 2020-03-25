#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 12:53:13 2020

@author: anubhavsharma
"""
import random
import curses
import time 
curses.initscr()
scr=curses.newwin(20,20,0,0)
curses.noecho()
x=3
y=1
scr.addstr(y,x,"*")
scr.timeout(100)
scr.keypad(1)
#key = curses.KEY_RIGHT


class node:
    def __init__(self,y,x):
        self.y = y
        self.x = x
        self.data="*"
        self.next = None
        self.prev = None

class linklist:
    def __init__(self):
        self.head = None
        self.count=0
    def append(self, y,x):
        new_node = node(y,x)
        if self.head is None:
            self.head = new_node
            return
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = new_node
    def printl(self):
        p1 = self.head
        while p1:
            scr.addstr(p1.y,p1.x,p1.data)
            p1 = p1.next
    def delete(self):
        self.count+=1
        p = self.head
        for i in range(self.count):
            p.data=" "
            p = p.next
    def search(self,y1,x1):
        p = self.head
        flag=0
        while p.next:
            if p.y == y1 and p.x == x1 and p.data == "*":
                flag+=1
                return 1
            else:
                p = p.next
        if flag == 0:
            return 0
          
snake=linklist()
snake.append(1,1)
snake.append(1,2)
snake.append(1,3)
snake.printl()
scr.refresh()


food_y = None
food_x = None

def food():
    global food_x
    global food_y
    while food_x == None and food_y == None:
        Nfood_y = random.randint(1,19)
        Nfood_x = random.randint(1,19)              
    
        if snake.search(Nfood_y,Nfood_x):
            food_x = None 
            food_y = None
        else:
            food_y = Nfood_y
            food_x = Nfood_x

    scr.addstr(food_y,food_x,"O")
    
food()

def food_check():
    global food_x
    global food_y
    if y == food_y and x == food_x:
        return 0
    else:
        return 1
    
while y!= 0 and y!= 19 and x!= 0 and x!= 19:
   
    key = scr.getch()
 #   key = key if Nkey==-1 else Nkey
  
    if key == curses.KEY_DOWN:
        y+=1
        snake.append(y,x)
        if food_check():
           # scr.addstr(0,0,(food_check())
            snake.delete()
        else:
            food_x = None
            food_y = None
            food()
        snake.printl()
        scr.refresh()
    elif key == curses.KEY_UP:
        y-=1
        snake.append(y,x)  
        if food_check():
            snake.delete()
        else:
            food_x = None
            food_y = None
            food()
        snake.printl()
        scr.refresh()
    elif key == curses.KEY_RIGHT:
        x+=1
        snake.append(y,x)
        if food_check():
            snake.delete()
        else:
            food_x = None
            food_y = None
            food()
        snake.printl()
        scr.refresh()
    elif key == curses.KEY_LEFT:
        x-=1
        snake.append(y,x)
        if food_check():
            snake.delete()
        else:
            food_x = None
            food_y = None
            food()
        snake.printl()
        scr.refresh()

    
    
    
    
curses.echo()
curses.endwin()