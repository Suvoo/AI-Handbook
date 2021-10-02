import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    ans1 = np.exp(L)
    su = sum(ans1)
    ans = []

    for i in ans1:
        ans.append(i/su)
    
    return ans

