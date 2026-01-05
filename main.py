from pyscript import display, document

subjects = ['science','ss','english','filipino', 'tle', 've'] # using Tuples for the subjects
units = (5,3,5,3,1,1) # using list for the units

def give(e):
    first_name = document.getElementById("first-name").value
    last_name = document.getElementById("last-name").value
    
    science_score = int(document.getElementById (subjects[0]).value)
    ss_score = int(document.getElementById (subjects[1]).value)
    english_score = int(document.getElementById (subjects[2]).value)
    filipino_score = int(document.getElementById (subjects[3]).value)
    TLE_score = int(document.getElementById (subjects[4]).value)
    VE_score = int(document.getElementById (subjects[5]).value)

    science_average = science_score * units[0]
    ss_average = ss_score * units[1]
    english_average = english_score * units[2]
    filipino_average = filipino_score * units[3]
    TLE_average = TLE_score * units[4]
    VE_average = VE_score * units[5]

    total_units = units[0] + units[1] + units[2] + units[3] + units[4] + units[5]
    average = (science_average + ss_average + english_average + filipino_average + TLE_average + VE_average) / total_units

    document.getElementById("output").innerHTML = ''

    display(f"Name: {first_name} {last_name}", target='output')
    display("Average:", target="output")
    display(f"{subjects[0]}: {science_score}", target="output")
    display(f"{subjects[1]}: {ss_score}", target="output")
    display(f"{subjects[2]}: {english_score}", target="output")
    display(f"{subjects[3]}: {filipino_score}", target="output")
    display(f"{subjects[4]}: {TLE_score}", target="output")
    display(f"{subjects[5]}: {VE_score}", target="output")

    display(f"General Weighted Average: {average}", target="output")

if average > 75:
        display(f'You passed', target='output')
    else:
        display(f'You failed', target='output')  




