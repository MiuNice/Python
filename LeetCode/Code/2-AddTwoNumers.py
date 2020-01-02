"""
    2-AddTwoNumber.py 两数相加
    给定两个非空 链表(linked list) ，表示两个非负整数。
    存储方式为逆存储，切一个节点只能存储一位数字。返回两数相加 逆存储链表。
    例：
        [1 -> 2 -> 3] +  [4 -> 5 -> 6]
        = 321 + 654
        = 975
        return [5 -> 7 -> 9] 
"""

class Node:
    def __init__(self, vaule):
        self.value = vaule
        self.next = None

class LinkedList:
    def __init__(self):
        self.header = None
    
    def init_linklist(self, data):
        self.header = Node(data[0])
        p = self.header
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = node
        return self.display_Link_list()
    
    def display_Link_list(self):
        temp = []
        cur = self.header
        while cur:
            temp.append(cur)
            cur = cur.next
        return temp

def addTwoNumbers(l1 : LinkedList, l2 : LinkedList) -> LinkedList:
    for i in l1:
        print(i)
    print(l2)


if __name__ == "__main__":
    linklist = LinkedList()
    addTwoNumbers(linklist.init_linklist([1, 2, 3]), linklist.init_linklist([4, 5, 6]))