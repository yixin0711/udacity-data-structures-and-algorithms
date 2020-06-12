class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = []
        while cur_head:
            out_string.append(str(cur_head.value))
            cur_head = cur_head.next
        return "->".join(out_string)


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    
    if llist_1.size() == 0 and llist_2.size() == 0:
        print("Both Linked List are Empty. \n No Union List Can Be Found.")
        return None

    if llist_1.size() == 0:
        return llist_2
    elif llist_2.size() == 0:
        return llist_1


    head1 = llist_1.head
    head2 = llist_2.head
    
    union_llist = LinkedList()
    
    hash_table = {}
    while head1 != None:
        if head1.value not in hash_table:
            union_llist.append(head1.value)
            hash_table[head1.value] = head1.next
        head1 = head1.next
        
    while head2 != None:
        if head2.value not in hash_table:
            hash_table[head2.value] = head2.next
            union_llist.append(head2.value)
        head2 = head2.next
    
    return union_llist

def intersection(llist_1, llist_2):

    if llist_1.size() == 0 or llist_1.size() == 0:
        print("At Least One Empty Linked List Inserted. \nNo intersection found.")
        return None

    head1 = llist_1.head
    head2 = llist_2.head
    
    intersect_llist = LinkedList()
    
    hash_table = {}
    while head1 != None:
        if head1.value not in hash_table:
            hash_table[head1.value] = head1.next
        head1 = head1.next
    while head2 != None:
        if head2.value in hash_table:
            intersect_llist.append(head2.value)
            hash_table.pop(head2.value)
        head2 = head2.next
        
    return intersect_llist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

union_llist = LinkedList()
inter_llist = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

union_set = list((set(element_1) | set(element_2)))
inter_set = list((set(element_1) & set(element_2)))

for i in union_set:
    union_llist.append(i)
    
for i in inter_set:
    inter_llist.append(i)
    

print("==========TEST 1==========")
print("List 1: ", element_1)
print("List 2: ", element_2)
print("=======Union of Two Linked List=======")
print("My answer: ", union(linked_list_1,linked_list_2))
print("Correct answer: ", union_set)

print("=======Intersection of Two Linked List=======")
print("My answer: ", intersection(linked_list_1,linked_list_2))
print("Correct answer: ", inter_set)

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

union_llist = LinkedList()
inter_llist = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

union_set = list((set(element_1) | set(element_2)))
inter_set = list((set(element_1) & set(element_2)))       #should be no intersection

for i in union_set:
    union_llist.append(i)
    
for i in inter_set:
    inter_llist.append(i)
    
print("==========TEST 2==========")
print("List 1: ", element_1)
print("List 2: ", element_2)
print("=======Union of Two Linked List=======")
print("My answer: ", union(linked_list_3,linked_list_4))
print("Correct answer: ", union_set)

print("=======Intersection of Two Linked List=======")
print("My answer: ", intersection(linked_list_3,linked_list_4))
print("Correct answer: ", inter_set)


# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

union_llist = LinkedList()
inter_llist = LinkedList()

element_1 = []      #corner case 1, one empty list
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

union_set = list((set(element_1) | set(element_2)))
inter_set = list((set(element_1) & set(element_2)))

for i in union_set:
    union_llist.append(i)
    
for i in inter_set:
    inter_llist.append(i)
    
print("==========TEST 3==========")
print("List 1: ", element_1)
print("List 2: ", element_2)
print("=======Union of Two Linked List=======")
print("My answer: ", union(linked_list_5,linked_list_6))
print("Correct answer: ", union_set)

print("=======Intersection of Two Linked List=======")
print("My answer: ", intersection(linked_list_5,linked_list_6))
print("Correct answer: ", inter_set)

# Test case 4

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

union_llist = LinkedList()
inter_llist = LinkedList()

element_1 = []      #corner case 2, both empty list
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

union_set = list((set(element_1) | set(element_2)))
inter_set = list((set(element_1) & set(element_2)))  

for i in union_set:
    union_llist.append(i)
    
for i in inter_set:
    inter_llist.append(i)
    
print("==========TEST 4==========")
print("List 1: ", element_1)
print("List 2: ", element_2)
print("=======Union of Two Linked List=======")
print("My answer: ", union(linked_list_7,linked_list_8))
print("Correct answer: ", union_set)

print("=======Intersection of Two Linked List=======")
print("My answer: ", intersection(linked_list_7,linked_list_8))
print("Correct answer: ", inter_set)