 #ECOR 1042 Lab 6 - Individual submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Caleb Payne"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101264830"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-115"

#==========================================#
# Place your histogram function after this line
import matplotlib.pyplot as plt

def histogram(dictionaries: list, attribute: str) -> None:
    """This function takes a list of student dictionaries and a string as inputs.The string specifies which attribute of the dictionaries is wanted to be graphed. The functions returns a bar graph with the values of the attributes along the x-axis and the amount of students with those attributes along the y-axis.
    
    preconditions: attributes is a string that is a key in dictionaries
    
    >>>histogram([{'school': 'MP'},{'school': 'LF'}, {'school': 'LF'}, {'school': 'CB'}], 'school')
    <<<<histogram is displayed>>
    >>>histogram([{'health': 1},{'health': 2}, {'health': 1}, {'health': 4}], 'health')
    <<<<histogram is displayed>>
    >>>histogram([{'G_avg': 1.5},{'G_avg': 2.3}, {'G_avg': 6.0}, {'G_avg': 6.0}], 'G_avg')
    <<<<histogram is displayed>>
    """

    required_values = []
    y_values = []
    
    for i in range(len(dictionaries)):
        required_values += [dictionaries[i][attribute]]
      
    x_values_set = set(required_values)
    x_values = list(x_values_set)
    
    for i in range(len(x_values)):
        y_values += [required_values.count(x_values[i])]

    fig1 = plt.figure()
    plt.title('Student' + ' ' + attribute + ' ' + 'Histogram')
    plt.xlabel(attribute)
    plt.ylabel('Amount of Students')
    plt.bar(x_values, y_values, 0.5, color='mediumseagreen')
    plt.show()

    # Do NOT include a main script in your submission
