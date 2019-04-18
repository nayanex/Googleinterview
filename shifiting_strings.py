
s0 ='abcd'
s1 = "abcdef" # abcdef
s2='a'

leftShifts = 0
rightShifts = 0


def shift_left(text):
    my_string = text[1:] + text[0]
    return my_string

def shift_right(text):
    my_string = text[-1] + text[:-1]
    return my_string


shifted_text = ""

if(leftShifts == 0 or rightShifts == 0):
   print(s1)


for n in range(0,leftShifts):
    print("crazy")
    shifted_text = shift_left(s1)

for n in range(0,rightShifts):
    print("dubaubauab")

    shifted_text = shift_right(s1)

print(shifted_text)

SELECT DEPARTMENT.NAME, COUNT(STUDENT.ID) AS COUNT_OF_STUDENT_IN_THE_DEPARTMENT
    FROM DEPARMENT 
    LEFT JOIN STUDENT ON DEPARTMENT.ID = STUDENT.DEPT_ID
    GROUP BY DEPARTMENT.NAME
    ORDER BY COUNT_OF_STUDENT_IN_THE_DEPARTMENT DESC, DEPARTMENT.NAME ASC