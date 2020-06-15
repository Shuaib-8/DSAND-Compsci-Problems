# Unscramble Computer Science Problems Using Python

In this project, I set out to complete five tasks based on a fictional set of calls and texts (stored in a csv) exchanged during September 2016. I used Python to analyze and answer questions about the texts and calls contained in the dataset. Finally, I rounded the analysis off by documenting run time (Worst-Case Big-0 Notation) analyses of my solutions and determine each algorithms' efficiency.

## Task 0 

This task revolved around finding the first record of texts and last record of calls.
Simply, the solution to this task revolved around a simple search for the elements with a collection of lists (csv file). 
Hence, the run time analysis of this algorithm is O(1), which is constant.

## Task 1

This tasks centres around calculating the distinct set of numbers from the calls/texts records as gathered from the csv files.
As the algorithm loops (iterates) over the records and then checks to provide back only unique records, a larger input is proportional (linearly) to a longer run time.
Thus, the run time analysis of this algorithm is similar to O(n+1), where we drop constants as we consider only large inputs overall, so this simplifies to O(n) which is linear.

## Task 2

Similarly to task 1, this algorithm exploits looping over a collection of lists gathered from a csv file(s), given that the computation is a function of the size of the input (when it's very big) that is given as a list of lists (as n). Hence when we check the order of growth as the input size scales up, we find the complexity (worst) case to be around O(4n + 1). Overall, given we drop constant and multiplicative factors as above, this simplifies to O(n) as well.

## Task 3 

***Part A***

As above, this algorithm exploits looping over a collection of lists gathered from a csv file(s) - computation is a function of the size of the input - given as list of lists (size n). Furthermore, we take the distinct observations as a set of values that are sorted in a lexicographical order. Hence when we check the order of growth as the input size scales up, we find the complexity (worst) case to be around O(n log n + 2n + 1). Overall, given we drop constant/multlicative factors and in this case focus only on the dominant term (n log n), this simplifies to O(n log n) which is log-linear.

***Part B***

The second part of this task involes searching (looping/iterating) over a collection of lists gathered from the calls csv that is known to be (as a function of the algorithm) size of the input n (lists).