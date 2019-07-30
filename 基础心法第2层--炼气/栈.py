'''
顺序栈
基于数组实现的栈
'''
# class ListStack:
#     def __init__(self):
#         self.arraylist = []

#     def push(self, item):
#         self.arraylist.append(item)

#     def pop(self):
#         self.arraylist.pop()

# s = Stack()
# s.push('1')
# s.push('2')
# s.push('3')
# print(s.arraylist)
# s.pop()
# print(s.arraylist)

'''
基于链表实现的栈

Author: YUYI
'''
class Node:

    def __init__(self, data: int, next = None):
        self._data = data
        self._next = next
        

class LinkedStack:

    def __init__(self):
        self._top: Node = None
        
    def push(self, value: int):
        new_top = Node(value)
        new_top._next = self._top
        self._top = new_top

    def pop(self):
        if self._top:
            value = self._top._data
            self._top = self._top._next
            return value
    
    def __repr__(self) -> str:
        current = self._top
        nums = []
        while current:
            nums.append(current._data)
            current = current._next
        return "".join(f"{num}]" for num in nums)

if __name__ == "__main__":
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    print(stack)
    for _ in range(3):
        stack.pop()
    print(stack)

