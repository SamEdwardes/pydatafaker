"""
Create a school with fake data.
"""
import numpy as np
import pandas as pd
from faker import Faker


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

    Returns
    -------
    dict
        A dictionary containing related DataFrames.
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
        available_teachers = np.repeat(
            teachers_grade_i, (num_students_grade_i / num_teachers_grade_i) + 1
        )
        students_by_grade_i = student_table.query("grade == @i").reset_index(drop=True)
        students_by_grade_i["teacher_id"] = np.random.choice(
            available_teachers, replace=False, size=num_students_grade_i
        )
        students_by_grade.append(students_by_grade_i)
    student_table = pd.concat(students_by_grade)
    # create rooms and assign to teachers
    room_table = create_rooms(n_teachers)
    teacher_table["room_id"] = np.random.choice(
        room_table["room_id"], replace=False, size=n_teachers
    )
    x = {
        "student_table": student_table,
        "teacher_table": teacher_table,
        "room_table": room_table,
    }
    return x
