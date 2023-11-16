import main
import sqlite3 as sql

db = sql.connect('database.db')
cur = db.cursor()

async def create_subjects():
    main.cur.execute('''CREATE TABLE IF NOT EXISTS subjects_10t_2 (
        title TEXT NOT NULL,
        subj_id INTEGER DEFAULT 0,
        subjects TEXT NOT NULL,
        cabines INTEGER NOT NULL
    )''')
    main.db.commit()


async def start_db_2():
    for i in range(1, 7):
        main.cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['monday']['title'], subjects=subjects['monday']['subjects'][f'{i}'], cabines=subjects['monday']['cabines'][f'{i}']))
        main.db.commit()
    for i in range(1, 7):
        main.cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['tuesday']['title'], subjects=subjects['tuesday']['subjects'][f'{i}'], cabines=subjects['tuesday']['cabines'][f'{i}']))
        main.db.commit()
    for i in range(1, 7):
        main.cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['wednesday']['title'], subjects=subjects['wednesday']['subjects'][f'{i}'], cabines=subjects['wednesday']['cabines'][f'{i}']))
        main.db.commit()
    for i in range(1, 7):
        main.cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['thursday']['title'], subjects=subjects['thursday']['subjects'][f'{i}'], cabines=subjects['thursday']['cabines'][f'{i}']))
        main.db.commit()
    for i in range(1, 7):
        main.cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['friday']['title'], subjects=subjects['friday']['subjects'][f'{i}'], cabines=subjects['friday']['cabines'][f'{i}']))
        main.db.commit()
    for i in range(1, 8):
        main.cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['saturday']['title'], subjects=subjects['saturday']['subjects'][f'{i}'], cabines=subjects['saturday']['cabines'][f'{i}']))
        main.db.commit()

async def add_subjects():
    subject_monday = main.cur.execute('SELECT title, subj_id FROM subjects_10t_2 WHERE title = "Понедельник"').fetchall()[-1]
    if subject_monday[0] == 'Понедельник' and subject_monday[1] != 6:
        for i in range(1, 7):
            main.cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['monday']['title'], subjects=subjects['monday']['subjects'][f'{i}'], cabines=subjects['monday']['cabines'][f'{i}']))
            main.db.commit()
    subject_tuesday = main.cur.execute('SELECT title, subj_id FROM subjects_10t_2 WHERE title = "Вторник"').fetchall()[-1]
    if subject_tuesday[0] == 'Вторник' and subject_tuesday[1] != 6:
        for i in range(1, 7):
            main.cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['tuesday']['title'], subjects=subjects['tuesday']['subjects'][f'{i}'], cabines=subjects['tuesday']['cabines'][f'{i}']))
            main.db.commit()
    subject_wednesday = main.cur.execute('SELECT title, subj_id FROM subjects_10t_2 WHERE title = "Среда"').fetchall()[-1]
    if subject_tuesday[0] == 'Среда' and subject_tuesday[1] != 6:
        for i in range(1, 7):
            main.cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['wednesday']['title'], subjects=subjects['wednesday']['subjects'][f'{i}'], cabines=subjects['wednesday']['cabines'][f'{i}']))
            main.db.commit() 
    subject_thursday = main.cur.execute('SELECT title, subj_id FROM subjects_10t_2 WHERE title = "Четверг"').fetchall()[-1]
    if subject_thursday[0] == 'Четверг' and subject_thursday[1] != 6: 
        for i in range(1, 7):
            main.cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['thursday']['title'], subjects=subjects['thursday']['subjects'][f'{i}'], cabines=subjects['thursday']['cabines'][f'{i}']))
            main.db.commit()
    subject_friday = main.cur.execute('SELECT title, subj_id FROM subjects_10t_2 WHERE title = "Пятница"').fetchall()[-1]
    if subject_friday[0] == 'Пятница' and subject_friday[1] != 6:
        for i in range(1, 7):
            main.cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['friday']['title'], subjects=subjects['friday']['subjects'][f'{i}'], cabines=subjects['friday']['cabines'][f'{i}']))
            main.db.commit()
    subject_saturday = main.cur.execute('SELECT title, subj_id FROM subjects_10t_2 WHERE title = "Суббота"').fetchall()[-1]
    if subject_saturday[0] == 'Суббота' and subject_saturday[1] != 7:
        for i in range(1, 8):
            main.cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['saturday']['title'], subjects=subjects['saturday']['subjects'][f'{i}'], cabines=subjects['saturday']['cabines'][f'{i}']))
            main.db.commit()
    else:
        print('Error')

subjects = {
    'monday': {
        'title': 'Понедельник',
        'subjects': {
            '1': 'Разговоры о важном',
            '2': 'Геометрия',
            '3': 'Алгебра',
            '4': 'Литер',
            '5': 'Общество',
            '6': 'ОБЖ'
        },
        'cabines': {
            '1':'216',
            '2':'216',
            '3':'216',
            '4':'206',
            '5':'205',
            '6':'315'
        }
    },
    'tuesday': {
        'title': 'Вторник',
        'subjects': {
            '1': 'Эл. физика',
            '2': 'История',
            '3': 'Англ.яз',
            '4': 'Англ.яз',
            '5': 'Информатика',
            '6': 'Информатика'
        },
        'cabines': {
            '1':'210',
            '2':'205',
            '3':'215',
            '4':'215',
            '5':'218',
            '6':'218'
        }
    },
    'wednesday': {
        'title': 'Среда',
        'subjects': {
            '1': 'Физ-ра',
            '2': 'Русс.яз',
            '3': 'Литер',
            '4': 'Геометрия',
            '5': 'Химия',
            '6': 'Информатика'
        },
        'cabines': {
            '1':'219',
            '2':'206',
            '3':'206',
            '4':'215',
            '5':'218',
            '6':'105'
        }
    },
    'thursday': {
        'title': 'Четверг',
        'subjects': {
            '1': 'Физ-ра',
            '2': 'Физика',
            '3': 'Геометрия',
            '4': 'Информатика',
            '5': 'Англ.яз',
            '6': 'Инд.проект'
        },
        'cabines': {
            '1':'219',
            '2':'210',
            '3':'216',
            '4':'218',
            '5':'215',
            '6':'216'
        }
    },
    'friday': {
        'title': 'Пятница',
        'subjects': {
            '1': 'Алгебра',
            '2': 'История',
            '3': 'География',
            '4': 'Рус.яз',
            '5': 'Биология',
            '6': 'Эл.физика'
        },
        'cabines': {
            '1':'216',
            '2':'105',
            '3':'212',
            '4':'315',
            '5':'312',
            '6':'210'
        }
    },
    'saturday': {
        'title': 'Суббота',
        'subjects': {
            '1': 'Отсутсвует',
            '2': 'Общество',
            '3': 'Алгебра',
            '4': 'Вероятность',
            '5': 'Физика',
            '6': 'Родн.яз',
            '7': 'Кл.час'
        },
        'cabines': {
            '1':'216',
            '2':'205',
            '3':'216',
            '4':'216',
            '5':'210',
            '6':'318',
            '7': '216'
        }
    }
}

subjects_monday_2 = cur.execute('SELECT title, subjects, cabines FROM subjects_10t_2 WHERE title="Понедельник"').fetchall()
subjects_tuesday_2 = cur.execute('SELECT title, subjects, cabines FROM subjects_10t_2 WHERE title="Вторник"').fetchall()
subjects_wednesday_2 = cur.execute('SELECT title, subjects, cabines FROM subjects_10t_2 WHERE title="Среда"').fetchall()
subjects_thursday_2 = cur.execute('SELECT title, subjects, cabines FROM subjects_10t_2 WHERE title="Четверг"').fetchall()
subjects_friday_2 = cur.execute('SELECT title, subjects, cabines FROM subjects_10t_2 WHERE title="Пятница"').fetchall()
subjects_saturday_2 = cur.execute('SELECT title, subjects, cabines FROM subjects_10t_2 WHERE title="Суббота"').fetchall()


full_schedule_second = (                         f'═────<b>{subjects_monday_2[0][0]}</b>────═'
                                               '\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {subjects_monday_2[0][1]}  <b>{subjects_monday_2[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {subjects_monday_2[1][1]}  <b>{subjects_monday_2[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {subjects_monday_2[2][1]}  <b>{subjects_monday_2[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {subjects_monday_2[3][1]}  <b>{subjects_monday_2[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {subjects_monday_2[4][1]}  <b>{subjects_monday_2[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {subjects_monday_2[5][1]}  <b>{subjects_monday_2[5][2]}</b>'
                                               '\n————————————————————'
                                               f'\n═────<b>{subjects_tuesday_2[0][0]}</b>────═'
                                               '\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {subjects_tuesday_2[0][1]}  <b>{subjects_tuesday_2[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {subjects_tuesday_2[1][1]}  <b>{subjects_tuesday_2[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {subjects_tuesday_2[2][1]}  <b>{subjects_tuesday_2[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {subjects_tuesday_2[3][1]}  <b>{subjects_tuesday_2[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {subjects_tuesday_2[4][1]}  <b>{subjects_tuesday_2[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {subjects_tuesday_2[5][1]}  <b>{subjects_tuesday_2[5][2]}</b>'
                                               '\n————————————————————'
                                               f'\n═────<b>{subjects_wednesday_2[0][0]}</b>────═'
                                               '\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {subjects_wednesday_2[0][1]}  <b>{subjects_wednesday_2[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {subjects_wednesday_2[1][1]}  <b>{subjects_wednesday_2[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {subjects_wednesday_2[2][1]}  <b>{subjects_wednesday_2[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {subjects_wednesday_2[3][1]}  <b>{subjects_wednesday_2[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {subjects_wednesday_2[4][1]}  <b>{subjects_wednesday_2[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {subjects_wednesday_2[5][1]}  <b>{subjects_wednesday_2[5][2]}</b>'
                                               '\n————————————————————'
                                               f'\n═────<b>{subjects_thursday_2[0][0]}</b>────═'
                                               '\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {subjects_thursday_2[0][1]}  <b>{subjects_thursday_2[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {subjects_thursday_2[1][1]}  <b>{subjects_thursday_2[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {subjects_thursday_2[2][1]}  <b>{subjects_thursday_2[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {subjects_thursday_2[3][1]}  <b>{subjects_thursday_2[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {subjects_thursday_2[4][1]}  <b>{subjects_thursday_2[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {subjects_thursday_2[5][1]}  <b>{subjects_thursday_2[5][2]}</b>'
                                               '\n————————————————————'
                                               f'\n═────<b>{subjects_friday_2[0][0]}</b>────═'
                                               '\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {subjects_friday_2[0][1]}  <b>{subjects_friday_2[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {subjects_friday_2[1][1]}  <b>{subjects_friday_2[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {subjects_friday_2[2][1]}  <b>{subjects_friday_2[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {subjects_friday_2[3][1]}  <b>{subjects_friday_2[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {subjects_friday_2[4][1]}  <b>{subjects_friday_2[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {subjects_friday_2[5][1]}  <b>{subjects_friday_2[5][2]}</b>'
                                               '\n————————————————————'
                                               f'\n═────<b>{subjects_saturday_2[0][0]}</b>────═'
                                               f'\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {subjects_saturday_2[0][1]}  <b>{subjects_saturday_2[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {subjects_saturday_2[1][1]}  <b>{subjects_saturday_2[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {subjects_saturday_2[2][1]}  <b>{subjects_saturday_2[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {subjects_saturday_2[3][1]}  <b>{subjects_saturday_2[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {subjects_saturday_2[4][1]}  <b>{subjects_saturday_2[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {subjects_saturday_2[5][1]}  <b>{subjects_saturday_2[5][2]}</b>'
                                               f'\n<b>7</b> |⌛️<i>13:10-13:50</i> {subjects_saturday_2[6][1]}  <b>{subjects_saturday_2[6][2]}</b>'
                                               '\n————————————————————')

monday = (f'═────<b>{subjects_monday_2[0][0]}</b>────═'
                                               f'\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {subjects_monday_2[0][1]}  <b>{subjects_monday_2[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {subjects_monday_2[1][1]}  <b>{subjects_monday_2[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {subjects_monday_2[2][1]}  <b>{subjects_monday_2[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {subjects_monday_2[3][1]}  <b>{subjects_monday_2[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {subjects_monday_2[4][1]}  <b>{subjects_monday_2[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {subjects_monday_2[5][1]}  <b>{subjects_monday_2[5][2]}</b>'
                                               f'\n————————————————————')

tuesday_second = (f'\n═────<b>{subjects_tuesday_2[0][0]}</b>────═'
                                               f'\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {subjects_tuesday_2[0][1]}  <b>{subjects_tuesday_2[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {subjects_tuesday_2[1][1]}  <b>{subjects_tuesday_2[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {subjects_tuesday_2[2][1]}  <b>{subjects_tuesday_2[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {subjects_tuesday_2[3][1]}  <b>{subjects_tuesday_2[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {subjects_tuesday_2[4][1]}  <b>{subjects_tuesday_2[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {subjects_tuesday_2[5][1]}  <b>{subjects_tuesday_2[5][2]}</b>'
                                               f'\n————————————————————')
wednesday_second = (f'\n═────<b>{subjects_wednesday_2[0][0]}</b>────═'
                                               f'\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {subjects_wednesday_2[0][1]}  <b>{subjects_wednesday_2[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {subjects_wednesday_2[1][1]}  <b>{subjects_wednesday_2[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {subjects_wednesday_2[2][1]}  <b>{subjects_wednesday_2[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {subjects_wednesday_2[3][1]}  <b>{subjects_wednesday_2[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {subjects_wednesday_2[4][1]}  <b>{subjects_wednesday_2[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {subjects_wednesday_2[5][1]}  <b>{subjects_wednesday_2[5][2]}</b>'
                                               f'\n————————————————————')
thursday_second = (f'\n═────<b>{subjects_thursday_2[0][0]}</b>────═'
                                               f'\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {subjects_thursday_2[0][1]}  <b>{subjects_thursday_2[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {subjects_thursday_2[1][1]}  <b>{subjects_thursday_2[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {subjects_thursday_2[2][1]}  <b>{subjects_thursday_2[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {subjects_thursday_2[3][1]}  <b>{subjects_thursday_2[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {subjects_thursday_2[4][1]}  <b>{subjects_thursday_2[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {subjects_thursday_2[5][1]}  <b>{subjects_thursday_2[5][2]}</b>'
                                               f'\n————————————————————')
friday =  (f'\n═────<b>{subjects_friday_2[0][0]}</b>────═'
                                               '\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {subjects_friday_2[0][1]}  <b>{subjects_friday_2[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {subjects_friday_2[1][1]}  <b>{subjects_friday_2[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {subjects_friday_2[2][1]}  <b>{subjects_friday_2[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {subjects_friday_2[3][1]}  <b>{subjects_friday_2[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {subjects_friday_2[4][1]}  <b>{subjects_friday_2[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {subjects_friday_2[5][1]}  <b>{subjects_friday_2[5][2]}</b>'
                                               '\n————————————————————')
saturday_second = (f'\n═────<b>{subjects_saturday_2[0][0]}</b>────═'
                                               f'\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {subjects_saturday_2[0][1]}  <b>{subjects_saturday_2[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {subjects_saturday_2[1][1]}  <b>{subjects_saturday_2[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {subjects_saturday_2[2][1]}  <b>{subjects_saturday_2[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {subjects_saturday_2[3][1]}  <b>{subjects_saturday_2[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {subjects_saturday_2[4][1]}  <b>{subjects_saturday_2[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {subjects_saturday_2[5][1]}  <b>{subjects_saturday_2[5][2]}</b>'
                                               f'\n<b>7</b> |⌛️<i>13:10-13:50</i> {subjects_saturday_2[6][1]}  <b>{subjects_saturday_2[6][2]}</b>'
                                               f'\n————————————————————')