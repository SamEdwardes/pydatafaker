"""
Create a school with fake data.
"""
import numpy as np
import pandas as pd
from faker import Faker

from pydatafaker.utilities import create_date


def create_students(n=300, min_grade=1, max_grade=7):
    """Create a DataFrame with fake student names and attributes.

    Parameters
    ----------
    n : int, optional
        The number of students to generate, by default 300.
    min_grade : int, optional
        The minimum grade for a school, by default 1.
    max_grade : int, optional
        The maximum grade for a school, by default 7.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing: student_id, name, grade, and teacher_id.

    Examples
    --------
    >>> from pydatafaker import school
    >>> school.create_students()
        student_id                name  grade teacher_id
    0    student_0001    Michael Peterson      7       <NA>
    1    student_0002       Kimberly Ryan      6       <NA>
    2    student_0003    Joseph Rodriguez      6       <NA>
    3    student_0004        Brandon Reid      3       <NA>
    4    student_0005   Mrs. Amanda Clark      4       <NA>
    ..            ...                 ...    ...        ...
    295  student_0296      Kayla Anderson      2       <NA>
    296  student_0297  Nicholas Frederick      1       <NA>
    297  student_0298  Jacqueline Spencer      3       <NA>
    298  student_0299       Kelsey Acosta      1       <NA>
    299  student_0300      Glenn Beck DVM      1       <NA>
    [300 rows x 4 columns]
    """
    fake = Faker()
    x = pd.DataFrame(
        {
            "student_id": ["student_" + str(i).zfill(4) for i in range(1, n + 1)],
            "name": [fake.name() for _ in range(n)],
            "grade": np.random.randint(min_grade, max_grade + 1, n),
            "teacher_id": pd.NA,
        }
    )
    return x


def create_teachers(n=14, min_grade=1, max_grade=7):
    """Create a DataFrame with fake teacher names and attributes.

    Parameters
    ----------
    n : int, optional
        The number of teachers to generate, by default 14.
    min_grade : int, optional
        The minimum grade a teacher can teach, by default 1.
    max_grade : int, optional
        The maximum grade a teacher can teach, by default 7.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing: teacher_id, name, grade, room_id
        
    Examples
    --------
    >>> from pydatafaker import school
    >>> school.create_teachers()
        teacher_id              name  grade room_id
    0   teacher_0001       Omar Savage      1    <NA>
    1   teacher_0002     Susan Shepard      2    <NA>
    2   teacher_0003  Kimberly Johnson      3    <NA>
    3   teacher_0004    Carlos Johnson      4    <NA>
    4   teacher_0005  Stephanie Castro      5    <NA>
    5   teacher_0006      Thomas Young      6    <NA>
    6   teacher_0007       Robert Wood      1    <NA>
    7   teacher_0008       Scott Yates      2    <NA>
    8   teacher_0009    William Flores      3    <NA>
    9   teacher_0010  Christopher Reid      4    <NA>
    10  teacher_0011  Dr. Laura Martin      5    <NA>
    11  teacher_0012     Diana Coleman      6    <NA>
    12  teacher_0013   Stephanie Pratt      1    <NA>
    13  teacher_0014        Jorge Rios      2    <NA>
    """
    fake = Faker()
    x = pd.DataFrame(
        {
            "teacher_id": ["teacher_" + str(i).zfill(4) for i in range(1, n + 1)],
            "name": [fake.name() for _ in range(n)],
            "grade": np.concatenate(
                [np.arange(min_grade, max_grade) for _ in range(n)]
            )[0:n],
            "room_id": pd.NA,
        }
    )
    return x


def create_grades(
    student_ids, n_tests_per_student=10, min_date="2020-09-01", max_date="2021-07-30"
):
    """Create fake grades.

    Parameters
    ----------
    student_ids : list
        A list of unique student IDs.
    n_tests_per_student : int, optional
        The number of tests to generate per student, by default 10.
    min_date : str, optional
        The minimum possible date, by default '2020-09-01'.
    max_date : str, optional
        The maximum possible date, by default '2021-07-30'.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing test scores.

    Examples
    --------
    >>> from pydatafaker import school
    >>> school.create_grades(['student_01', 'student_02'], 5)
    student_id  test_score       date
    0  student_01    1.000000 2021-07-03
    1  student_01    0.584709 2021-07-08
    2  student_01    0.735963 2020-11-08
    3  student_01    1.000000 2021-02-26
    4  student_01    0.920111 2021-01-09
    5  student_02    0.626991 2021-05-13
    6  student_02    0.903123 2020-10-30
    7  student_02    0.690480 2021-01-09
    8  student_02    1.000000 2020-09-26
    9  student_02    0.788777 2021-04-11
    """
    n = n_tests_per_student * len(student_ids)
    x = pd.DataFrame(
        {
            "student_id": np.repeat(student_ids, n_tests_per_student),
            "test_score": np.random.normal(0.8, 0.15, size=n),
            "date": [create_date(min_date, max_date) for _ in range(n)],
        }
    )
    # test scores should never be greater than 1
    x["test_score"] = x["test_score"].apply(lambda x: 1 if x > 1 else x)
    return x


def create_rooms(n=10):
    """Create a DataFrame with fake room IDs and attributes.

    Parameters
    ----------
    n : int, optional
        The number of rooms to generate, by default 10.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing: room_id, smartboard, sink, and square_footage.
        
    Examples
    --------
    >>> from pydatafaker import school
    >>> school.create_rooms()
        room_id  smartboard  sink  square_footage
    0  room_001           0     0             981
    1  room_002           1     1             936
    2  room_003           1     0            1158
    3  room_004           0     0            1275
    4  room_005           1     1             939
    5  room_006           0     0             793
    6  room_007           1     1            1207
    7  room_008           0     1             702
    8  room_009           1     1             707
    9  room_010           1     1            1048
    """
    x = pd.DataFrame(
        {
            "room_id": ["room_" + str(i).zfill(3) for i in range(1, n + 1)],
            "smartboard": np.random.choice([0, 1], replace=True, size=n),
            "sink": np.random.choice([0, 1], replace=True, size=n),
            "square_footage": np.random.normal(1_000, 200, size=n).astype(int),
        }
    )
    return x


def create_school(
    n_students=300,
    max_class_size=22,
    min_grade=1,
    max_grade=7,
    n_tests_per_student=10,
    min_date="2020-09-01",
    max_date="2021-07-30",
):
    """Create an entire fake school.

    A meta function that creates an entire fake school represented by
    different tables. The tables have relationships between theme. A dictionary
    is returned that contains the following DataFrames:

    - student_table
    - teacher_table
    - room_table

    Parameters
    ----------
    n_students : int, optional
        The number of students to generate, by default 300.
    max_class_size : int, optional
        The maximum number of students that can be assigned to one teacher, by
        default 22.
    min_grade : int, optional
        The minimum grade a teacher can teach, by default 1.
    max_grade : int, optional
        The maximum grade a teacher can teach, by default 7.
    n_tests_per_student : int, optional
        The number of tests to generate per student, by default 10.
    min_date : str, optional
        The minimum possible date, by default '2020-09-01'.
    max_date : str, optional
        The maximum possible date, by default '2021-07-30'.

    Returns
    -------
    dict
        A dictionary containing related DataFrames.
        
    Examples
    --------
    >>> from pydatafaker import school
    >>> skool = school.create_school()
    >>> type(skool)
    <class 'dict'>
    >>> skool.keys()
    dict_keys(['student_table', 'teacher_table', 'room_table', 'grade_table'])
    >>> skool['student_table']
        student_id                name  grade    teacher_id
    0   student_0002       Barry Nichols      1  teacher_0001
    1   student_0005  Dr. Sheri Williams      1  teacher_0013
    2   student_0006          Jason Park      1  teacher_0001
    3   student_0014   Christopher Allen      1  teacher_0013
    4   student_0021      Thomas Johnson      1  teacher_0001
    ..           ...                 ...    ...           ...
    43  student_0280      Crystal Hughes      7  teacher_0015
    44  student_0289      Rachel Barajas      7  teacher_0016
    45  student_0292        Steven Brown      7  teacher_0002
    46  student_0296      Cynthia Bright      7  teacher_0015
    47  student_0297          Brian Hill      7  teacher_0016
    [300 rows x 4 columns]
    >>> skool['teacher_table']
        teacher_id                name  grade   room_id
    0   teacher_0001     Andrew Valencia      1  room_009
    1   teacher_0002       Brenda Howell      7  room_005
    2   teacher_0003         Drew Garcia      3  room_010
    3   teacher_0004           Chad Byrd      5  room_013
    4   teacher_0005  Alexander Williams      6  room_016
    5   teacher_0006   Mrs. Angela Baird      4  room_015
    6   teacher_0007        Megan Dillon      4  room_008
    7   teacher_0008       Robert Murray      3  room_003
    8   teacher_0009          Robin Wood      2  room_004
    9   teacher_0010      Brent Castillo      2  room_001
    10  teacher_0011          Tina Jones      4  room_006
    11  teacher_0012         Evan Riddle      5  room_007
    12  teacher_0013           Nancy Key      1  room_011
    13  teacher_0014         Mary Thomas      2  room_014
    14  teacher_0015           Troy Cole      7  room_002
    15  teacher_0016      Michael Lowery      7  room_012
    16  teacher_0017        Robert Hicks      6  room_017
    """
    student_table = create_students(n_students, min_grade, max_grade)
    # figure out how many teachers you need
    grade_distribution = student_table["grade"].value_counts().sort_index()
    grade_distribution = grade_distribution.rename("num_students").to_frame()
    grade_distribution["num_teachers"] = (
        grade_distribution["num_students"] / max_class_size
    )
    grade_distribution["num_teachers"] = grade_distribution["num_teachers"].apply(
        lambda x: int(np.ceil(x))
    )
    # now create teacher table
    n_teachers = grade_distribution["num_teachers"].sum()
    teacher_table = create_teachers(n_teachers, min_grade, max_grade)
    # reassign grades to respect class size
    grades = np.empty(0)
    for i in grade_distribution.index:
        grades = np.concatenate(
            [grades, np.repeat(i, grade_distribution.loc[i, "num_teachers"])]
        )
    teacher_table["grade"] = np.random.choice(grades, replace=False, size=n_teachers)
    teacher_table["grade"] = teacher_table["grade"].astype(int)
    # assign each student a teacher from the correct grade
    students_by_grade = []
    for i in range(1, max_grade + 1):
        num_students_grade_i = grade_distribution.loc[i, "num_students"]
        num_teachers_grade_i = grade_distribution.loc[i, "num_teachers"]
        teachers_grade_i = teacher_table.query("grade == @i")["teacher_id"].to_list()
        teachers_grade_i_assignment = teachers_grade_i * int(
            (num_students_grade_i / num_teachers_grade_i) + 1
        )
        teachers_grade_i_assignment = teachers_grade_i_assignment[
            0:num_students_grade_i
        ]
        students_by_grade_i = student_table.query("grade == @i").reset_index(drop=True)
        students_by_grade_i["teacher_id"] = teachers_grade_i_assignment
        students_by_grade.append(students_by_grade_i)
    student_table = pd.concat(students_by_grade)
    # create rooms and assign to teachers
    room_table = create_rooms(n_teachers)
    teacher_table["room_id"] = np.random.choice(
        room_table["room_id"], replace=False, size=n_teachers
    )
    # grades
    grade_table = create_grades(
        student_ids=student_table["student_id"].to_list(),
        n_tests_per_student=n_tests_per_student,
        min_date=min_date,
        max_date=max_date,
    )
    x = {
        "student_table": student_table,
        "teacher_table": teacher_table,
        "room_table": room_table,
        "grade_table": grade_table,
    }
    return x
