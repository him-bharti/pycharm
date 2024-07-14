# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""def addnum(list,k):
    list1 = sorted(list)
    i = 0
    while i < len(list1):
        for j in range(i+1,len(list1)):
            if list1[i]+list1[j] == k:
                return list1[i],list1[j]

        i = i+1

print(addnum([10,15,3,7],22))"""

# ----------------------------------x-------------------------------------------------

# This problem was asked by Uber.
# Given an array of integers, return a new array such that each
# element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5],
# the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

"""def product(list):
    prod = 1
    for num in list:
        prod = prod * num

    list1 = []
    for i in list:
        list1.append(prod//i)
    return list1

list = [1,2,3,4,5]

print(product(list))"""

# ----------------------------------x-------------------------------------------------

# This problem was recently asked by Google.
# Given the root to a binary tree, implement serialize(root),
# which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
# For example, given the following Node class
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

"""class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(Node):
    elements = []

    elements.append(Node.val)

    if Node.left:
        elements = elements + serialize(Node.left)

    if Node.right:
        elements = elements + serialize(Node.right)

    return elements


node = Node('root', Node('left', Node('left.left')), Node('right'))
list = serialize(node)
print(list)"""

# ----------------------------------x-------------------------------------------------

# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place

"""def find_mis_pos_int(list):
    list = set(list)
    sum = 0
    for i in list:
        if i > 0:
            sum = sum + i
    sortedlist = sorted(list)
    n = sortedlist[-1]
    sum1 = n*(n+1)/2
    diff = sum1 - sum
    if diff > 0:
        print(diff)
    else:
        print(n+1)
find_mis_pos_int([3, 4, -1, 1])"""

# ----------------------------------x-------------------------------------------------

# This problem was asked by Jane Street.
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
# Given this implementation of cons:
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# Implement car and cdr.

"""def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

my_pair = cons(2, 3)

def get_first(a, b):
    return a

def get_second(a, b):
    return b

first_element = my_pair(get_first)
second_element = my_pair(get_second)

print(first_element)
print(second_element)"""

# ----------------------------------x-------------------------------------------------

# This problem was asked by Google.
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

"""class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    def is_unival(self):
        if self.val is None:
            return True
        if self.left.val is not None and self.left.val != self.val:
            return False
        if self.right.val is not None and self.right.val != self.val:
            return False
        if self.left.is_unival and self.right.is_unival :
            return True
        return False

    def count_unival_node(self):

        if self.val is None:
            return 0
        if self.left is None and self.right is None:
            return 1

        total = self.left.count_unival_node() + self.right.count_unival_node()

        if self.is_unival():
            total = total + 1
        return total

a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.right = Node(0)
a.right.left = Node(1)
a.right.left.right = Node(1)
a.right.left.left = Node(1)

#print(a.right.left.is_unival())
print(a.count_unival_node())"""

# ----------------------------------x-------------------------------------------------

# This problem was asked by Twitter.
# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix.
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

"""abc = ['dog', 'deer', 'deal']
temp = []
query = str(input('enter the query string:'))
for i in abc:
    if query in i:
        temp.append(i)
print(temp)"""

# ----------------------------------x-------------------------------------------------

# This problem was asked by Amazon.
# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function
# that returns the number of unique ways you can climb the staircase. The order of the steps matters.
# For example, if N is 4, then there are 5 unique ways:
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive
# integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

"""def steps(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return steps(n-1) + steps(n-2)

print(steps(4))"""

# ----------------------------------x-------------------------------------------------
# This problem was asked by Amazon.
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct character
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb"

"""def substring(string,k):
    if len(string) == k:
        return k
    n = len(string)
    dict ={}
    for i in string[0:n]:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1

    if len(dict) > k:
        if len(string) % 2 != 0:
            return substring(string[0:n-1],k)
        else:
            return substring(string[1:n],k)

    return n

print(substring('abcabce',3))"""

# ----------------------------------x-------------------------------------------------

# This problem was asked by Twitter.
# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:
# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.

"""from collections import deque

def record(order_id):
    log = deque()
    for i in order_id:
        log.appendleft(i)
    globals()['log'] = log
    print(log)

def get_last(k,order_id):
    log.remove(order_id[len(order_id)-k])
    print(log)

record([18,19,20,21,22])
get_last(2,[18,19,20,21,22])"""

# ----------------------------------x-------------------------------------------------

# This problem was asked by Google.
# Suppose we represent our file system by a string in the following manner:
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
#
# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
#
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty
# second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file
# file2.ext.
# We are interested in finding the longest (number of characters) absolute path to a file within our file system.
# For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext",
# and its length is 32 (not including the double quotes).
# Given a string representing the file system in the above format,
# return the length of the longest absolute path to a file in the abstracted file system.
# If there is no file in the system, return 0.
# Note:
#
# The name of a file contains at least a period and an extension.
#
# The name of a directory or sub-directory will not contain a period.

"""def longest_path(string):
    words = string.split('\n')
    directory = ""
    level = []
    t_count = 0
    for word in words:
        for i in word:
            if i == '\t':
                t_count +=1
        level.append(t_count)
        directory = directory + word[t_count:len(word)] + "/"
        t_count = 0
    name_len = directory.split('/')
    name_len.remove('')
    maximum = max(level)
    sum = 0
    sub_level = []
    while maximum >= 0:
        for j in range(len(level)):
            if level[j] == maximum:
                sub_level.append(name_len[j])
        if len(sub_level) >= 1:
            sum = sum + len(sub_level[-1])
        sub_level.clear()
        maximum = maximum - 1
    sum = sum + max(level)
    # print final answer
    print(sum)

longest_path("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")"""

# ----------------------------------x-------------------------------------------------

# This problem was asked by Snapchat.
# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
# find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

"""def find_min_rooms(list1):
    list1 = sorted(list1)
    print(list1)
    rooms = 1
    start,end = list1[0]
    for i in range(len(list1)-1):
        start_next,end_next = list1[i+1]
        if start_next < end:
            rooms +=1
        if start_next > end:
            temp,end = list1[i]
            rooms -=1
            if start_next < end:
                rooms +=1
    return rooms

print(find_min_rooms([(30, 75), (0, 50), (60, 150),(76,120)]))"""

# ----------------------------------x-------------------------------------------------

# This problem was asked by Facebook.
# A builder is looking to build a row of N houses that can be of K different colors.
# He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color,
# return the minimum cost which achieves this goal.

"""def min_cost(matrix):

    n = len(matrix)
    min_sum = min(matrix[0][:])
    for i in range(1,n):
        if min(matrix[i-1][:]) != min(matrix[i][:]):
            min_sum = min_sum + min(matrix[i][:])
        if min(matrix[i-1][:]) == min(matrix[i][:]):
            temp = sorted(matrix[i][:])
            min_sum = min_sum + temp[1]
    return min_sum

matrix= [[1,2,3],[4,6,5],[9,8,7]]
print(min_cost(matrix))"""

# ----------------------------------x-------------------------------------------------

# This problem was asked by Google.
# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
# In this example, assume nodes with the same value are the exact same node objects.
# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

"""class linked_list:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

    def intersect_node(self):
        head = self
        address = []
        while head.next is not None:
            address.append(head)
            head = head.next
        address.append(head)
        return address

A = linked_list(3)
A.next = linked_list(7)
A.next.next = linked_list(8)
A.next.next.next = linked_list(10)
B = linked_list(99)
B.next = linked_list(1)
B.next.next = A.next.next
B.next.next.next = A.next.next.next

a = A.intersect_node()
b = B.intersect_node()


for i in range(len(a)):
    if a[i] == b[i]:
        print(a[i].val)
        break"""

# ----------------------------------x-------------------------------------------------

# This problem was asked by Microsoft.
# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
# If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction,
# then return null.
# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
# you should return ['the', 'quick', 'brown', 'fox'].
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
# return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

"""list = ['bed', 'bath', 'bedbath', 'and', 'beyond']
string = "bedbathandbeyond"
list1 = []

for i in list:
    if i in string:
        list1.append(string.index(i))
dict = {}
for j in range(len(list)):
    dict[list1[j]] = list[j]

list_values = (sorted(dict.keys()))
list1.clear()
for i in list_values:
    list1.append(dict[i])
print(list1)"""

# ----------------------------------x-------------------------------------------------

# This problem was asked by Google.
# You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall.
# Each False boolean represents a tile you can walk on.
# Given this matrix, a start coordinate, and an end coordinate,
# return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path,
# then return null. You can move up, left, down, and right. You cannot move through walls.
# You cannot wrap around the edges of the board.
# For example, given the following board:
# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the
# end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

"""from collections import deque

def min_steps_to_end(board, start, end):
    if not board or not board[0]:
        return None

    rows, cols = len(board), len(board[0])
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # Possible directions: down, up, right, left

    queue = deque([(start[0], start[1], 0)])  # (row, col, steps)
    visited = set()

    while queue:
        row, col, steps = queue.popleft()

        if (row, col) == end:
            return steps

        for dr, dc in directions:
            r, c = row + dr, col + dc

            if 0 <= r < rows and 0 <= c < cols and not board[r][c] and (r, c) not in visited:
                queue.append((r, c, steps + 1))
                visited.add((r, c))
    return None  # No valid path found

# Example usage:
board = [
    [False, False, False, False],
    [True, True, False, True],
    [False, False, False, False],
    [False, False, False, False]
]

start = (0, 0)
end = (1, 2)

result = min_steps_to_end(board, start, end)
if result is not None:
    print(f"The minimum number of steps required is {result}")
else:
    print("No valid path found.")"""

# ----------------------------------x-------------------------------------------------

# This problem was asked by Facebook.
# Implement regular expression matching with the following special characters:
# . (period) which matches any single character
# * (asterisk) which matches zero or more of the preceding element
# That is, implement a function that takes in a string and a valid regular expression and returns whether or not the
# string matches the regular expression.
# For example, given the regular expression "ra." and the string "ray", your function should return true.
# The same regular expression on the string "raymond" should return false.
# Given the regular expression ".*at" and the string "chat", your function should return true.
# The same regular expression on the string "chats" should return false.

"""import re

def inp(string,pat):
    pattern = re.compile("^"+pat+"$")
    return True if re.match(pattern,string) else False

print(inp("ray","ra."))
print(inp("raymond","ra."))
print(inp("chat",".*at"))
print(inp("chats",".*at"))"""

# ----------------------------------x-------------------------------------------------

# This problem was asked by Google.
# Given a singly linked list and an integer k, remove the kth last element from the list.
# k is guaranteed to be smaller than the length of the list.
# The list is very long, so making more than one pass is prohibitively expensive.
# Do this in constant space and in one pass.

"""class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class Linked_list:
    def __init__(self):
        self.head = None

    def add_at_beg(self,data):
        if self.head is None:
            n = Node()
            n.next = None
            n.data = data
            self.head = n
        else:
            n = Node()
            n.next = self.head
            n.data = data
            self.head = n

    def traverse(self):
        if self.head is None:
            print('empty list')
        else:
            n = self.head
            while n is not None:
                print(n.data, '-->', end="")
                n = n.next

    def remove(self,k):
        if self.head is None:
            print('nothing to remove')
        else:
            list = []
            n = self.head
            while n is not None:
                list.append(n)
                n = n.next
            length = len(list)
            pointer = list[-k-1]
            pointer.next = pointer.next.next

obj = Linked_list()
obj.add_at_beg(20)
obj.add_at_beg(400)
obj.add_at_beg(-10)
obj.add_at_beg(0)
obj.add_at_beg(35)

obj.traverse()
print()
obj.remove(3)
obj.traverse()"""

# ----------------------------------x--------------------------------------------

# This problem was asked by Google.
# Implement locking in a binary tree.
# A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.
# Design a binary tree node class with the following methods:
# [is_locked], which returns whether the node is locked
# [lock], which attempts to lock the node. If it cannot be locked, then it should return false,
# Otherwise, it should lock it and return true.
# [unlock], which unlocks the node. If it cannot be unlocked, then it should return false,
# Otherwise, it should unlock it and return true.
# You may augment the node to add parent pointers or any other property you would like.
# You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes.
# Each method should run in O(h), where h is the height of the tree.

"""class treeNode:
    def __init__(self, lock=False):
        self.left = None
        self.right = None
        self.lock = lock

    def is_locked(self):
        if self.lock is True:
            return True
        if self.lock is False:
            return False

    def lock_it(self):
        if not self.left and not self.right and self.lock is False:
            return True
        while self.left is not None and self.right is not None:
            if self.left.lock_it() and self.right.lock_it():
                self.lock = True
                print("Node locked")
                return True
            else:
                return False

    def unlock_it(self):
        if not self.left and not self.right and self.lock is False:
            return True
        while self.left is not None and self.right is not None:
            if self.left.unlock_it() and self.right.unlock_it():
                self.lock = False
                print('Node unlocked')
                return True
            else:
                return False


node = treeNode(False)
node.left = treeNode(False)
node.left.left = treeNode(False)
node.left.right = treeNode(False)
node.right = treeNode(False)
print(node.left.lock_it())
print(node.left.is_locked())
print(node.left.unlock_it())"""

# ----------------------------------x--------------------------------------------

# This problem was asked by Facebook.
# Given a string of round, curly, and square open and closing brackets,
# return whether the brackets are balanced (well-formed).
# For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.

"""def is_balanced(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack == [] or mapping[char] != stack.pop():
                return False
        else:
            return False
    return stack == []


print(is_balanced("([])[]({})"))
print(is_balanced("()[]"))
print(is_balanced("((()"))"""

# ----------------------------------x--------------------------------------------

# This problem was asked by Amazon.
# Run-length encoding is a fast and simple method of encoding strings.
# The basic idea is to represent repeated successive characters as a single count and character.
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
# Implement run-length encoding and decoding.
# You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
# You can assume the string to be decoded is valid.

"""def encode(string):
    count = []
    list = []
    for i in range(1,len(string)):
        if string[i-1] == string[i]:
            count.append(1)
            if i == len(string)-1:
                list.append(str(len(count)+1)+string[i-1])
        else:
            list.append(str(len(count)+1)+string[i-1])
            count.clear()
    return list

print(encode("AAAABBBCCDAA"))"""

# ----------------------------------x--------------------------------------------

# This problem was asked by Quora.
# Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere
# in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically
# earliest one (the first one alphabetically).
# For example, given the string "race", you should return "ecarace", since we can add three letters to it
# (which is the smallest amount to make a palindrome).There are seven other
# palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.
# As another example, given the string "google", you should return "elgoogle".

"""from collections import deque

def is_palindrome(string):
    list = deque(reversed(string))
    a = ""
    for i in list:
        a = a + i
    if string == a:
        return True
    else:
        return False

def find_palindrome(string):
    if len(string) == 1:
        return string
    if is_palindrome(string):
        return string
    return find_palindrome(string[0:(len(string)-1)])

def return_palindrome(string):
    a = find_palindrome(string)
    if len(a) == 1:
        b = list(reversed(string[1:len(string)]))
        c = ""
        for i in b:
            c = c + i
        return c + string
    if len(a) > 1:
        c = len(a)
        d = list(reversed(string[c:len(string)]))
        e = ""
        for j in d:
            e = e + j
        return e + string

print(return_palindrome("car"))"""

# ----------------------------------x--------------------------------------------

# This problem was asked by Microsoft.
# Compute the running median of a sequence of numbers. That is, given a stream of numbers,
# print out the median of the list so far on each new element.
# Recall that the median of an even-numbered list is the average of the two middle numbers.
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
# 2,1.5,2,3.5,2,2,2

"""from collections import deque
def median_run(list):
    stack = deque()
    for i in list:
        stack.append(i)
        stack = sorted(stack)
        if len(stack) == 1:
            print(i)
        else:
            if len(stack) % 2 == 0:
                j = len(stack)//2
                print((stack[j] + stack[j-1])/2)
            else:
                j = len(stack)//2
                print(stack[j])

median_run([2, 1, 5, 7, 2, 0, 5])"""

# ----------------------------------x--------------------------------------------

# This problem was asked by Google.
# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so
# that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.
# Do this in linear time and in-place.
# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B']

# THIS IS A PROBLEM FROM DUTCH NATIONAL FLAG (DNF) ALGORITHM

"""def segregate_rgb(arr):
    low = 0
    high = len(arr) - 1
    mid = 0

    while mid <= high:
        if arr[mid] == 'R':
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 'G':
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
segregated_arr = segregate_rgb(arr)
print(segregated_arr)"""

# ----------------------------------x--------------------------------------------

# This problem was asked by Google.
# The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
# For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
# You may also use a list or array to represent a set.

"""def generate_power_set(nums):
    n = len(nums)
    power_set_size = 2 ** n
    result = []
    for i in range(power_set_size):
        subset = []
        for j in range(n):
            if (i & (1 << j)) > 0:
                subset.append(nums[j])
        result.append(subset)
    return result

input_set = [1, 2, 3]
print(generate_power_set(input_set))"""

# ----------------------------------x--------------------------------------------

# Finding a number in an array in O(N) time and O(1) space with only 1 different value and other repeated a common -
# number of times.

"""array = [3,3,4,3,3,2,2,2,2]
find = 0
for i in range(4):
    count = 0
    for num in array:
        if (num >> i) & 1:
            count = count + 1
            count = count % 4
    if count != 0:
        find = find | (count << i)

print(find)"""

# ----------------------------------x--------------------------------------------

# Classic Backtracking N-queens problem in NxN board
"""result = []

def solvequeens(board, row, n):
    if row == n:
        result.append(["".join(row) for row in board])
        return

    for col in range(n):
        if is_valid(board, row, col, n):
            board[row][col] = 'Q'
            solvequeens(board, row + 1, n)
            board[row][col] = '.'

def is_valid(board, row, col, n):
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True

n = 4
board = [["." for _ in range(n)] for _ in range(n)]
solvequeens(board, 0, n)
print(result)"""

# ----------------------------------x--------------------------------------------

# backtracking problem 2

"""def arrangements(string,result):
    if len(result) == 3:
        print(result)
        return
    for i,j in enumerate(string):
        curr_index = i
        new_string = string[0:curr_index] + string[curr_index+1:]
        arrangements(new_string,result+j)

arrangements("ABC","")"""

# ----------------------------------x--------------------------------------------

# This problem was asked by Google.
# Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k.
# If such a subset cannot be made, then return null.
# Integers can appear more than once in the list. You may assume all numbers in the list are positive.
# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

"""def sub_set(nums,k):
    n = len(nums)
    power_set_size = 2 ** n
    for i in range(power_set_size):
        subset = []
        for j in range(n):
            if (i & (1 << j)) > 0:
                subset.append(nums[j])
        sumation = 0
        if len(subset) > 0:
            for l in subset:
                sumation = sumation + l
            if sumation == k:
                return subset
    return None

input_set = [12, 1, 61, 5, 9, 2]
print(sub_set(input_set,24))"""

# method 2
"""def find_sub(list,k,res,result):
    if res == 0:
        return result
    while len(list) != 0:
        res = res - list[0]
        result.append(list[0])
        if res > 0:
            return find_sub(list[1:],k,res,result)

        if res < 0:
            result.pop()
            res = res + list[0]
            return find_sub(list[1:],k,res,result)
    return result

def check_list(list,k,result):
    for i,j in enumerate(list):
        result.clear()
        res = k
        temp = list[i]
        list[i] = 0
        result = find_sub(list,k,res,result)
        list[i] = temp
        if result_false(result,k):
            result.remove(0)
            return result


def result_false(result,k):
    temp = 0
    for i in result:
        temp +=i
    if temp == k:
        return True

if __name__ == "__main__":
    list = [12, 1, 61, 5, 9, 2]
    k = 8
    res = k
    a = find_sub(list,k,res,[])
    if result_false(a,k):
        print(a)
    else:
        print(check_list(list,k,[]))"""

# ----------------------------------x--------------------------------------------

# This problem was asked by Amazon.
# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137,
# since we would take elements 42, 14, -5, and 86.
# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
# Do this in O(N) time.

# kadane's algorithm

"""def max_sum(list):
    maximum = 0
    for num in list:
        maximum += num
        maximum = max(0,maximum)
    return maximum

print(max_sum([34, -50, 42, 14, -5, 86]))"""

# ----------------------------------x--------------------------------------------

# This problem was asked by Amazon.
# A sorted array of integers was rotated an unknown number of times.
# Given such an array, find the index of the element in the array in faster than linear time.
# If the element doesn't exist in the array, return null.
# For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).
# You can assume all the integers in the array are unique.

"""def find_index(list,element,start):
    n = len(list)
    last = n-1
    mid = last // 2
    if element == list[mid]:
        return mid
    if element == list[last]:
        return last
    if element == list[start]:
        return start
    if list[mid] > list[last] and element < list[last]:
        return mid + find_index(list[mid:],element,mid)
    if list[mid] > list[start] and element > list[start]:
        return start + find_index(list[:mid],element,0)
    if list[mid] < list[last] and element < list[mid]:
        return start + find_index(list[:mid],element,0)
    if list[mid] > list[start] and element > list[mid]:
        return mid + find_index(list[mid:],element,mid)
    if list[mid] < list[start] and element > list[mid]:
        return start + find_index(list[:mid],element,0)
    if list[mid] < list[start] and element < list[mid]:
        return mid + find_index(list[mid:],element,mid)

print(find_index([13, 18, 25, 2, 8, 10],8,0))"""

# ----------------------------------x--------------------------------------------

# This problem was asked by Google.
# Given an undirected graph represented as an adjacency matrix and an integer k,
# write a function to determine whether each vertex in the graph can be colored such that no two adjacent
# vertices share the same color using at most k colors.

"""def is_valid(graph,vertex,color,coloring):
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and coloring[i] == color:
            return False
    return True

def color_vertex(graph,vertex,coloring,k):
    if vertex == len(graph):
        return True
    for color in range(1,k+1):
        if is_valid(graph,vertex,color,coloring):
            coloring[vertex] = color
            if color_vertex(graph,vertex+1,coloring,k):
                return True
            coloring[vertex] = 0
    return False

graph = [[0,1,0,1],
        [1,0,1,0],
        [0,1,0,1],
        [1,0,1,0]]

coloring = [0]*len(graph)
print(color_vertex(graph,0,coloring,2))"""

# ----------------------------------x--------------------------------------------

# his problem was asked by Facebook.
# There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting
# at the top-left corner and getting to the bottom-right corner. You can only move right or down.
# For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:
# Right, then down
# Down, then right
# Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

"""def ways(n,m):
    if n == 1 or m == 1:
        return 1
    return ways(n-1,m) + ways(m-1,n)

print(ways(5,5))"""

# ----------------------------------x--------------------------------------------

# This problem was asked by Google.
# Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.

"""class node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def head(self):
        self.head = self

def sort(head1,head2):
    p1 = head1
    p2 = head2
    arr = []
    while p1.next or p2.next is not None:
        if p1.val > p2.val:
            arr.append(p2.val)
            p2 = p2.next
        if p1.val < p2.val:
            arr.append(p1.val)
            p1 = p1.next
    if p1.next is not None:
        while p1.next is not None:
            p1 = p1.next
            arr.append(p1.val)
    if p2.next is not None:
        while p2.next is not None:
            p2 = p2.next
            arr.append(p2.val)
    if p1.val > p2.val:
        arr.append(p2.val)
        arr.append(p1.val)
    if p1.val < p2.val:
        arr.append(p1.val)
        arr.append(p2.val)
    return arr

n1 = node(12)
n2 = node(23)
n1.next = n2
n3 = node(27)
n2.next = n3
n4 = node(56)
n3.next = n4
head1 = n1

m1 = node(10)
m2 = node(14)
m1.next = m2
m3 = node(25)
m2.next = m3
m4 = node(37)
m3.next = m4
head2 = m1

a = sort(head1,head2)"""

# ----------------------------------x--------------------------------------------

# This problem was asked by Google.
# In a directed graph, each node is assigned an uppercase letter. We define a path's value as the number of most
# frequently-occurring letter along that path. For example, if a path in the graph goes through "ABACA",
# the value of the path is 3, since there are 3 occurrences of 'A' on the path
# Given a graph with n nodes and m directed edges, return the largest value path of the graph.
# If the largest value is infinite, then return null.
# The graph is represented with a string and an edge list. The i-th character represents the uppercase
# letter of the i-th node. Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to t
# e j-th node. Self-edges are possible, as well as multi-edges.
# For example, the following input graph:
#
# ABACA
# [(0, 1),
#  (0, 2),
#  (2, 3),
#  (3, 4)]
# Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).
# The following input graph:
# A
# [(0, 0)]
# Should return null, since we have an infinite loop.

"""temp = 0
count = 0
arr = []
def largest_value_path(string,list,count):
    if len(string) == 1:
        return None
    if len(list) == 1:
        count += 1
        return count
    for i in range(len(list)):
        temp = list[i][1]
        for j in range(i,len(list)):
            if temp == list[j][0]:
                count = count + 1
                arr.append(largest_value_path(string,(list[j:]),count))
            else:
                pass
        count = 0

    return max(arr)

print(largest_value_path("ABACA",[(0, 1),(0, 2),(2, 3),(3, 4)],0))"""

# ----------------------------------x--------------------------------------------

# LFU(Least Frequently Used) Cache algorithm

"""class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = []
        self.dict = {}

    def get(self, key: int) -> int:
        if key in self.dict:
            return self.arr[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.arr) < self.capacity:
            if key in self.dict:
                self.arr.append((key, value))
                self.dict[key] += 1
                print(self.arr)
            else:
                self.arr.append((key, value))
                self.dict[key] = 1
                print(self.arr)

        if len(self.arr) == self.capacity:

            key1, val1 = self.arr[0]
            if self.dict[key1] == 1:
                del self.dict[key1]
                self.arr.remove((key1, val1))
                self.arr.append((key, value))
                print(self.arr)
            else:
                key2, val2 = self.arr[0]
                list1 = list(self.dict.values())
                list2 = list(self.dict.keys())
                for val in list1:
                    if val < val2:
                        self.arr.remove((list2[list1.index(val)], val))
                        self.arr.append((key, value))
                        self.dict[self.dict.get(val)] -= 1
                        print(self.arr)


# Your LFUCache object will be instantiated and called as such:
obj = LFUCache(6)
obj.put(1, 1)
obj.put(2, 2)
obj.put(3, 3)
obj.put(3, 3)
obj.put(5, 5)
obj.put(6, 6)
obj.put(7, 7)
obj.put(8, 8)"""
    
# ----------------------------------x--------------------------------------------

"""import os

user = os.getenv('OS')
print(user)
print(os.getcwd())
command = 'ipconfig'
result = os.system(command)
print(result)

import sys

platform = sys.platform
print(platform)

def process_data(data):
    # Process the data
    if len(data) == 0:
        print("Error: No data to process.")
        sys.exit(1)

    # Continue with data processing
    print("Processing data...")

data = []
process_data(data)

try:
    x = 10 / 0
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("Exception Type:", exc_type.__name__)
    print("Exception Value:", exc_value)
    print("Exception Traceback:", exc_traceback)"""

# ----------------------------------x--------------------------------------------

# This problem was asked by Uber.
# A rule looks like this:
# A NE B
# This means that point A is located northeast of point B.
# A SW C
# means that point A is southwest of C.
#
# Given a list of rules, check if the sum of the rules validate. For example:
# A N B
# B NE C
# C N A
# does not validate, since A cannot be both north and south of C.
# A NW B
# A N B
# is considered valid.

"""class rules:
    def __init__(self):
        self.north = []
        self.south = []
        self.count = 0

    def input_rule(self, string: str) -> None:
        if len(self.north) > 0:
            if "N" in string or "NW" in string or "NE" in string:
                if string[0] == self.north[-1] and string[-1] == self.south[-1]:
                    pass
                else:
                    if string[0] in self.north or self.south:
                        if string[0] in self.north:
                            if string[-1] not in self.south:
                                self.north.append(string[-1])
                            else:
                                self.count += 1

                        if string[0] in self.south:
                            if string[-1] not in self.north:
                                self.south.append(string[-1])
                            else:
                                self.count += 1
                    else:
                        if "N" in string or "NW" in string or "NE" in string:
                            self.north.append(string[0])
                            self.south.append(string[-1])
                        if "S" in string or "SW" in string or "SE" in string:
                            self.south.append(string[0])
                            self.north.append(string[-1])
            else:
                if "N" in string or "NW" in string or "NE" in string:
                    self.north.append(string[0])
                    self.south.append(string[-1])
                if "S" in string or "SW" in string or "SE" in string:
                    self.south.append(string[0])
                    self.north.append(string[-1])
            if "S" in string or "SW" in string or "SE" in string:
                if string[0] == self.south[-1] and string[-1] == self.north[-1]:
                    pass
                else:
                    if string[0] in self.north or self.south:
                        if string[0] in self.north:
                            if string[-1] not in self.south:
                                self.north.append(string[-1])
                            else:
                                self.count += 1

                        if string[0] in self.south:
                            if string[-1] not in self.north:
                                self.south.append(string[-1])
                            else:
                                self.count += 1
                    else:
                        if "N" in string or "NW" in string or "NE" in string:
                            self.north.append(string[0])
                            self.south.append(string[-1])
                        if "S" in string or "SW" in string or "SE" in string:
                            self.south.append(string[0])
                            self.north.append(string[-1])
        else:
            if "N" in string or "NW" in string or "NE" in string:
                self.north.append(string[0])
                self.south.append(string[-1])
            if "S" in string or "SW" in string or "SE" in string:
                self.south.append(string[0])
                self.north.append(string[-1])



    def validate(self):

        if self.count > 0:
            return "Not Valid"
        else:
            return "Valid"

object = rules()
object.input_rule("A N B")
object.input_rule("B NE C")
object.input_rule("C N A")
print(object.validate())"""

# ----------------------------------x--------------------------------------------

# code to check time complexity of dynamically programmed code vs normal approach

"""from timeit import default_timer

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n*factorial(n-1)

print('without dynamic approach')
start = default_timer()
print(factorial(5))
end = default_timer()
print("total time taken: ",end - start)

print()

def fact_dynamic(n, memo):
    if n == 0 or n == 1:
        return 1

    if n not in memo:
        memo[n-1] = n * fact_dynamic(n - 1, memo)

    return memo[n-1]

print('with dynamic approach')
start = default_timer()
print(fact_dynamic(5,[0,0,0,0,0]))
end = default_timer()
print("total time taken: ",end - start)"""

# ----------------------------------x--------------------------------------------

# Given two non-empty binary trees s and t,
# check whether tree t has exactly the same structure and node values with a subtree of s.
# A subtree of s is a tree consists of a node in s and all of this node's descendants.
# The tree s could also be considered as a subtree of itself.


"""class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

array = []
array1 = []

def helper(node1):
    if node1.left is None and node1.right is None:
        return node1.val
    left_value = helper(node1.left)
    if left_value is not None:
        array.append(left_value)
    right_value = helper(node1.right)
    if right_value is not None:
        array.append(right_value)
    array.append(node1.val)

def is_exact(node1,node2):
    helper(node1)
    for i in array:
        array1.append(i)
    array.clear()
    helper(node2)
    j = 0; k = 0
    while j < len(array1) and k < len(array):
        if array1[j] == array[k]:
            k+=1; j+=1
        else:
            j+=1
    if k == len(array):
        print("is_exact")



node1 = Node(5)
node1.left = Node(3)
node1.left.left = Node(1)
node1.left.right = Node(4)
node1.right = Node(10)
node1.right.left = Node(9)
node1.right.right = Node(11)

node2 = Node(3)
node2.left = Node(1)
node2.right = Node(4)

is_exact(node1,node2)"""

# ----------------------------------x--------------------------------------------

# This problem was asked by Google.
# Given an iterator with methods next() and hasNext(), create a wrapper iterator, PeekableInterface,
# which also implements peek(). peek shows the next element that would be returned on next().
# Here is the interface:
#
# class PeekableInterface(object):
#     def __init__(self, iterator):
#         pass
#
#     def peek(self):
#         pass
#
#     def next(self):
#         pass
#
#     def hasNext(self):
#         pass

"""class PeekableInterface:
    def __init__(self, list):
        self.list = list
        self.i = 0

    def peek(self):
        print("Next Element: ",self.list[self.i+1])

    def next(self):
        self.i = self.i + 1
        return self.list[self.i]

    def hasNext(self):
        if self.i < len(self.list)-1:
            print("It has next element")
        else:
            print("No next element")

list = [1,2,3,4,5]
object = PeekableInterface(list)
object.peek()
print(object.next())
object.hasNext()
object.peek()
print(object.next())
object.hasNext()
object.peek()
print(object.next())
object.hasNext()
object.peek()
print(object.next())
object.hasNext()"""

# ----------------------------------x--------------------------------------------

# This problem was asked by LinkedIn.
# Given a list of points, a central point, and an integer k, find the nearest k points from the central point.
# For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2,
# return [(0, 0), (3, 1)].

"""from math import sqrt

def find_nearest(list,point,k):
    list2 = []
    list1 = []
    x,y = point[0],point[1]
    for i,j in list:
        list2.append(((sqrt((x-i)**2 + (y-j)**2)),(i,j)))
    for _ in range(k):
        list1.append(min(list2))
        list2.remove(min(list2))
    return list1

print(find_nearest([(0,0),(5,4),(3,1)],(1,2),2))"""


# ----------------------------------x--------------------------------------------

# This problem was asked by Uber.
# Given a tree where each edge has a weight, compute the length of the longest path in the tree.
# For example, given the following tree:
#    a
#   /|\
#  b c d
#     / \
#    e   f
#   / \
#  g   h
# and the weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1,
# the longest path would be c -> a -> d -> f, with a length of 17.
# The path does not have to pass through the root, and each node can have any amount of children.

"""total_sum_path = []

def largest_path(matrix,nodes):
    temporary_sum = 0
    for i in range(0,nodes):
        temp = 0
        visited = []
        path = []
        while i not in visited:
            for j in range(0,nodes):
                if matrix[i][j] != 0 and matrix[i][j] not in path:
                    temp = max(temp,matrix[i][j])
            if temp == 0:
                break
            visited.append(i)
            path.append(temp)
            temporary_sum += temp
            for j in range(0,nodes):
                if matrix[i][j] == temp:
                    i = j
                    break
            temp = 0
        total_sum_path.append(temporary_sum)
        temporary_sum = 0

    return max(total_sum_path)

matrix = [[0,3,5,8,0,0,0,0],
          [3,0,0,0,0,0,0,0],
          [5,0,0,0,0,0,0,0],
          [8,0,0,0,2,4,0,0],
          [0,0,0,2,0,0,1,1],
          [0,0,0,4,0,0,0,0],
          [0,0,0,0,1,0,0,0],
          [0,0,0,0,1,0,0,0]]

print(largest_path(matrix,8))"""

# ----------------------------------x--------------------------------------------

# 0-1 KNAPSACK PROBLEM

"""values = [1.5,3,10,3.5]
weights = [100,150,1000,350]
k = 500

def knapsack(n,k):
    if n == -1 or k == 0:
        return 0
    elif weights[n] > k:
        return knapsack(n-1,k)
    else:
        temp1 = values[n] + knapsack(n-1,k-weights[n])
        temp2 = knapsack(n-1,k)
        temp3 = max(temp1,temp2)
        return temp3

print(knapsack(len(values)-1,k))"""

# ----------------------------------x--------------------------------------------

# This problem was asked by Twitter.
# A teacher must divide a class of students into two teams to play dodgeball.
# Unfortunately, not all the kids get along, and several refuse to be put on the same team as that of their enemies.
# Given an adjacency list of students and their enemies, write an algorithm that finds a satisfactory pair of teams,
# or returns False if none exists.
# For example, given the following enemy graph you should return the teams {0, 1, 4, 5} and {2, 3}.
#
# students = {
#     0: [3],
#     1: [2],
#     2: [1, 4],
#     3: [0, 4, 5],
#     4: [2, 3],
#     5: [3]
# }
# On the other hand, given the input below, you should return False.
#
# students = {
#     0: [3],
#     1: [2],
#     2: [1, 3, 4],
#     3: [0, 2, 4, 5],
#     4: [2, 3],
#     5: [3]
#  }

students = {
    0: [3],
    1: [2],
    2: [1, 3, 4],
    3: [0, 2, 4, 5],
    4: [2, 3],
    5: [3]
 }

def find_team(students):
    i = len(students)
    # visited = []
    group1,group2 = [],[]

    m = students.keys()
    for j in m:
        group1.append(j)
        # visited.append(j)

        for k in students[j]:
            if k in group1:
                if j in group1:
                    group1.remove(j)
    for l in m:
        if l in group1:
            pass
        else:
            group2.append(l)

    for j in group2:
        for k in students[j]:
            if k in group2:
                return "TEAM FORMATION NOT POSSIBLE!"


    return f"team1 :{group1} and team2 : {group2}"

print(find_team(students))

# ----------------------------------x--------------------------------------------













