from os import rename, remove
from random import randint

# Adding Student records in Student File
def addrec():
    p = []
    no = admcode()
    fout = open('STUDENT_FILE.txt', 'a')
    for k in range(n):
        no = no + 1
        print('\n')
        # Input Roll Number
        roll = int(input("Input Roll number: "))
        # Input Class
        cla = int(input('Input Class: '))
        # Input Section
        sec = input("Input Section: ")
        while True:
            # Input Employee Name
            na = input('Student Name: ')
            if not na.isalnum() or na.isdigit():
                print('PLEASE ENTER VALID STUDENT NAME')
                na = input('Student Name: ')
            elif na.isalpha() and len(na) <= 2 :
                print('PLEASE ENTER VALID STUDENT NAME')
                na = input('Student Name: ')
            else:
                break
        # Input Student Gender
        gender = input('Gender [F/M]? ')
        while True:
            if not gender.isalpha():
                print('PLEASE ENTER ENDER AS EITHER F- FEMALE OR M- MALE')
                gender = input('Gender [F/M]? ')
            elif gender.isalpha() and len(gender) != 1 :
                print('PLEASE ENTER ENDER AS EITHER F- FEMALE OR M- MALE')
                gender = input('Gender [F/M]? ')
            elif gender.upper() != 'F' and gender.upper() != 'M' :
                print('PLEASE ENTER ENDER AS EITHER F- FEMALE OR M- MALE')
                gender = input('Gender [F/M]? ')
            else:
                break
        # Input Date of Birth details
        print('ENTER STUDENT DATE OF BIRTH DETAILS')
        dob = dateval()
        while len(dob) != 10:
            print(dob)
            print('PLEASE ENETER VALID DATE OF BIRTH')
            dob = dateval()
        # Input Mother's Name
        m_name= input("Input Mother's Name: ")
        # Input Father's Name
        f_name= input("Input Father's Name: ")
        # Input Phone number
        pn = input("Input Phone Number: ")
        validphone = phonevalidate(pn)
        if len(pn) == 10:
            while validphone == 1:
                print('Please enter New Phone Number as it already exists')
                pn = input('Phone Number? ')
                validphone = phonevalidate(pn)
            while True:
                if pn in p:
                    print('Please enter New Phone Number as it already exists')
                    pn = input('Phone Number? ')
                else:
                    p += [pn]
                    break
        else:
            print('Please enter New Phone Number with 10 digits')
            pn = input('Phone Number? ')
            validphone = phonevalidate(pn)
            while True:
                if pn in p:
                    print('Please enter New Phone Number as it already exists')
                    pn = input('Phone Number? ')
                else:
                    p += [pn]
                    break
        # Input Stream Code
        print('=' * 40)
        print(' SB  Science with Biology')
        print(' SC  Science with Computer Science')
        print(' SE  Science with Economice')
        print(' CM  Commerce with Mathematics')
        print(' CI  Commerce with Informatics Practices')
        print(' HU  Humanities')
        print('=' * 40)
        sc = input("Input Stream Code: ")
        print('-' * 75)

        data = str(no) + ',' + str(roll) + ',' + str(cla) + ',' + sec.upper() + ',' + na.upper() + ',' + dob + ',' + m_name.upper() + ',' + f_name.upper() + ',' + str(pn) + ',' + gender.upper() + ',' + sc.upper() + '\n'
        fout.write(data)
    print('STUDENT RECORDS ADDED SUCCESSFULLY!\n')
    fout.close()

# Adding Student records in Result File 
def res_file():
    # Input Year
    y = int(input('Year for Result File: '))
    file_name = 'RESULT_FILE_' + str(y) + '.txt'
    fout = open(file_name, 'a')
    # Input Admission Number
    no = input('Admission Number: ')
    fin = open('STUDENT_FILE.txt', 'r')
    for line in fin:
        line = line.strip()
        arr = line.split(',')
        if arr[0] == str(no):
            print('Student Name  :', arr[4])
            print('Roll Number: ', arr[1])
            print('Class: ', arr[2])
            print('Section: ', arr[3])
            print('Stream Code: ', arr[-1])
            print('\nENTER MARKS OUT OF 100:')
            if arr[-1] == 'SB':
                print('Science with Biology'.upper())
            elif arr[-1] == 'SC':
                print('Science with Computer Science'.upper())
            elif arr[-1] == 'SE':
                print('Science with Economics'.upper())
            elif arr[-1] == 'CM':
                print('Commerce with Mathematics'.upper())
            elif arr[-1] == 'CI':
                print('Commerce with Informatics Practices'.upper())
            elif arr[-1] == 'HU':
                print('Humanities'.upper())
            print('-' * 90)
            print('STREAM\t SUBJECT1\tSUBJECT2\tSUBJECT3\tSUBJECT4\tSUBJECT5')
            print('-' * 90)
            print(' SE\t English\tMathematics\tPhysics\t\tChemistry\tEconomics')
            print(' SC\t English\tMathematics\tPhysics\t\tChemistry\tComputer Sc')
            print(' SB\t English\tMathematics\tPhysics\t\tChemistry\tBiology')
            print(' CM\t English\tMathematics\tEconomics\tAccountancy\tBusiness St')
            print(' CI\t English\tEconomics\tAccountancy\tBusiness St\tInformatics Prac')
            print(' HU\t English\tHistory\t\tGeography\tEconomics\tPolitical Sc')
            print('-' * 90)
            sub1 = float(input('Marks in Subject 1: '))
            sub2 = float(input('Marks in Subject 2: '))
            sub3 = float(input('Marks in Subject 3: '))
            sub4 = float(input('Marks in Subject 4: '))
            sub5 = float(input('Marks in Subject 5: '))
            grade1 = grade_calc(sub1)
            grade2 = grade_calc(sub2)
            grade3 = grade_calc(sub3)
            grade4 = grade_calc(sub4)
            grade5 = grade_calc(sub5)
            total = round(sub1 + sub2 +sub3 + sub4 +sub5, 2)
            avg = round(total/5, 2)
            if sub1 >= 33 and sub2 >= 33 and sub3 >= 33 and sub4 >= 33 and sub5 >= 33:
                if avg >= 60:
                    div = 'I'
                elif 50 <= avg < 60:
                    div = 'II'
                elif avg < 50:
                    div = 'III'
            else:
                if sub1 < 33 or sub2 < 33 or sub3 < 33 or sub4 < 33 or sub5 < 33:
                    div = 'CO'
                else:
                    div = 'FA'
            print('\n')
            print('Subject 1: ', sub1, '\t', 'Grade 1: ', grade1)
            print('Subject 2: ', sub2, '\t', 'Grade 2: ', grade2)
            print('Subject 3: ', sub3, '\t', 'Grade 3: ', grade3)
            print('Subject 4: ', sub4, '\t', 'Grade 4: ', grade4)
            print('Subject 5: ', sub5, '\t', 'Grade 5: ', grade5)
            print('Total: ', total, '\t\t', 'Average: ', avg)
            print('\nADDED SUCCESSFULLY IN RESULT FILE!\n')
            data = str(no) + ',' + arr[1] + ',' + arr[4] + ',' + str(sub1) + ',' + grade1 + ',' + str(sub2) + ',' + grade2 + ',' + str(sub3) + ',' + grade3 + ',' + str(sub4) + ',' + grade4 + ',' + str(sub5) + ',' + grade5 + ',' + str(total) + ',' + str(avg) + ',' + div + '\n'
            fout.write(data)
    fout.close()

# Modifying Student records in Student File

# Modifying Roll Number
def modif1():
    fin = open('STUDENT_FILE.txt', 'r')
    fout = open('TEMPORARY.txt', 'w')
    # Input Admission Number
    no = int(input('Admission Number to change Roll Number: '))
    # Input New Admission Number
    newroll = input('New Roll Number: ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name: ', arr[4])
            print('Roll Number: ', arr[1])
            print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[1] = newroll
                print('ROLL NUMBER UPDATED!\n')
            else:
                print('ROLL NUMBER NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: ADMISSION NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('STUDENT_FILE.txt')
    rename('TEMPORARY.txt', 'STUDENT_FILE.txt') 

# Modifying Class
def modif2():
    fin = open('STUDENT_FILE.txt', 'r')
    fout = open('TEMPORARY.txt', 'w')
    # Input Admission Number
    no = int(input('Admission Number to change Class: '))
    # Input New Class
    newcla = input('New Class: ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name: ', arr[4])
            print('Class: ', arr[2])
            print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[2] = newcla
                print('CLASS UPDATED!\n')
            else:
                print('CLASS NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: ADMISSION NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('STUDENT_FILE.txt')
    rename('TEMPORARY.txt', 'STUDENT_FILE.txt')

# Modifying Section
def modif3():
    fin = open('STUDENT_FILE.txt', 'r')
    fout = open('TEMPORARY.txt', 'w')
    # Input Admission Number
    no = int(input('Admission Number to change Section: '))
    # Input New Section
    newsec = input('New Section: ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name: ', arr[4])
            print('Section: ', arr[3])
            print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[2] = newsec
                print('SECTION UPDATED!\n')
            else:
                print('SECTION NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: ADMISSION NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('STUDENT_FILE.txt')
    rename('TEMPORARY.txt', 'STUDENT_FILE.txt')

# Modifying Date of Birth
def modif4():
    fin = open('STUDENT_FILE.txt', 'r')
    fout = open('TEMPORARY.txt', 'w')
    # Input Admission Number
    no = input('Admission Number to change Date of Birth: ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name: ', arr[4])
            print('Date of Birth: ', arr[5])
            print('Enter a Correct Date of Birth')
            newdob = dateval()
            while len(newdob) != 10:
                print(newdob)
                print('Please enter Correct Date of Birth')
                newdob = dateval()
            print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[5] = newdob
                print('DATE OF BIRTH UPDATED SUCCESSFULLY!\n')
            else:
                print('DATE OF BIRTH NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: ADMISSION NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('STUDENT_FILE.txt')
    rename('TEMPORARY.txt', 'STUDENT_FILE.TXT')

# Modifying Phone Number
def modif5():
    fin = open('STUDENT_FILE.txt', 'r')
    fout = open('TEMPORARY.txt', 'w')
    # Input Admission Number
    no = int(input('Admission Number to change Phone Number: '))
    # Input New Phone Number
    newpn = input('New Phone Number: ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name: ', arr[4])
            print('Phone Number: ', arr[8])
            print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[8] = newpn
                print('PHONE NUMBER UPDATED!\n')
            else:
                print('PHONE NUMBER NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: ADMISSION NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('STUDENT_FILE.txt')
    rename('TEMPORARY.txt', 'STUDENT_FILE.txt')

# Modifying Stream Code
def modif6():
    fin = open('STUDENT_FILE.txt', 'r')
    fout = open('TEMPORARY.txt', 'w')
    # Input Admission Number
    no = int(input('Admission Number to change Stream Code: '))
    # Input New Stream Code
    newsc = input('New Stream Code: ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name: ', arr[4])
            print('Stream Code: ', arr[-1])
            print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[-1] = newsc
                print('STREAM CODE UPDATED!\n')
            else:
                print('STREAM CODE NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: ADMISSION NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('STUDENT_FILE.txt')
    rename('TEMPORARY.txt', 'STUDENT_FILE.txt')

# Delete Student Record
def delete():
    fin = open('STUDENT_FILE.txt', 'r')
    fout = open('TEMPORARY.txt', 'a')
    # Input Admission Number
    no = int(input('Admission Number to delete? '))
    # Input Student Name
    na = input('Student Name to delete? ')
    found = 0
    for data in fin:
        arr = data.split(',')
        if int(arr[0]) == no and arr[4] == na.upper():
            found = 1
            print('Name: ', arr[4], '\t\t\t\t', 'Admission Number: ', arr[0])
            print('Class: ', arr[2], '\t\t\t\t', 'Grade: ', arr[3])
            print('Date of Birth: ', arr[5], '\t\t', 'Stream Code: ', arr[-1])
            print('Are you sure you want to delete?\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                print('\nSTUDENT RECORD SUCCESSFULLY DELETED!\n')
            else:
                print('\nSTUDENT RECORD NOT DELETED!\n')
        else:
            fout.write(data)
    fout.close()
    fin.close()
    if found == 0:
        print('\nERROR: STUDENT RECORD NOT FOUND!\n')
    remove('STUDENT_FILE.txt')
    rename('TEMPORARY.txt','STUDENT_FILE.txt')

# Automatic generation of Admission Number
def admcode():
    code = 1000
    fin = open('STUDENT_FILE.txt', 'r')
    fin.seek(0)
    first_char = fin.read(1)
    if not first_char:
         code = 1000
    else:
        for line in fin:
            line = line.strip()
            rec = line.split(',')
            code = int(rec[0])
    return(code)

# Computing the grade from mark
def grade_calc(mark):
    if 90 < mark <= 100:
        return 'A1'
    elif 80 < mark <= 90:
        return 'A2'
    elif 70 < mark <= 80:
        return 'B1'
    elif 60 < mark <= 70:
        return 'B2'
    elif 50 < mark <= 60:
        return 'C1'
    elif 40 < mark <= 50:
        return 'C2'
    elif 33 < mark <= 40:
        return 'D'
    elif mark <= 33:
        return 'E'

# Validation for Inputted Date
def dateval():
    # Input Day
    d = int(input('Day? '))
    # Input Month
    m = int(input('Month? '))
    # Input Year
    y = int(input('Year? '))
    maxd = 0
    if m in [1, 3, 5, 7, 8, 10, 12]:
        maxd = 31
    elif m in [4, 6, 9, 11]:
        maxd = 30
    elif m == 2: 
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            maxd = 29
        else:
            maxd = 28
    if maxd == 0:
        print('Please input valid Month'.upper())
    elif d < 1 or d > maxd:
        print('Please input valid Day'.upper())
    elif y < 1950 and y > 2001:
        print('Please input valid Year between 1950 and 2001'.upper())
    else:
        if len(str(m)) == 1:
            m = '0' +  str(m)
        if len(str(d)) == 1:
               d = '0' +  str(d)
        return (str(d) + '-' + str(m) + '-' + str(y))

# Validation for Phone Number
def phonevalidate(n):
    fin = open('STUDENT_FILE.txt','r')
    fin.seek(0)
    found = 0
    for line in fin:
        line = line.strip()
        rec = line.split(',')
        ph = rec[7]
        if ph == n:
            found = 1
            print('Same Phone Number found in records')
            break
    if len(fin.read()) == 0:
        found = 0
    return(found)

while True:
    print('Menu:')        
    print('1. Adding Student records in Student File')
    print('2. Adding Student records in Result File')
    print('3. Modifying Student records in Student File')
    print('4. Deleting Student records from Student File')
    print('5. Searching Student records')
    print('6. Displaying Student Reports')
    print('0. Exit Menu')
    print('\n')
    ch = int(input('Choice [0-6]: '))
    if ch == 1:
        n = int(input('Number of Student records to be added: '))
        addrec()
    elif ch == 2:
        res_file()
    elif ch == 3:
        print('Modifying Records Menu:')
        print('1. Modifying Roll Number')
        print('2. Modifying Class')
        print('3. Modifying Section')
        print('4. Modifying Date of Birth')
        print('5. Modifying Phone Number')
        print('6. Modifying Stream Code')
        print('0. Exit Modifying Menu')
        a = int(input('Choice [0-6]: '))
        if a == 1:
            modif1()
        elif a == 2:
            modif2()
        elif a == 3:
            modif3()
        elif a == 4:
            modif4()
        elif a == 5:
            modif5()
        elif a == 6:
            modif6()
        else:
            break
    elif ch == 4:
        delete()
    elif ch == 5:
        search()
    elif ch == 6:
        print('Student Reports Menu:')
        print('1. Stream-wise Personal information of each student')
        print('2. Stream-wise Result List')
        print('3. Stream-wise Merit List')
        print('4. Marks Sheet of student')
        print('0. Exit Student Records Menu')
        b = int(input('Choice [0-4]: '))
        if b == 1:
            sw_personal()
        elif b == 2:
            sw_result()
        elif b == 3:
            sw_merit()
        elif b == 4:
            marksheet()
        else:
            break
    else:
        print('Thank You for visiting!')
        break
        
