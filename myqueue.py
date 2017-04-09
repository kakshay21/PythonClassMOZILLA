#!/usr/bin/python
class Queue:
    def __init__(self):
        self.queueList=[]

    def isEmpty(self):
        return (self.queueList==[])

    def insert(self,item):
        self.queueList.insert(0,item)

    def pop(self):
        return self.queueList.pop()