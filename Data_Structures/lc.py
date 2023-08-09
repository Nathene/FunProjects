import random
## Nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.left = None
        self.right = None

def create_linked_list():
    head = Node(1)
    curr = head
    rand_num = 0
    while True:
        rand_num -= 1
        if rand_num < 0:
            break
        new_node = Node(random.randint(1, 100))
        curr.next = new_node
        curr = curr.next
    return head

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.data, end=' -> ')
        curr = curr.next
    idx = 1
    len_list = list_length
    while len_list > 0:
        print(idx, end=' --- ')
        len_list -= 1
        idx += 1
    print("\n")

def delete_node(data, head):
    curr = head
    prev = None
    while curr:
        if curr.data == data:
            if prev:
                prev.next = curr.next
            else:
                head = curr.next
            break
        prev = curr
        curr = curr.next
    return head



## stacks
def print_stack(stack):
    print(stack)
    return stack

def create_stack():
    stack = [1, 2, 3, 4, 5]
    return stack

## queues
def print_queue(queue):
    print(queue)
    return queue

def create_queue():
    queue = [1, 2, 3, 4, 5]
    return queue

## trees
def print_tree(head):
    curr = head
    output = input("There are many ways to show a tree, which one would you like to see?\n 1. Preorder\n 2. Inorder\n 3. Postorder\n")
    if output == "1":
        pre_order(curr)
    elif output == "2":
        in_order(curr)
    elif output == "3":
        post_order(curr)
    else:
        print("Invalid choice")
    print("\n")

def create_tree():
    head = Node(1)
    curr = head
    rand_num = 7
    hi = 1
    while True:
        if rand_num < 0:
            break
        new_left = Node(random.randint(1, 100))
        new_right = Node(random.randint(1, 100))
        curr.left = new_left
        curr.right = new_right
        if hi == 1:
            hi = 0
            continue
        if rand_num % 2 == 0:
            curr.left.left = new_left
            curr.left.right = new_right
        else:
            curr.right.right = new_right
            curr.right.left = new_left

        rand_num -= 1

    return head

def pre_order(curr):
    if curr:
        print(curr.data, end=' -> ')
        pre_order(curr.left)
        pre_order(curr.right)

def in_order(curr):
    if curr:
        in_order(curr.left)
        print(curr.data, end=' -> ')
        in_order(curr.right)

def post_order(curr):
    if curr:
        post_order(curr.left)
        post_order(curr.right)
        print(curr.data, end=' -> ')

def main():
    head = create_linked_list()
    global list_length
    list_length = 1
    while True:
        choice = input("Which Data structure do you want to use?\n"
                    "1. Linked List\n"
                    "2. Stack\n"
                    "3. Queue\n"
                    "4. Tree\n"
                    "5. Graph\n"
                    "6. Heap\n"
                    "7. Trie\n\n")
        if choice == "1":
            while True:
                print("=== Here is the the Linked List ===\n")
                print_linked_list(head)
                action = input("What do you want to do with the Linked List?\n"
                        "1. Insert\n"
                        "2. Delete\n")
                if action == "1":
                    list_length += 1
                    add_node_choice = input("How many nodes into the list do you want to put it?\n\n")
                    add_node_choice = int(add_node_choice)
                    curr = head
                    if add_node_choice == 0:
                        tmp_node = Node(random.randint(1, 100)) 
                        tmp_node.next = head
                        head = tmp_node
                    while add_node_choice > 0:
                        if not curr.next:
                            curr.next = Node(random.randint(1, 100))
                            break
                        if add_node_choice == 1:
                            new_node = Node(random.randint(1, 100))
                            new_node.next = curr.next
                            curr.next = new_node
                            break
                        curr = curr.next
                        add_node_choice -= 1
                        

                elif action == "2":
                    list_length -= 1
                    print("Delete a node from the Linked List\n\n")
                    print_linked_list(head)
                    choice = input("which node would you like to delete?\n")
                    head = delete_node(int(choice), head)
                else:
                    break
                continue
                    
        elif choice == "2":
            stack = create_stack()
            while True:
                print_stack(stack)
                choice = input("1. Push\n2. Pop\n") 
                if choice == "1":
                    # number = input("What number would you like to add to the stack?\n")
                    stack.append(random.randint(1, 70))

                elif choice == "2":
                    stack.pop()
                else:
                    break

        elif choice == "3":
            queue = create_queue()
            while True:
                print_queue(queue)
                choice = input("1. Enqueue\n2. Dequeue\n")
                if choice == "1":
                    queue.append(random.randint(1, 70))
                elif choice == "2":
                    queue.pop(0)
                else:
                    break
        elif choice == "4":
            head = create_tree()
            while True:
                print_tree(head)

        elif choice == "5":
            print("Graph")
        elif choice == "6":
            print("Heap")
        elif choice == "7":
            print("Trie")
        else:
            print("Cya!\n")
            break

if __name__ == '__main__':
    main()
