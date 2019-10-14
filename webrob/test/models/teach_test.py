import pytest
from webrob.app_and_db import app,db
import teaching_test_constants as CONSTANTS
from webrob.models.teaching import Course

backup_config = app.config[CONSTANTS.DATABASE_URI]

def create_course_exercise_rows():
    from webrob.models.teaching import CourseExercise
    exercise1 = CourseExercise(course_id = CONSTANTS.COURSE_ID_ONE, number= CONSTANTS.COURSE_NUM_ONE,
                               title= CONSTANTS.TITLE_ONE, archive= bin(20) )
    exercise2 = CourseExercise(course_id = CONSTANTS.COURSE_ID_TWO, number = CONSTANTS.COURSE_NUM_TWO,
                               title = CONSTANTS.TITLE_TWO, archive=bin(10))
    db.session.add(exercise1)
    db.session.add(exercise2)


def create_course_task_rows():
    from webrob.models.teaching import CourseTask
    task1 = CourseTask(exercise_id = CONSTANTS.EXERCISE_ID_ONE, number = CONSTANTS.TASK_NUM_ONE,
                       title = CONSTANTS.TASK_TITLE_ONE, text = CONSTANTS.TEXT_ONE)
    task2 = CourseTask(exercise_id = CONSTANTS.EXERCISE_ID_ONE, number = CONSTANTS.TASK_NUM_ONE,
                       title = CONSTANTS.TASK_TITLE_TWO, text = CONSTANTS.TEXT_TWO)
    db.session.add(task1)
    db.session.add(task2)

def create_database():
    app.config[CONSTANTS.DATABASE_URI] = CONSTANTS.TEST_DB_PATH

    db.drop_all()
    db.create_all()
    create_course_exercise_rows()
    create_course_task_rows()
    db.session.commit()

def test_get_exercises():
    from webrob.models.teaching import get_exercises
    create_database()
    exercises = get_exercises(course_id = CONSTANTS.COURSE_ID_ONE)
    title = exercises[0].title
    assert title == CONSTANTS.TITLE_ONE
    app.config[CONSTANTS.DATABASE_URI] = backup_config

def test_get_tasks():
    from webrob.models.teaching import get_tasks
    create_database()
    tasks = get_tasks(exercise_id = CONSTANTS.EXERCISE_ID_ONE)
    text = tasks[1].text
    assert text == CONSTANTS.TEXT_TWO
    app.config[CONSTANTS.DATABASE_URI] = backup_config

def test_get_task():
    from webrob.models.teaching import get_task
    create_database()
    task = get_task(exercise_id = CONSTANTS.EXERCISE_ID_ONE, task_number = CONSTANTS.TASK_NUM_ONE)
    assert task.title == CONSTANTS.TASK_TITLE_ONE
    app.config[CONSTANTS.DATABASE_URI] = backup_config


