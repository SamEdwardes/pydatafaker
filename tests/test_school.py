from pydatafaker import school


def test_create_school():

    x = school.create_school(n_students=400, max_class_size=22)
    student_table = x['student_table']
    teacher_table = x['student_table']
    room_table = x['student_table']

    assert student_table.shape[0] == 400
    assert room_table.shape[0] == teacher_table.shape[0]

    # make sure that each classroom is under the max number of students
    num_students_per_class = student_table['teacher_id'].value_counts()
    assert max(num_students_per_class) <= 22
