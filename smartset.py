# Smartest Set
# A smart-set is a set of distinct numbers in which all the elements have the same number of 1s in their binary form.
# The set of all smallest elements from each smart-set
# that can be formed from a given array of distinct positive numbers is known as the smartest-set.
#
# So given an array of distinct numbers, outline the elements of the smartest-set in ascending sorted order.
#
# Example
# Let the array be {6 , 2 , 11 , 1 , 9 , 14 , 13 , 4 , 18}.
# In binary form the set is {110, 010, 1011, 0001, 1001, 1110, 1101, 0100, 10010}.
# The smart-sets are {1, 2, 4}, {6, 9, 18}, {11, 13, 14}.
#
# The smartest-set is {1,6,11} as each element is the smallest element from each smart-set.
#
# Input Format
#
# The first line of input consists of an integer t. This is the number of test cases. For each test case,
# the first line of input contains an integer n. Here n is the number of elements in the array. The next line contains
# n space separated distinct integers which are the elements
# of the array.
#
# Output Format
#
# The output will space separated integer elements of the smartest-set in ascending order.
#
# Constraints
#
# 0 < t < 1000 (This is the number of test cases
# 2 < n < 10000 (This is the number of integer elements of the array)
# 1 < Xi < 100000 (This is the size of each element of the array)
#
# Sample input :
# 3
# 9
# 6 2 11 1 9 14 13 4 18
# 3
# 7 3 1
# 3
# 1 2 4
# Sample Output :
# 1 6 11
# 1 3 7
# 1
#
# Sample stdin 1
# 3
# 9
# 6 2 11 1 9 14 13 4 18
# 3
# 7 3 1
# 3
# 1 2 4
# Sample stdout 1
# 1 6 11
# 1 3 7
# 1

# Taking inputs from the Stdin
t = int(input())
total_lists = []
if 0 < t < 1000:
    for i in range(0, t):
        n = int(input())
        if 2 < n < 10000:
            temp = input().strip().split(' ')
            for k in range(len(temp)):
                temp[k] = int(temp[k])
            total_lists.append(list(set(temp)))


def smart_set(l):
    """
    The method that calculates the smart set for a given list
    :param: l, type: list 
    """
    binary_lst = []
    dic = {}
    for number in l:
        binary_lst.append(bin(number))

    for numb in binary_lst:
        cnt = numb.count('1')
        if cnt not in dic:
            dic[cnt] = []
            dic[cnt].append(int(numb, 2))
        else:
            dic[cnt].append(int(numb, 2))

    for x in dic:
        print(min(dic[x]), end=' ')
    print('')


for lst in total_lists:
    smart_set(lst)
