# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Shifat Ghazi, Michael Aziz, Caleb Payne, Benjamin Goodyear"

# Update "" with your team (e.g. T102)
__team__ = "T115"

#==========================================#
# Place your sort_students_age_bubble function after this line

def sort_students_age_bubble(students: list[dict], order: str) -> list[dict]:
    """
    return the sorted list of students’ dictionaries by the “Age” attribute. If "Age" is a key in the dictionary, the function returns the sorted list in descending order "D" or ascending order "A" using the bubble sort algorithm. If "Age" is not a key in the dictionary, the function prints a message stating the key is not in the dictionary (e.g., "Age" key is not present) and returns the original list.

    preconditions: 
    parameter order should be a string "A" or "D" and it must be capitalized
    parameter students is a list of dictionnaires.

    >>> sort_students_age_bubble([{"Age":10,"School":"GP"},{"Age":19,"School":"MS"}], "D")
    [{'Age': 19, 'School': 'MS'}, {'Age': 10, 'School': 'GP'}]

    >>> sort_students_age_bubble([{"Age":19,"School":"GP"},{"Age":16,"School":"MS"}], "A")
    [{'Age': 16, 'School': 'MS'}, {'Age': 19, 'School': 'GP'}]

    >>> sort_students_age_bubble([{"School":"GP"}, {"School":"MS"}], "A")
    Age key is not present
    [{'School': 'GP'}, {'School': 'MS'}]

    """
    swap = True
    while swap:
        swap = False

        for i in range(len(students)):
            if "Age" not in students[i]:
                print("Age key is not present")
                return students

        for i in range(len(students) - 1):
            if order == "A":
                if students[i]["Age"] > students[i + 1]["Age"]:
                    aux = students[i]
                    students[i] = students[i + 1]
                    students[i + 1] = aux
                    swap = True

            elif order == "D":
                if students[i]['Age'] < students[i + 1]["Age"]:
                    aux = students[i]
                    students[i] = students[i + 1]
                    students[i + 1] = aux
                    swap = True

    return students


#==========================================#
# Place your sort_students_time_selection function after this line


def sort_students_time_selection(student_dictionaries: list, order: str):
    """This finction takes a list of dictionaries and if the 'order' parameter is 'A' will sort the dictionaries in accending order of study time, and if the 'order' parameter is 'D' will sort the dictionaries in decending order of study time. It will return the list original list if study time is not a key in the dictionary and prints a message saying as such.
    
    Preconditions: 
    student_dictionaries is a list of dictionaries
    order is a string == 'A' or 'D'
    
    >>>sort_students_time_selection([{"StudyTime":10.2,"School":"GP"}, {"StudyTime":19.1,"School":"MS"}], "D")
    [{'StudyTime': 19.1, 'School': 'MS'}, {'StudyTime': 10.2, 'School': 'GP'}]
    
    >>>sort_students_time_selection([{"StudyTime":16,"School":"GP"}, {"StudyTime":11.5,"School":"MS"}], "A")
    [{'StudyTime': 11.5, 'School': 'MS'}, {'StudyTime': 16, 'School': 'GP'}]
    
    >>>sort_students_time_selection()
    "StudyTime" key is not present
    [{'School': 'GP'}, {'School': 'MS'}]
    """
    if "StudyTime" in student_dictionaries[0]:
        if order == 'A':
            for i in range (len(student_dictionaries)):
                min_idx = 0
                for j in range(i + 1, len(student_dictionaries)):
                    if student_dictionaries[min_idx]["StudyTime"] > student_dictionaries[j]["StudyTime"]:
                        min_idx = j
                student_dictionaries[i], student_dictionaries[min_idx] = student_dictionaries[min_idx],student_dictionaries[i]
                return student_dictionaries
        
        else:
            for i in range (len(student_dictionaries)):
                max_idx = 0
                for j in range(i + 1, len(student_dictionaries)):
                    if student_dictionaries[max_idx]["StudyTime"] < student_dictionaries[j]["StudyTime"]:
                        max_idx = j
                student_dictionaries[i], student_dictionaries[max_idx] = student_dictionaries[max_idx],student_dictionaries[i]
                return student_dictionaries
            
    else:
        print('"StudyTime" key is not present')
        return student_dictionaries


#==========================================#
# Place your sort_students_g_avg_insertion function after this line

def sort_students_g_avg_insertion(studentList: list[dict], order: str) -> list[dict]:
    
    """
    Returns a randomized list of dictionaries in ascending or decending order specified based upon the "G_Avg" key values using the insertion sort method
    
    Precondition: No duplicate entries and keys in every dictionary are noted to be the same
    
    >>>sort_students_g_avg_insertion([{"G_Avg": 7.2, "School": "GP"}, {"G_Avg": 9.1, "School": "MS"}], "D")
    [{'G_Avg': 9.1, 'School': 'MS'}, {'G_Avg': 7.2, 'School': 'GP'}]
    
    >>>sort_students_g_avg_insertion([{"School":"GP"},{"School":"MS"}], "D")
    'G_Avg' key is not present.
    [{'School': 'GP'}, {'School': 'MS'}]
    
    
    >>>sort_students_g_avg_insertion([{"G_Avg": 9.2, "School": "GP"}, {"G_Avg": 9.1, "School": "MS"}, {"G_Avg": 7.3, "School": "MS", "Age": 7.3}], "A")
    [{'G_Avg': 7.3, 'School': 'MS', 'Age': 7.3}, {'G_Avg': 9.1, 'School': 'MS'}, {'G_Avg': 9.2, 'School': 'GP'}]
    
    """      
    checkList = []
    emptyList = []  
    counter = 0
    for dicts in studentList:
        for key in dicts:
            if key == "G_Avg":
                x = dicts["G_Avg"]
                emptyList.append(x)
        
            checkList.append(key)
            
            
        if "G_Avg" in checkList:
                counter += 1
        else:
                print("'G_Avg' key is not present.")
                return(studentList)            
                

    if order == "A":
        for i in range(1, len(emptyList)):
            key = emptyList[i]
                                    
                                    
            j = i-1
            while j >= 0 and key < emptyList[j]:
                    emptyList[j+1] = emptyList[j]
                    j -= 1
            emptyList[j+1] = key
                
    elif order == "D":
        for i in range(1, len(emptyList)):
            key = emptyList[i]
                                                       
            j = i-1
            while j >= 0 and key > emptyList[j]:
                    emptyList[j+1] = emptyList[j]
                    j -= 1
            emptyList[j+1] = key            
                    

    newList = []
    for x in emptyList:
            for dicts in studentList:
                    for key in dicts:
                        if key == "G_Avg":
                            y = dicts["G_Avg"]                
                            if x == y:
                                newList.append(dicts)                           
    return(newList)


#==========================================#
# Place your sort_students_failures_bubble function after this line

def sort_students_failures_bubble(studentlst: list, order: str) -> list:
        """ This function returns an updated list of dictionaries by sorting the 
        list of dictionaries by the Failures key value in either assending or 
        decending order. 
        Preconditions: order must be capitalized, the list of dictionaries needs
        proper dictionary notation.
        Examples: sort_students_failures_bubble([{"School":"GP"}, {"School":"MS"}], "D")
            will return: Failures” key is not present.
                         [{'School': 'GP'}, {'School': 'MS'}]
                  sort_students_failures_bubble([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "A")
            will return: [{'Failures': 10, 'School': 'GP'}, {'Failures': 19, 'School': 'MS'}]
                  sort_students_failures_bubble([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "D")
            will return: [{'Failures': 10, 'School': 'GP'}, {'Failures': 19, 'School': 'MS'}]
        """
        counter = 0
        checklist = []
        emptylst = []
        for dics in studentlst:
                for key in dics:
                        if key == "Failures":
                                x = dics["Failures"]
                                emptylst.append(x)
                        
                        checklist.append(key)
        
                if "Failures" in checklist:
                        counter += 1
                else:
                        print("Failures key is not present.")
                        return(studentlst)                                 
                        
        if order == "D":
                swap = True
                while swap:
                        swap = False
                        for i in range(len(emptylst) -1):
                                if emptylst[i] < emptylst[i+1]:
                                #swap
                                        aux = emptylst[i]
                                        emptylst[i] = emptylst[i+1]
                                        emptylst[i+1] = aux
                                        swap = True
        if order == "A":
                swap = True
                while swap:
                        swap = False
                        for i in range(len(emptylst) -1):
                                if emptylst[i] > emptylst[i+1]:
                                #swap
                                        aux = emptylst[i]
                                        emptylst[i] = emptylst[i+1]
                                        emptylst[i+1] = aux
                                        swap = True
        newlist = []
        for x in emptylst:
                for dics in studentlst:
                        for key in dics:
                                if key == "Failures":
                                        y = dics["Failures"]                
                                        if x == y:
                                                newlist.append(dics)
        return(newlist)


#==========================================#
# Place your sort function after this line

def sort(studentList: list, order: str, sortType: str) -> list:
    """
    Returns a randomized list of dictionaires in a ascending or descending order through a sorting method specified by the user
    
    Precondition: order needs to start with a capital letter and no duplicate entries
    
    >>>sort([{"StudyTime":10.2,"School":"GP"}, {"StudyTime":19.1,"School":"MS"}], "A", "G_Avg")
    'G_Avg' key is not present.
    [{'StudyTime': 10.2, 'School': 'GP'}, {'StudyTime': 19.1, 'School': 'MS'}]
    
    >>>sort([{"StudyTime":10.2,"School":"GP"}, {"StudyTime":19.1,"School":"MS"}], "D", "StudyTime")
    [{'StudyTime': 19.1, 'School': 'MS'}, {'StudyTime': 10.2, 'School': 'GP'}]
    
    >>>sort([{"Age":10,"School":"GP"},{"Age":19,"School":"MS"}], "D", "Age")
    [{'Age': 19, 'School': 'MS'}, {'Age': 10, 'School': 'GP'}]
    """
        
    if sortType == "Age":
        return sort_students_age_bubble(studentList, order)
    elif sortType == "StudyTime":
        return sort_students_time_selection(studentList, order)
    elif sortType == "G_Avg":
        return sort_students_g_avg_insertion(studentList, order)
    elif sortType == "Failures":
        return sort_students_failures_bubble(studentList, order)
    else:
        print("'" + sortType + "' cannot be sorted")
        return studentList
        

# Do NOT include a main script in your submission