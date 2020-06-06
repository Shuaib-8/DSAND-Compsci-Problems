# Unscramble Computer Science Problems Using Python

In this project, I set out to complete five tasks based on a fictional set of calls and texts (stored in a csv) exchanged during September 2016. I used Python to analyze and answer questions about the texts and calls contained in the dataset. Finally, I rounded the analysis off by documenting run time (Worst-Case Big-0 Notation) analyses of my solution and determine each algorithms' efficiency.

## Task 0 

This task revolved around finding the first record of texts and last record of calls.
Simply, the solution to this task revolved around a simple search for the elements with a collection of lists (csv file). 
Hence, the run time analysis of this algorithm is O(1).

## Task 1

This tasks centres around calculating the distinct set of numbers from the calls/texts records as gathered from the csv files.
As the algorithm loops (iterates) over the records and then checks to provide back only unique records, a larger input is proportional (linearly) to a longer run time.
Thus, the run time analysis of this algorithm is similar to O(n+1), where we drop constants as we consider only large inputs overall, so this simplifies to O(n).