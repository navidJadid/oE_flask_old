import pytest
from webrob.app_and_db import app,db
from webrob.models.teaching import Course, CourseExercise, CourseTask
import teaching_test_constants as CONSTANTS

backup_config = app.config[CONSTANTS.DATABASE_URI]

def create_course_rows():
    # db.drop_all()
    course1 = Course(name = CONSTANTS.COURSES[0], term = CONSTANTS.TERMS[0], university = CONSTANTS.UNIVERSITIES[0])
    course2 = Course(name = CONSTANTS.COURSES[1], term = CONSTANTS.TERMS[1], university = CONSTANTS.UNIVERSITIES[1])
    db.session.add(course1)
    db.session.add(course2)
    db.session.commit()

def create_course_exercise_rows():
    # db.drop_all()
    create_course_rows()
    course_one = Course.query.get(1)
    course_two = Course.query.get(2)
    exercise1 = CourseExercise(course_id = course_one.id, number= CONSTANTS.EXERCISE_NUM_ONE,
                               title= CONSTANTS.TITLE_ONE, archive= bin(20) )
    exercise2 = CourseExercise(course_id = course_two.id, number = CONSTANTS.EXSERCISE_NUM_TWO,
                               title = CONSTANTS.TITLE_TWO, archive=bin(10))
    db.session.add(exercise1)
    db.session.add(exercise2)
    db.session.commit()

    return course_one, course_two


def create_course_task_rows():
    # db.drop_all()
    course_one, course_two = create_course_exercise_rows()
    exercise_one = CourseExercise.query.get(1)
    exercise_two = CourseExercise.query.get(2)
    task1 = CourseTask(exercise_id = exercise_one.id, number = CONSTANTS.TASK_NUM_ONE,
                       title = CONSTANTS.TASK_TITLE_ONE, text = CONSTANTS.TEXT_ONE)

    task2 = CourseTask(exercise_id = exercise_one.id, number = CONSTANTS.TASK_NUM_TWO,
                       title = CONSTANTS.TASK_TITLE_TWO, text = CONSTANTS.TEXT_TWO)

    task3 = CourseTask(exercise_id = exercise_two.id, number = CONSTANTS.TASK_NUM_THREE,
                       title = CONSTANTS.TASK_TITLE_THREE, text = CONSTANTS.TEXT_THREE)
    db.session.add(task1)
    db.session.add(task2)
    db.session.add(task3)
    db.session.commit()

    return course_one, course_two, exercise_one, exercise_two

def create_database():
    app.config[CONSTANTS.DATABASE_URI] = CONSTANTS.TEST_DB_PATH

    db.drop_all()
    db.create_all()

    course_one, course_two, exercise_one, exercise_two = create_course_task_rows()

    return course_one, course_two, exercise_one, exercise_two


def test_find_courses_with_course_name_None():
    from webrob.models.teaching import find_courses
    getcourse = find_courses(course_name = None)
    assert getcourse == CONSTANTS.EMPTY_COURSE
    


def test_get_exercises():
    from webrob.models.teaching import get_exercises
    course_one, course_two, exercise_one, exercise_two = create_database()
    exercises = get_exercises(course_id = course_one.id)
    title = exercises[0].title
    assert title == CONSTANTS.TITLE_ONE
    app.config[CONSTANTS.DATABASE_URI] = backup_config

def test_get_tasks():
    from webrob.models.teaching import get_tasks
    course_one, course_two, exercise_one, exercise_two = create_database()
    tasks = get_tasks(exercise_id = exercise_one.id)
    text = tasks[1].text
    assert text == CONSTANTS.TEXT_TWO
    app.config[CONSTANTS.DATABASE_URI] = backup_config

def test_get_task():
    from webrob.models.teaching import get_task
    course_one, course_two, exercise_one, exercise_two = create_database()
    task = get_task(exercise_id = exercise_one.id, task_number = CONSTANTS.TASK_NUM_ONE)
    assert task.title == CONSTANTS.TASK_TITLE_ONE
    app.config[CONSTANTS.DATABASE_URI] = backup_config




