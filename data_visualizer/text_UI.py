# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Shifat Ghazi"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101265285"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-115"


import numpy as np
import matplotlib.pyplot as plt


import histogram
from histogram import histogram

import curve_fit
from curve_fit import curve_fit


import sort
from sort import*
from sort import sort_students_age_bubble
from sort import sort_students_time_selection
from sort import sort_students_g_avg_insertion
from sort import sort_students_failures_bubble


import load_data
from load_data import student_school_list
from load_data import student_age_list
from load_data import student_health_list
from load_data import student_failures_list
from load_data import add_average
#==========================================#
# Place your script for your text_UI after this line

def loadData():
    fileName = input("Please enter the name of the file: ")
    
    
    while True:
        attribute = input("Please enter the attribute to use as a filter: ")
        if attribute == "All" or attribute == "Age" or attribute == "School" or attribute == "Failures" or attribute == "Health":
            break
        else:
            print("Invalid entry. Please try again\n")
            
   
    if attribute == "All":
        return add_average(load_data.load_data(fileName, ("All", -1)))
    else:
        value = input("Please enter the value of the attribute: ")
        if type(value) == float:
            value = int(value)
            
    if attribute == "School":
        variable = add_average(student_school_list(fileName, value)) 
    elif attribute == "Age":
        variable = add_average(student_age_list(fileName, int(value)))      
    elif attribute == "Failures":
        variable = add_average(student_failures_list(fileName, int(value)))     
    elif attribute == "Health":
        variable = add_average(student_health_list(fileName, int(value)))
        
    print("\nData loaded\n")
    return variable


def sortData(studentList):
    while True:
        print("Please enter the attribute you want to use for sorting:")
        print("'Age'\t'StudyTime'\t'Failures'\t'G_Avg'")
        attribute = input(": ")
        if attribute == "Age" or attribute == "StudyTime" or attribute == "Failures" or attribute =="G_Avg":
            break
        else:
            print("\nInvalid commond.\n")
        
    while True:
        order = input("Ascending (A) or Descending (D) order: ").upper()
        if order == "A" or order == "D":
            break
        else:
            print("\nInvalid commond.\n")
            
    if attribute == "Age":
        sortVariable = sort_students_age_bubble(studentList, order)
    elif attribute == "StudyTime":
        sortVariable = sort_students_time_selection(studentList, order)
    elif attribute == "G_Avg":
        sortVariable = sort_students_g_avg_insertion(studentList, order)
    elif attribute == "Failures":
        sortVariable = sort_students_failures_bubble(studentList, order)        
    
    while True:
        shownCommonad = input("Data Sorted. Do you want to display the data?: ").upper()
        if shownCommonad == "Y" or shownCommonad == "N":
            if shownCommonad == "Y":
                print("\n")
                print(sortVariable)
                print("\n")
            break
        else:
            print("Invalid entry. Please enter Y or N\n")
    return sortVariable
       
   
   
   
def histogramData(infoList):
    histList = []
    histAttribute = input("Please enter the attribute you want to use for plotting: ")
    
    for student in infoList:
        for key in student:
            if key == histAttribute:
                histList.append({key : student[key]})
    return histogram(histList, histAttribute)
   
       


    
def curveFitData(infoList): 
    while True:
        curveAttribute = input("Please enter the attribute you want to use to find the best fit for G_Avg: ")
        if curveAttribute == "Age" or curveAttribute == "StudyTime" or curveAttribute == "Failures" or curveAttribute =="G_Avg" or curveAttribute =="Health" :
            break
        else:
            print("\nInvalid entry.\n")    
       
    
    
    
    while True:
        curveOrder = int(input("Please enter the order of the polynomial to be fitted: "))
        if curveOrder < 1:
            print("\nInvalid entry. Order must be 1 or greater\n")        
        
        else:          
            if curveOrder > 5:
                curveOrder = 5
            break


    newList = []
    element = 0
    dict1 = {}
    
    for student in infoList:
        dict1 = {}
        
        for key in student:
            #print(student[key])
            
            if key == "G_Avg":
                element = student[key]
                dict1[key] = element
                
        for key in student:
            if key == curveAttribute:
                element = student[key]
                dict1[key] = element  
                  
        newList.append(dict1)
        
    
    #print( curve_fit(newList, curveAttribute, curveOrder))
    print (curve_fit(newList, curveAttribute, curveOrder))
           
       
count = 0
while True:
    
    while True:
        
        while True:
            print("The available commands are:")
            print("     L)oad Data\n     S)ort Data\n     C)urve Fit\n     H)istogram\n     E)xit")
            userInput = input("\nPlease type your command: ").upper()
            if userInput == "L" or userInput == "S" or userInput == "C" or userInput == "H" or userInput == "E":
                break
            else:
                print("Invalid command.\n")
                
                
        #if count == 1: #Loop is exited if load data was already called
            #break
        if userInput == "L": #L is asked to load the data
            infoList = loadData() #Function called to load the data to a variable
            count = 1 #Will no need to run the load data later
            break
        elif userInput == "E":
            break
        
        if count == 1: #Loop is exited if load data was already called
            break        
 
        if userInput != "L":
            print("File not loaded. Please, load a file first.\n")
            
    if userInput == "E":
        break
    
    if userInput == "S":
        sortData(infoList) 
        
    if userInput == "C":
        curveFitData(infoList) 
        
    if userInput == "H":
        histogramData(infoList) 