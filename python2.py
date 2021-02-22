#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. You are given a time in 12-hour format. Convert it to 24-hour format.
# Input : 08:55:48PM
# Output : 20:55:48
# Function to convert the date format
def timeConversion(s):
    if s[8:]=='PM':
        if int(s[:2])<12:
           return str(int(s[:2])+12)+str(s[2:8])
        else:
           return s[:8]          
    else :
        if int(s[:2])==12:
           return '00'+str(s[2:8])
        else:
           return s[:8]   
if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)


# In[ ]:


#2. John and Sean went to a shop to buy chocolates. John doesn’t buy a chocolate that
# Sean does. Consider N no.of chocolates are there and they have a total of Rs.M. Given
# a list of prices of chocolates, select the two that will cost all of the money they have.
# Considering 1-based indexing, print which two chocolate they bought.
def chocoBuy():
    lst = [] 
    i=0
    m=0
    # number of elemetns as input 
    n = int(input("Enter number of chocolates : ")) 
    p=int (input('Enter total price: '))
    # iterating till the range 
    for i in range(0, n): 
        choco = int(input('Enter Choco price : '))
        lst.append(choco) # adding the element
    #     print(lst)

    for ele in range(0, (len(lst)-1)):
        m=lst[ele] + lst[ele+1]
        if(p==m):
            print('You can buy choco')
            print(lst[ele],lst[ele+1])
            #print("These two" + lst[ele] + "," + lst[ele+1] + "chocolate they can buy")
        else :
            print('You can not buy choco')

if __name__ == '__main__':
    chocoBuy()


# In[ ]:


# Alice and Bob decided to have a competition. They wrote N no.of tests. For whoever
# scores more will be given one point. If both score the same marks, no point is awarded.
# Alice's marks are entered first followed by Bob’s. Calculate who got how many points.
# The output should display their name and no.of point each got followed by who won the
def Ab():
    alice = 0
    bob = 0
    alst = []
    blst = []
    # number of elemetns as input 
    n = int(input("Enter number of subject : "))  
    for i in range(0, n): 
        a = int(input('Enter Mark of Alice : '))
        alst.append(a) # adding the element
    for i in range(0, n):
        b = int(input('Enter Mark of Bob : '))
        blst.append(b) # adding the element
    for i in range(0, n):
        if alst[i] > blst[i]:
            alice += 1
        elif blst[i] > alst[i]:
            bob += 1
    if alice > bob:
        print('alice won')
    elif alice==bob:
        print('No point to Both')
    else:
        print('bob won')
if __name__ == '__main__':
    Ab()


# In[ ]:


#You are given no.of words followed by the list of words. For each word, print the word,
#it’s length and number of its occurrences.

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def word_len(str):
    lengths = dict()
    words = str.split()
    for word in words :
        if word in lengths:
            word_len(len(word))

    return lengths

if __name__ == '__main__':
    print(word_len('5 New old Existing New New'))
    print( word_count('5 New old Existing New New'))


# In[ ]:


# You are given a sentence containing alphabets, numbers, symbols and spaces. Your
# task is to sort the string in the following order and each separated by space:
def splitString(str):
    alpha = ""
    even = ""
    special = ""
    upper = ""
    lower = ""
    odd = ""
    
    for i in range(len(str)):
        if (str[i].isdigit()%2==0):
            even = even+ str[i]
        elif (str[i].isdigit()%2!=0):
            odd = odd+ str[i]
        elif str[i].isupper():
            upper += str[i]
        elif str[i].lower():
            lower += str[i]
        else:
            special += str[i]
            
    print(upper) 
    print(even)
    print(special)
    print(lower)
    print(odd)

if __name__ == "__main__": 
    str = "131/265 is where I and Sam Live."
splitString(str)  


# In[ ]:


# You are given a list of N books and their details (no.of pages, price and no.of chapters).
# Display the list of attributes and ask the user to select one attribute. You are required to
# 3
# sort the data based on the attribute selected by the user and print the final resulting
# table.
def Ab():
    alst = []
    blst = []
    clst = []
    # number of elemetns as input 
    n = int(input("Enter number of books : "))  
    for i in range(0, n): 
        a = int(input('Enter No of pages of each book : '))
        alst.append(a) # adding the element
    for i in range(0, n):
        b = int(input('Enter price of each book : '))
        blst.append(b) # adding the element
    for i in range(0, n):
        c = int(input('Enter no of chapter of each book : '))
        clst.append(c) # adding the element
    print('1.pages',alst)
    print('2.price',blst)
    print('3.chapter',clst)
    for i in range(0, 3):
        d = int(input('Enter which attribute u want 1/2/3 : '))
        if d==1:
            print(alst)
        elif d==2:
            print(blst)
        elif d==3:
            print(clst)
    
if __name__ == '__main__':
    Ab()

