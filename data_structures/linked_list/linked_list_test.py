#!/usr/bin/env python3

import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    
        def test_add(self):
            ll = LinkedList()
            ll.add(1)
            self.assertEqual(ll.head.data, 1)
            ll.add(2)
            self.assertEqual(ll.head.data, 2)
    
        def test_addtoend(self):
            ll = LinkedList()
            ll.addtoend(1)
            self.assertEqual(ll.head.data, 1)
            ll.addtoend(2)
            self.assertEqual(ll.head.data, 1)
            self.assertEqual(ll.head.next.data, 2)
    
        def test_addtosecond(self):
            ll = LinkedList()
            ll.add(1) # 1
            ll.add(2) # 2 -> 1
            ll.addtosecond(3) # 2 -> 3 -> 1
            self.assertEqual(ll.head.data, 2)
            self.assertEqual(ll.head.next.data, 3)
            self.assertEqual(ll.head.next.next.data, 1)

        def test_str(self):
            ll = LinkedList()
            ll.add(1)
            ll.add(2)
            ll.add(3)
            self.assertEqual(str(ll), "3 -> 2 -> 1")

        def test_deletefirst(self):
            ll = LinkedList()
            ll.add(1)
            ll.add(2)
            ll.add(33)
            ll.deletefirst() # 2 -> 1
            self.assertEqual(ll.head.data, 2)
            self.assertEqual(ll.head.next.data, 1)
if __name__ == '__main__':
    unittest.main()
        
