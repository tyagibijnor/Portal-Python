from statistics import mean as m

admins = {'Python':'Python','demo':'demo'}

studentDict = {'Victor':[78,88,93],
               'James':[50,40,54],
               'Navneet':[82,54,69]}

def main():
    print("""
    Welcome to Grade System

    1.Add Grade
    2.Remove Student
    3.Average of Grade
    4.List All
    5.Exit
    """)
    action = input('What action will you do: ')
    if action=='1':
        enterGrade()        
    elif action=='2':
        removeStudent()
    elif action=='3':
        gradeAvgStudent()
    elif action=='4':
        showListStudent()
    elif action=='5':
        exit()
    else:
        print('Wrong Selection')

def enterGrade():
    nameToEnter = input('Student Name: ')
    gradeToEnter = input('Grade: ')
    if nameToEnter in studentDict:
        print('Adding Grade...')
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('Student does not exist.')
    print(studentDict)

def showListStudent():
	for key in studentDict.keys():
	    print(key)
		
def removeStudent():
    nameToRemove = input('Student Name: ')
    if nameToRemove in studentDict:
        print('Removing Student...')
        del studentDict[nameToRemove]
    else:
        print('Student does not exist.')           

    print(studentDict)
    
def gradeAvgStudent():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)
    print(eachStudent,'has average grade of',avgGrade)
    
login = input('Username: ')
passw = input('Password: ')

if login in admins:
    if admins[login] == passw:
        print('Welcome, ',login)
        while True:
            main()
    else:
        print('Invalid password')
else:
    print('Invalid username')
    
