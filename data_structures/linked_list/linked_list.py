#!/usr/bin/env python3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
  
    def add(self,data):
        N1 = Node(data)
        N1.next = self.head
        self.head = N1


    def addtoend(self,data):
        newelement = Node(data)
        if self.head is None:
            self.head = newelement
            self.tail = newelement
            return
        lastelement = self.tail
        lastelement.next = newelement
        self.tail = newelement


    def addtosecond(self,data):
        newelement = Node(data)
        if self.head is None:
            self.head = newelement
            return
        secondelement = self.head.next
        self.head.next = newelement
        newelement.next = secondelement
        return

# deletefirst - method to delete first element
    def deletefirst(self):
        if self.head is None:
            return None
        if self.head:
            deleted_element = self.head
            self.head = deleted_element.next
            return deleted_element

    def __str__(self):
        current = self.head
        output = ""
        while current:
            output += str(current.data) + " -> "
            current = current.next
        return output[:-4]
