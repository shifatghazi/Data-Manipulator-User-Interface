# ECOR 1042 Lab 4 - team submission

#import check module here
import check

#import load_data module here
import load_data
from load_data import student_school_list
from load_data import student_age_list
from load_data import student_health_list
from load_data import student_failures_list
from load_data import add_average

# Update "" with your the name of the active members of the team
__author__ = "Shifat Ghazi, Michael Aziz, Caleb Payne"

# Update "" with your student number (e.g., 100100100)

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-115"
#==========================================#

# Place test_return_list function here 
def test_return_list():
    # Complete the function with your test cases

    # test that student_school_list returns a list (3 different test cases required)

    check.equal(
        type(load_data.student_school_list("student-test.csv", "GP")), list)
    check.equal(
        type(load_data.student_school_list("student-test.csv", "MB")), list)
    check.equal(
        type(load_data.student_school_list("student-test.csv", "MS")), list)

    # test that student_age_list returns a list (3 different test cases required)

    check.equal(
        type(load_data.student_age_list("student-test.csv", 14)), list)
    check.equal(
        type(load_data.student_age_list("student-test.csv", 10)), list)
    check.equal(
        type(load_data.student_age_list("student-test.csv", 20)), list)

    # test that student_health_list returns a list (3 different test cases required)

    check.equal(
        type(load_data.student_health_list("student-test.csv", 1)), list)
    check.equal(
        type(load_data.student_health_list("student-test.csv", 2)), list)
    check.equal(
        type(load_data.student_health_list("student-test.csv", 4)), list)

    # test that student_failures_list returns a list (3 different test cases required)

    check.equal(
        type(load_data.student_failures_list("student-test.csv", 1)), list)
    check.equal(
        type(load_data.student_failures_list("student-test.csv", 2)), list)
    check.equal(
        type(load_data.student_failures_list("student-test.csv", 6)), list)

    # test that load_data returns a list (6 different test cases required)

    
    check.equal(type(load_data.load_data(
        'student-test.csv', ('Failures', 0))), list)
    check.equal(type(load_data.load_data(
        'student-test.csv', ('All', -1))), list)
    check.equal(type(load_data.load_data(
        'student-test.csv', ('Health', 4))), list)
    check.equal(type(load_data.load_data(
        'student-test.csv', ('All', 0))), list)
    check.equal(type(load_data.load_data(
        'student-test.csv', ('Health', 1))), list)
    check.equal(type(load_data.load_data(
        'student-test.csv', ('School', 'BD'))), list)
    
  

    # test that add_average returns a list (3 different test cases required)
    check.equal(type(load_data.add_average(
        load_data.load_data('student-test.csv', ('Failures', 0)))), list)
    check.equal(type(load_data.add_average(
        load_data.load_data('student-test.csv', ('School', 'BD')))), list)
    check.equal(type(load_data.add_average(
        load_data.load_data('student-test.csv', ('Age', 16)))), list)

    check.summary()

# Place test_return_list_correct_lenght function here
def test_return_list_correct_lenght():
    
    #test that student_school_list returns a list with the correct lenght (3 different test cases required)
    check.equal(len(student_school_list("student-test.csv", "GP")), 3)
    check.equal(len(student_school_list("student-test.csv", "MB")), 2)
    check.equal(len(student_school_list("student-test.csv", "CF")), 3)
    
    #test that student_age_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(student_age_list("student-test.csv", 18)), 4)
    check.equal(len(student_age_list("student-test.csv", 17)), 6)
    check.equal(len(student_age_list("student-test.csv", 15)), 3)    
    
    #test that student_health_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(student_health_list("student-test.csv", 3)), 8)
    check.equal(len(student_health_list("student-test.csv", 5)), 3)
    check.equal(len(student_health_list("student-test.csv", 4)), 3)    
    
    #test that student_failures_list returns a list   with the correct lenght(3 different test cases required)
    check.equal(len(student_failures_list("student-test.csv", 0)), 11)
    check.equal(len(student_failures_list("student-test.csv", 3)), 1)
    check.equal(len(student_failures_list("student-test.csv", 2)), 2)    
    
    #test that load_data returns a list  with the correct lenght (6 different test cases required)
    check.equal(len(load_data.load_data("student-test.csv", ("School", "GP"))), 3)
    check.equal(len(load_data.load_data("student-test.csv", ("School", "MB"))), 2)
    check.equal(len(load_data.load_data("student-test.csv", ("School", "CF"))), 3)
    check.equal(len(load_data.load_data("student-test.csv", ("Failures", 0))), 11)
    check.equal(len(load_data.load_data("student-test.csv", ("Age", 18))), 4)
    check.equal(len(load_data.load_data("student-test.csv", ("Age", 17))), 6)
    
     #test that add_average returns a list   with the correct lenght (3 different test cases required)
    check.equal(len(load_data.add_average(load_data.load_data("student-test.csv", ("School", "GP")))), 3)
    check.equal(len(load_data.add_average(load_data.load_data("student-test.csv", ("School", "MB")))), 2)
    check.equal(len(load_data.add_average(load_data.load_data("student-test.csv", ("School", "CF")))), 3)
    
    check.summary()
    



#Place test_return_correct_dict_inside_list function here
def test_return_correct_dict_inside_list():
    #Complete the function with your test cases
    
    #test that student_school_list returns a correct dictionary inside the list (3 different test cases required)
    check.equal(student_school_list('student-test.csv', 'GP')[0], {'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(student_school_list('student-test.csv', 'MB')[0], {'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5})
    check.equal(student_school_list('student-test.csv', 'CF')[0], {'Age': 15, 'StudyTime': 5.0, 'Failures': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7})
    
    #test that student_age_list returns a correct dictionary inside the list  (3 different test cases required)
    check.equal(student_age_list('student-test.csv', 15)[0], {'School': 'GP', 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10})
    check.equal(student_age_list('student-test.csv', 18)[0], {'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(student_age_list('student-test.csv', 1), [])
                
    #test that student_health_list returns a correct dictionary inside the list  (3 different test cases required)
    check.equal(student_health_list('student-test.csv', 1), [{'School': 'MS', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9}])
    check.equal(student_health_list('student-test.csv', 3)[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(student_health_list('student-test.csv', 5)[0], {'School': 'CF', 'Age': 16, 'StudyTime': 2.0, 'Failures': 1, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12})
                
    #test that student_failures_list returns a correct dictionary inside the list (3 different test cases required)
    check.equal(student_failures_list('student-test.csv', 3), [{'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}])
    check.equal(student_failures_list('student-test.csv', 1), [{'School': 'CF', 'Age': 16, 'StudyTime': 2.0, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}])
    check.equal(student_failures_list('student-test.csv', 10), [])
                
    #test that load_data returns a correct dictionary inside the list (6 different test cases required)
    check.equal(load_data.load_data('student-test.csv', ('Failures', 0))[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(load_data.load_data('student-test.csv', ('All', -1))[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(load_data.load_data('student-test.csv', ('Health', 20)), [])
    check.equal(load_data.load_data('student-test.csv', ('Health', 4))[0], {'School': 'BD', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 10, 'G2': 9, 'G3': 9})
    check.equal(load_data.load_data('student-test.csv', ('Age', 17))[0], {'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6})
    check.equal(load_data.load_data('student-test.csv', ('Health', 5))[0], {'School': 'CF', 'Age': 16, 'StudyTime': 2.0, 'Failures': 1, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12})

    
    #test that add_average returns a lcorrect dictionary inside the list  (3 different test cases required)
    check.equal(add_average([ {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}]), [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}])
    check.equal(add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}]), [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}])
    check.equal(add_average([{'School': 'MS', 'Age': 19, 'StudyTime': 1, 'Failures': 0, 'Absences': 5, 'G1': 8, 'G2': 9, 'G3': 9}]), [{'School': 'MS', 'Age': 19, 'StudyTime': 1, 'Failures': 0, 'Absences': 5, 'G1': 8, 'G2': 9, 'G3': 9, 'G_Avg': 8.67}])
    
    check.summary()


#Place test_add_average function here
def test_add_average():
    #Complete the function with your test cases
    
    #test that the function does not change the lengh of the list provided as input parameter (5 different test cases required)
    check.equal(len(load_data.add_average(load_data.student_school_list('student-test.csv', 'GP'))), len(load_data.student_school_list('student-test.csv', 'GP')))
    check.equal(len(load_data.add_average(load_data.student_health_list('student-test.csv', 4))), len(load_data.student_health_list('student-test.csv', 4)))
    check.equal(len(load_data.add_average(load_data.student_age_list('student-test.csv', 15))), len(load_data.student_age_list('student-test.csv', 15)))
    check.equal(len(load_data.add_average(load_data.student_failures_list('student-test.csv', 2))), len(load_data.student_failures_list('student-test.csv', 2)))
    check.equal(len(load_data.add_average(load_data.load_data('student-test.csv', ('All', 0)))), 15)
    
    #test that the function returns an empty list when it is called whith an empty list
    check.equal(add_average([]), [])
    
    #test that the function inscrememnts the number of keys of the dictionary inside the list by one  (5 different test cases required)
    check.equal(len(load_data.add_average(load_data.student_school_list('student-test.csv', 'MB'))[0]), 9)
    check.equal(len(load_data.add_average(load_data.student_health_list('student-test.csv', 3))[0]), 9)
    check.equal(len(load_data.add_average(load_data.student_age_list('student-test.csv', 17))[0]), 9)
    check.equal(len(load_data.add_average(load_data.student_failures_list('student-test.csv', 1))[0]), 9)
    check.equal(len(load_data.add_average(load_data.load_data('student-test.csv',('All', 0)))[0]), 10)
    
    #test that the G_Avg value is properly calculated  (5 different test cases required)
    check.equal(add_average([{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}])[0]['G_Avg'], 5.67)
    check.equal(add_average([{'School': 'BD', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 8}])[0]['G_Avg'], 8.00)
    check.equal(add_average([{'School': 'CF', 'StudyTime': 5.0, 'Failures': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}])[0]['G_Avg'], 7.00)
    check.equal(add_average([{'School': 'MB', 'Age': 16, 'StudyTime': 2.0, 'Health': 3, 'Absences': 2, 'G1': 5, 'G2': 5, 'G3': 5}])[0]['G_Avg'], 5.00)
    check.equal(add_average([{'School': 'MS', 'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Health': 4, 'Absences': 8, 'G1': 11, 'G2': 10, 'G3': 10}])[0]['G_Avg'], 10.33)
    
    check.summary()



# Do NOT include a main script in your submission
