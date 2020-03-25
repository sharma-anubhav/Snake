#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:04:47 2020

@author: anubhavsharma
"""

class node:
    def __init__(self,y,x):
        self.y = y
        self.x = x
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
            print(p1.y) 
            print(p1.x)
            p1 = p1.next
    def delete(self):
        self.count+=1
        p = self.head
        for i in range(self.count):
            p.y="*"
            p.x="*"
            p = p.next
        
    

snake=linklist()
snake.append(1,1)
snake.append(2,2)
snake.append(3,3)
snake.delete()
snake.delete()
snake.printl()



    