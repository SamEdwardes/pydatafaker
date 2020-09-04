"""
Create a school with fake data
"""
import numpy as np
import pandas as pd
from faker import Faker


def create_students(n=300, min_grade=1, max_grade=7):    
    fake = Faker()
    x = pd.DataFrame({
        'student_id': ['student_' + str(i).zfill(4) for i in range(1, n + 1)],
        'names': [fake.name() for _ in range(n)],
        'grade': np.random.randint(min_grade, max_grade + 1, n)
    })
    return x
    

def create_teachers(n=14, min_grade=1, max_grade=7):
    fake = Faker()
    x = pd.DataFrame({
        'teach_id': ['teacher_' + str(i).zfill(4) for i in range(1, n + 1)],
        'names': [fake.name() for _ in range(n)],
        'grade': np.concatenate([np.arange(min_grade, max_grade) for _ in range(n)])[0:n]      
    })
    return x

        


def create_school(n_students=300, max_class_size=22, min_grade=1, max_grade=7,):
    student_table = create_students(n_students, min_grade, max_grade)
    # figure out how many teachers you need
    grade_distribution = student_table['grade'].value_counts().sort_index()
    grade_distribution = grade_distribution.rename('num_students').to_frame()
    grade_distribution['num_teachers'] = grade_distribution['num_students'] / max_class_size
    grade_distribution['num_teachers'] = grade_distribution['num_teachers'].apply(lambda x: int(np.ceil(x)))
    # now create teacher table
    n_teachers = grade_distribution['num_teachers'].sum()
    teacher_table = create_teachers(n_teachers, min_grade, max_grade)
    # reassign grades to respect class size
    grades = np.empty(0)
    for i in grade_distribution.index:
        grades = np.concatenate([grades, np.repeat(i, grade_distribution.loc[i, 'num_teachers'])])
    teacher_table['grade'] = np.random.choice(grades, replace=False, size=n_teachers)
    teacher_table['grade'] = teacher_table['grade'].astype(int)
    # assign students to a teacher
    """
    Note to self for assigning students to classrooms:
    - If there are 44 studuents in a grade, and 2 teachers, replicate each
      teachers name 22 times and combine in an array
    - Then randomly select with np.random.choice replace=False from the list
    """
    students_by_grade = {}
    for i in range(1, max_grade + 1):
        students_by_grade[i] = student_table.query('grade == @i')['student_id']
        
    x = {
        'student_table': student_table,
        'teacher_table': teacher_table
    }
    return x

##############################################################################
##############################################################################
# create_teachers()['grade'].value_counts()
# create_teachers()['grade'].value_counts()
# create_students()['grade'].value_counts()
school = create_school()
for k, v in school.items():
    print('=' * 32)
    print(k)
    print('=' * 32)
    print(v)
print('=' * 32)
print(school['teacher_table']['grade'].value_counts())

# create_teachers()

# z = create_school()
# z