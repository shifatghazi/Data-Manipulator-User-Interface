# ECOR 1042 Lab 6 - Individual submission for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Benjamin Goodyear"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101273578"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T115"

#==========================================#
# Place your curve_fit function after this line
import numpy as np
import matplotlib.pyplot as plt
def curve_fit(lst: dict, string: str, degree: int) ->list:
      """ This function takes an input of a list of dictionaries with G-Avg and 
      another paramater and outputs the function that includes all the points of
      the average of all G_Avg values for the numerical value of the second input 
      parameter to the degree specified.
     
      *Preconditions: the dictionaries in the list must not contain any key values 
      that aren't integers or floats, the string input must be a key in the 
      dictionaries, the degree input must be an integer.
      
      *Examples: 
      >>>curve_fit([{"G_Avg": 6, "Health":1},{"G_Avg": 4, "Health":1},{"G_Avg": 2, "Health":1},{"G_Avg": 12, "Health":2},{"G_Avg": 8, "Health":2},{"G_Avg": 4, "Health":2},{"G_Avg": 18, "Health":3},{"G_Avg": 12, "Health":3},{"G_Avg": 6, "Health":3}],'Health', 2)
      will return:-1.696168591402491e-15x^2 + 2.000000000000005x + 1.9999999999999922
      >>>curve_fit([{"G_Avg": 6, "Health":1},{"G_Avg": 4, "Health":1},{"G_Avg": 2, "Health":1},{"G_Avg": 12, "Health":2},{"G_Avg": 8, "Health":2},{"G_Avg": 4, "Health":2},{"G_Avg": 18, "Health":3},{"G_Avg": 12, "Health":3},{"G_Avg": 6, "Health":3}],'Health', 1)
      will return: 1.9999999999999991x + 2.0000000000000044
      >>>curve_fit([{"G_Avg": 6, "Health":1},{"G_Avg": 4, "Health":1},{"G_Avg": 2, "Health":1},{"G_Avg": 12, "Health":2},{"G_Avg": 8, "Health":2},{"G_Avg": 4, "Health":2},{"G_Avg": 18, "Health":3},{"G_Avg": 12, "Health":3},{"G_Avg": 6, "Health":3}],'Health', 4)
      will return: -1.696168591402491e-15x^2 + 2.000000000000005x + 1.9999999999999922
      """
      xset = set()
      for dicts in lst:
            for element in dicts:
                  if element == string:
                        insert = dicts.get(string)
                        xset.add(insert)
      xlst = list(xset)
      x = xlst
      emptylist = []
      y = []
      for num in xlst:
            starter = 0
            emptylist.clear()
            for dicts in lst:
                  for element in dicts:
                        if num == dicts.get(string):
                              emptylist.append(dicts.get("G_Avg"))
                              
            for item in emptylist:
                  starter += item
            y_value = (starter/len(emptylist))
            y.append(y_value)
            
      if degree > (len(x) - 1):
            degree = (len(x) - 1)
      
      z = np.polyfit(x, y, degree)
      empstr = ""
      plus = " + "
      counter = 1
      counter2 = 1
      
      for item in z:
      
            exp = len(z) - counter
            
            if item < 0 :
                  neg = abs(item)
                  if exp == 0:
                        term = " - " + str(neg)
                        counter2 += 1
                  else:
                        term = " -" + str(neg) + "x^" + str(exp) 
                        counter2 += 1
      
            elif item > 0:
                  if counter2 == 1:
                        term = str(item) + "x^" + str(exp)
                        counter2 += 1

                  if exp == 0:
                        term = " + " + str(item)
                        counter2 += 1
                  else:
                        term =  " + " + str(item) + "x^" + str(exp) 
                        counter2 += 1                        
                  
                  
            empstr += str(term) 
            counter += 1
  
            
      return('y =  ' + empstr)  