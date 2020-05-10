class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def PalindromeOrnot(self,string):
        return (string==string[::-1])
    def isPalindrome(self):
        node = self.head
        temp = []
        while (node is not None):
            temp.append(node.data)
            node = node.next
        string = " ".join(temp)
        print(string)
        return self.PalindromeOrnot(string)


    def Listprint(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    list = LinkedList()
    list.head = Node('1')
    l1 = Node('2')
    l2 = Node('2')
    l3 = Node('1')

    list.head.next = l1
    l1.next = l2
    l2.next = l3
    if list.isPalindrome():
        print ("true")
    else:
        print("false")


