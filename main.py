from pyscript import display, document

subjects = ['Science','SS','English','Filipino', 'TLE', 'VE'] # using Tuples for the subjects
units = (5,3,5,3,1,1) # using list for the units

def funct(e):
    first_name = document.getElementById("first-name").value
    last_name = document.getElementById("last-name").value
    
    science_score = int(document.getElementById (subjects[0]).value)
    ss_score = int(document.getElementById (subjects[1]).value)
    english_score = int(document.getElementById (subjects[0]).value)
    filipino_score = int(document.getElementById (subjects[0]).value)
    TLE_score = int(document.getElementById (subjects[0]).value)
    VE_score = int(document.getElementById (subjects[0]).value)
    
    science_average = science_score * units[0]
    ss_average = ss_score * units[1]
    english_average = english_score * units[2]
    

    display(subjects(0), output='SubjectA')
    display(subjects(1), output='SubjectB')
    display(subjects(2), output='SubjectC')
    display(subjects(3), output='SubjectD')
    display(subjects(4), output='SubjectE')
    display(subjects(5), output='SubjectF')
    display(subjects(6), output='SubjectG')

