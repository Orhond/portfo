# 10 --> 5 --> 16
# This is how the linked list looks like
# myLinkedList = {
#     'head': {
#         'value': 10,
#         'next': {
#             'value': 5,
#             'next': {
#                 'value': 16,
#                 'next': None
#             }
#         }
#     }
# }

# print(myLinkedList.values())


class LinkedList:

    def __init__(self, value):
        self.head = {'value': value, 'next': None}
        self.tail = self.head
        self.length = 1

    def append(self, value):  # proper solution
        newNode = {'value': value, 'next': None}
        self.tail['next'] = newNode  # this line updates both tail and head
        # makes tail equal to only last dict (last key-value pair)
        self.tail = newNode
        self.length += 1  # this updates length by 1

    def prepend(self, value):
        # firstNode = {'value': value, 'next': self.head} this line is the same as two lines below
        firstNode = {'value': value, 'next': None}
        firstNode['next'] = self.head
        self.head = firstNode
        self.length += 1

    def insert(self, index, value):  # need to complete this
        newNode = {'value': value, 'next': None}
        i = 0
        currentNode = self.head
        while currentNode != None:
            i += 1
            if i == index:
                currentNode['value'] = value
                self.head = currentNode
            currentNode = currentNode['next']

    def printList(self):  # this line prints all the values their order
        newlist = []
        currentNode = self.head
        while currentNode != None:
            newlist.append(currentNode['value'])
            currentNode = currentNode['next']
        print(newlist)

    def printfunc(self):
        print(self.head)
        print(self.tail)
        print(self.length)


myLinkedList = LinkedList(10)
myLinkedList.printList()
myLinkedList.append(5)
myLinkedList.printList()
myLinkedList.append(16)
myLinkedList.printList()
myLinkedList.prepend(7)
myLinkedList.printList()
myLinkedList.prepend(8)
myLinkedList.printList()
myLinkedList.insert(3, 17)
myLinkedList.printfunc()
