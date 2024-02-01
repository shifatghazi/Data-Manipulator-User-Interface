# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Shifat Ghazi, Michael Aziz, Caleb Payne"

# Update "" with your team (e.g. T102)
__team__ = "T-115"

#==========================================#
# Place your student_school_list function after this line


def student_school_list(file_name: str, schoolName: str) -> list[dict]:
    """
    The function returns a list of students (stored as a dictionary) that attended the school provided as the input parameters.

    precondition: Preconditions: file_name must be a .csv file

    >>> student_school_list('student-mat.csv', 'GP')
    [ {'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6},{another element},…]


    >>> student_school_list('student-mat.csv', 'MB')
    [{'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5},{another element},… ]

    >>> student_school_list('student-mat.csv', 'MP')
    []


    """

    fileread = open(file_name, 'r')
    student_list = []
    for row in fileread:
        student = row.strip().split(',')
        if student[0] == str(schoolName):
            student_list.append({
                'Age': int(student[1]),
                'StudyTime': float(student[2]),
                'Failures': int(student[3]),
                'Health': int(student[4]),
                'Absences': int(student[5]),
                'G1': int(student[6]),
                'G2': int(student[7]),
                'G3': int(student[8])})

    fileread.close()
    return student_list


#==========================================#
# Place your student_health_list function after this line
def student_health_list(file_name: str, health_number: int) -> list[dict]:
    """
    this function returns a list of students, stored as a dictionary, whose health is equal to the value entered for health_number. The data is coming from the file inputted for file_name.

    Preconditions: file_name must be a .csv file

    >>>student_health_list('student-mat.csv', 3)
    [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {another element},…]
    >>>student_health_list('student-mat.csv', 1)
    [{'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6}, {another element},…]
    >>>student_health_list('student-mat.csv', 5)
    [{'School': 'MS', 'Age': 19, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 5, 'G1': 8, 'G2': 9, 'G3': 9}, {another element},…]

    """
    fileread = open(file_name, 'r')
    student_list = []
    for row in fileread:
        student = row.strip().split(',')
        if student[4] == str(health_number):
            student_list.append({
                'School': student[0],
                'Age': int(student[1]),
                'StudyTime': float(student[2]),
                'Failures': int(student[3]),
                'Absences': int(student[5]),
                'G1': int(student[6]),
                'G2': int(student[7]),
                'G3': int(student[8])})

    fileread.close()
    return student_list


#==========================================#
# Place your student_age_list function after this line

def student_age_list(file_name: str, age: int) -> list[dict]:
    """
    Returns a list of students (stored as a dictionary) with the same age as the input age parameter. If the age value provided is not on the file, the function returns an empty list.

    precondition:   age >= 15 and age <= 22 or it will return an empty list.

    >>> student_age_list('student-mat.csv', 15)
    [ {'School': 'GP', 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, {another element}, … ]

    >>> student_age_list('student-mat.csv', 1)
    []

    >>> student_age_list('student-mat.csv', 18)
    [ {'School': 'MS', 'StudyTime': 2.0, 'Failues': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {another element}, … ]


    """

    with open(file_name, 'r') as file:

        lines = file.readlines()

        headers = lines[0].strip().split(',')

        matching_students = []

        for line in lines[1:]:

            data = line.strip().split(',')

            if int(data[headers.index('Age')]) == age:

                student_data = {

                    'School': data[headers.index('School')],
                    'StudyTime': float(data[headers.index('StudyTime')]),
                    'Failures': int(data[headers.index('Failures')]),
                    'Health': int(data[headers.index('Health')]),
                    'Absences': int(data[headers.index('Absences')]),
                    'G1': int(data[headers.index('G1')]),
                    'G2': int(data[headers.index('G2')]),
                    'G3': int(data[headers.index('G3')]),
                }

                matching_students.append(student_data)

        return matching_students


#==========================================#
# Place your student_failures_list function after this line

def student_failures_list(fileName: str, failureNum: int) -> list[dict]:
    """
    Returns a list of dicitionries of information in the order of school, age, studytime, failures, health, absences, G1, G2, and G3 from the specified .csv file and failure count

    Precondition: fileName must be a .csv file

    >>> student_failures_list("student-mat.csv", 3)
    [{'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, {another element}, ...]

    >>> student_failures_list("student-mat.csv", 1)
    [{'School': 'GP', 'Age': 16, 'StudyTime': 2.0, 'Health': 3, 'Absences': 25, 'G1': 7, 'G2': 10, 'G3': 11}, {another element}, ...]

    >>> student_failures_list("student-mat.csv", 10)
    []
    """
    fileRead = open(fileName, 'r')
    studentList = []
    for i in fileRead:
        student = i.strip().split(',')
        if student[3] == str(failureNum):
            studentList.append({
                "School": student[0],
                "Age": int(student[1]),
                "StudyTime": float(student[2]),
                "Health": int(student[4]),
                "Absences": int(student[5]),
                "G1": int(student[6]),
                "G2": int(student[7]),
                "G3": int(student[8])})

    fileRead.close
    return studentList


#==========================================#
# Place your load_data function after this line

def load_data(file_name: str, filtered: tuple) -> list[dict]:
    """
    returns as a list of students (stored as a dictionary) where the keys of the dictionary are the labels for all attributes in the spreadsheet except for the attribute in 
    the first item of the tuple. If the first item of the tuple is invalid, the function will print the error message "Invalid Value" and return an empty list.

    precondition: file_name must be a .csv file

    >>> load_data('student-mat.csv', ('Failures', 0))
    [ {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6},{another element},…] 

    >>> load_data('student-mat.csv', ('All', -1))
    [ {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6},{another element}, … ] 

    >>> load_data('student-mat.csv', ('G1', 10))
    Invalid Value 
    [] 

    """

    if filtered[0] == "All":
        fileRead = open(file_name, 'r')
        studentList = []
        for i in fileRead:
            student = i.strip().split(',')
            if student[0] != "School":
                studentList.append({
                    "School": student[0],
                    "Age": int(student[1]),
                    "StudyTime": float(student[2]),
                    "Failures": int(student[3]),
                    "Health": int(student[4]),
                    "Absences": int(student[5]),
                    "G1": int(student[6]),
                    "G2": int(student[7]),
                    "G3": int(student[8])})

        fileRead.close
        return studentList

    else:
        if filtered[0] == "School":
            return student_school_list(file_name, filtered[1])

        elif filtered[0] == "Age":
            return student_age_list(file_name, filtered[1])

        elif filtered[0] == "Health":
            return student_health_list(file_name, filtered[1])

        elif filtered[0] == "Failures":
            return student_failures_list(file_name, filtered[1])

        else:
            print("invalid data")
            return []


#==========================================#
# Place your add_average function after this line

def add_average(student_dict_list) -> list[dict]:
    """
    returns the list with the dictionaries updated with the average grade.

    precondition: student_dict_list must be a list of student dictionaries

    >>> add_average([ {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {another element}, … ])
    [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}, {another element}, … ])

    >>> add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {another element}, … ])
    [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}, {another element}, … ])

    >>> add_average ([{'School': 'MS', 'Age': 19, 'StudyTime': 1, 'Failures': 0, 'Absences': 5, 'G1': 8, 'G2': 9, 'G3': 9}, {another element}, … ])
    [{'School': 'MS', 'Age': 19, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 5, 'G1': 8, 'G2': 9, 'G3': 9, 'G_Avg': 8.67}, {another element}, …]


    """
    row = 0
    for studentRow in student_dict_list:
        avg = round(
            (studentRow['G1'] + studentRow['G2'] + studentRow['G3']) / 3, 2)
        student_dict_list[row]['G_Avg'] = avg
        row += 1
    return student_dict_list


# Do NOT include a main script in your submission.