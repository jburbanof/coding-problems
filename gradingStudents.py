def gradingStudents(grades):
    gradeslist=[]
    for i in grades:    
        if i>37 and abs((i)-((int(i/5)+1)*5))<3:
            e=((int(i/5)+1)*5)
            gradeslist.append(e)
        else:
            gradeslist.append(i)
    return gradeslist