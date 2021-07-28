# Given a binary tree where the value of each node is a linked list where the value of each linked list is the value of a list.
# Write a function that will return info in a tuple format.
# Return the sum of all values
# the largest value
# the smallest value
# and the further removed from 0.

# Algorithm
# function(BinaryTree)
# traverse through binary tree iteratively, not recursively
# use stack or queue, when you come across a node, do something with it, check for left or right, put it into Statck or Queue
# pop it off, see if it has a left or right, put it in the stack or queue and I got lost

# first thing, don't code it out, talk it out
# no google

# Algorithm - non-recursive
# stack method
# set a storage variable for values popped off
# counter for iteratin using a while loop

# Queue
# Define function(Tree)


def function(BinaryTree):
    queue = Queue()
    sum = 0
    min = BinaryTree.root.value.head.value[0]
    max = BinaryTree.root.value.head.value[0]
    absolute = 0
    queue.enqueue(BinaryTree.root)
    # --- Binary Tree ---
    while queue.peek():
        front = queue.dequeue()
        if front.left:
            queue.enqueue(front.left)
        if front.right:
            queue.enqueue(front.right)
        # --- Linked List ---
        current = front.value.head
        while current is not None:
            # ---- list ----
            # iterate through a list and find the values
            for number in current.value:  # do a thing
                if number > max:
                    max = number
                if number < min:
                    min = number
                if abs(number) > absolute:
                    absolute = number
                sum += number

            for i in current.value:
                sum = sum + i
                current = current.next
    return (sum, min, max, absolute)

    # iterate through list
    # check values in list and find the sum, max, min, absolute value(furthest removed from 0, can be negative numbers)
    # current = current.next

    # now start looking at the value of the front
    # start looking at the linked list portion of our value
    # iterate through the linked list and grab every list value
    # then iterate through the list
    # ---- Algorithm for linked list ----
    # front.value points to a linked list

    # Iterate through the linked list


# front.value points to a linked lint
# while LookupError
# set a temp variable to frpn.

# current = head.next
# set a current variable to front.value
# while loop, whoile current is not None
# reassign the current variable to current.next
