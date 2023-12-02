import time

# Code to calculate the thickness when the paper is folded 43 times
THICKNESS = 0.00008

#[Problem 1] Implementation using exponentiation arithmetic operators
'''
Create a program that uses the exponentiation arithmetic operator.

As a template, we have prepared a code that calculates the thickness of a sheet of paper when it is folded once. Rewrite the code to calculate the thickness when the paper is folded 43 times.
'''

folded_thickness = THICKNESS * 2 ** 43
print("Thickness: {} meters".format(folded_thickness))

#[Problem 2] Unit Conversion
'''
If the unit is meters, it's hard to feel the difference, so please convert the unit to ◯◯ 10,000 kilometers and display it.

​We have prepared a code converted to ◯◯ kilometers as a sample, so please refer to it when working on it. It is specified that up to 2 digits are displayed after the decimal point.
'''

print("Thickness: {:.2f} kilometers".format(folded_thickness / 1000))


#[Problem 3] Create using a for statement
'''
Next, create a program that uses the for statement.

Do not use exponentiation arithmetic operators. Only the four arithmetic operations+ , - , * , / ) are allowed.
'''

THICKNESS = 0.00008
num_folds = 43

folded_thickness = THICKNESS

for _ in range(num_folds):
    folded_thickness *= 2

print("Thickness: {:.2f} kilometers".format(folded_thickness / 1000))

#[Problem 4] Comparison of calculation time
'''
Both of the above two methods are correct, but when comparing the goodness of the code, for example, the following points are evaluated.

Execution speed
Memory usage
Readability
Scalability
Reusability
This time I will compare the execution speed.

Use the template below to output the execution times of the two methods and compare them. Compare the time in the range excluding the parts used by either method, such as variable definition and print​
'''

start = time.time()
folded_thickness = THICKNESS * 2 ** 43
elapsed_time = time.time() - start
print("Using exponentiation: time {}[s]".format(elapsed_time))


start = time.time()
folded_thickness = THICKNESS
for _ in range(43):
    folded_thickness *= 2
elapsed_time = time.time() - start
print("Using for statement: time {}[s]".format(elapsed_time))

##[Problem 5] Saving to a list
'''
So far, we have only used the last value after 43 folds, but we need the process values as well to visualize them in the graph; add the code that records the total of 44 process values to the code using the for statement.
'''
THICKNESS = 0.00008
num_folds = 43

folded_thickness_list = [THICKNESS]

for _ in range(num_folds):
    folded_thickness *= 2
    folded_thickness_list.append(folded_thickness)

print("Number of elements in the list: {}".format(len(folded_thickness_list)))

#[Problem 6] Displaying a line graph
'''
A library called Matplotlib is used to draw the graph. Use the following template after the code you want to record in the list.
'''
import matplotlib.pyplot as plt

# Display the graph
plt.title("Thickness of Folded Paper")
plt.xlabel("Number of Folds")
plt.ylabel("Thickness [m]")
plt.plot(folded_thickness_list)
plt.show()

#[Problem 7] Customizing graphs
'''
Let's customize the graph to make it easier to see. Create at least 3 customized graphs. For example, the line color can be changed to red by rewriting as follows.
'''
plt.title("Thickness of Folded Paper")
plt.xlabel("Number of Folds")
plt.ylabel("Thickness [m]")
plt.plot(folded_thickness_list, color='green', linewidth=2, linestyle='--', marker='o', markersize=8)
plt.show()