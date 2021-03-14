students = ["Alp Tuğluk", "Berk Yalçın", "Gizem Öztepe", "Çınar Keçeci", "İrem Yalçın"]
gradeList=[]
for i in students:
        midterm = int(input("{} Vize notu:".format(i)))
        project = int(input("{} Proje notu:".format(i)))
        final = int(input("{} Final notu:".format(i)))
        Grade = (midterm*(0.3) + project*(0.3) + final*(0.4))
        if 50 <= Grade <= 100:
            gradeList.append(Grade,)
            print(i, "not ortalaması: ", Grade)
        elif Grade > 100 or Grade < 0:
            while Grade > 100 or Grade < 0:
                print("Lütfen geçerli değerler girerek tekrar deneyiniz.")
                midterm = int(input("{} Vize notu:".format(i)))
                project = int(input("{} Proje notu:".format(i)))
                final = int(input("{} Final notu:".format(i)))
                Grade = (midterm*(3) + project*(3) + final*(4))/10
                gradeList.append(Grade)
                print(i, "not ortalaması: ", Grade)
        else:
            while 0<Grade<50:
                print("Her öğrenci geçer not almalıdır. Lütfen kontrol edip tekrar deneyiniz.")
                midterm = int(input("{} Vize notu:".format(i)))
                project = int(input("{} Proje notu:".format(i)))
                final = int(input("{} Final notu:".format(i)))
                Grade = (midterm*(3) + project*(3) + final*(4))/10
                gradeList.append(Grade)
                print(i, "not ortalaması: ", Grade)
                
def studentInfo(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print('{}: {}'.format(key, value))
studentInfo(İsim= students[0], Not=gradeList[0])
studentInfo(İsim= students[1], Not=gradeList[1])
studentInfo(İsim= students[2], Not=gradeList[2])
studentInfo(İsim= students[3], Not=gradeList[3])
studentInfo(İsim= students[4], Not=gradeList[4])

sortedList = sorted(gradeList, reverse=True)
print(sortedList)