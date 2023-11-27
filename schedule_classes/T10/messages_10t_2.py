import main
import sqlite3 as sql

db = sql.connect('database.db')
cur = db.cursor()

async def add_subjects():
    subject_monday = cur.execute('SELECT title, subj_id FROM subjects_10t_2 WHERE title = "Понедельник"').fetchall()[-1]
    if subject_monday[0] == 'Понедельник' and subject_monday[1] != 6:
        for i in range(1, 7):
            cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['monday']['title'], subjects=subjects['monday']['subjects'][f'{i}'], cabines=subjects['monday']['cabines'][f'{i}']))
            db.commit()
    subject_tuesday = cur.execute('SELECT title, subj_id FROM subjects_10t_2 WHERE title = "Вторник"').fetchall()[-1]
    if subject_tuesday[0] == 'Вторник' and subject_tuesday[1] != 6:
        for i in range(1, 7):
            cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['tuesday']['title'], subjects=subjects['tuesday']['subjects'][f'{i}'], cabines=subjects['tuesday']['cabines'][f'{i}']))
            db.commit()
    subject_wednesday = cur.execute('SELECT title, subj_id FROM subjects_10t_2 WHERE title = "Среда"').fetchall()[-1]
    if subject_tuesday[0] == 'Среда' and subject_tuesday[1] != 6:
        for i in range(1, 7):
            cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['wednesday']['title'], subjects=subjects['wednesday']['subjects'][f'{i}'], cabines=subjects['wednesday']['cabines'][f'{i}']))
            db.commit() 
    subject_thursday = cur.execute('SELECT title, subj_id FROM subjects_10t_2 WHERE title = "Четверг"').fetchall()[-1]
    if subject_thursday[0] == 'Четверг' and subject_thursday[1] != 6: 
        for i in range(1, 7):
            cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['thursday']['title'], subjects=subjects['thursday']['subjects'][f'{i}'], cabines=subjects['thursday']['cabines'][f'{i}']))
            db.commit()
    subject_friday = cur.execute('SELECT title, subj_id FROM subjects_10t_2 WHERE title = "Пятница"').fetchall()[-1]
    if subject_friday[0] == 'Пятница' and subject_friday[1] != 6:
        for i in range(1, 7):
            cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['friday']['title'], subjects=subjects['friday']['subjects'][f'{i}'], cabines=subjects['friday']['cabines'][f'{i}']))
            db.commit()
    subject_saturday = cur.execute('SELECT title, subj_id FROM subjects_10t_2 WHERE title = "Суббота"').fetchall()[-1]
    if subject_saturday[0] == 'Суббота' and subject_saturday[1] != 7:
        for i in range(1, 8):
            cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['saturday']['title'], subjects=subjects['saturday']['subjects'][f'{i}'], cabines=subjects['saturday']['cabines'][f'{i}']))
            db.commit()
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

def update_data(day):
    monday = cur.execute('SELECT title, subjects, cabines FROM subjects_10t_2 WHERE title="Понедельник"').fetchall()
    tuesday = cur.execute('SELECT title, subjects, cabines FROM subjects_10t_2 WHERE title="Вторник"').fetchall()
    wednesday = cur.execute('SELECT title, subjects, cabines FROM subjects_10t_2 WHERE title="Среда"').fetchall()
    thursday = cur.execute('SELECT title, subjects, cabines FROM subjects_10t_2 WHERE title="Четверг"').fetchall()
    friday = cur.execute('SELECT title, subjects, cabines FROM subjects_10t_2 WHERE title="Пятница"').fetchall()
    saturday = cur.execute('SELECT title, subjects, cabines FROM subjects_10t_2 WHERE title="Суббота"').fetchall()
    if day == 'monday':
        return monday
    elif day == 'tuesday':
        return tuesday
    elif day == 'wednesday':
        return wednesday
    elif day == 'thursday':
        return thursday
    elif day == 'friday':
        return friday
    elif day == 'saturday':
        return saturday

full_schedule_second = (                         f'═────<b>{update_data("monday")[0][0]}</b>────═'
                                               '\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {update_data("monday")[0][1]}  <b>{update_data("monday")[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {update_data("monday")[1][1]}  <b>{update_data("monday")[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {update_data("monday")[2][1]}  <b>{update_data("monday")[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {update_data("monday")[3][1]}  <b>{update_data("monday")[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {update_data("monday")[4][1]}  <b>{update_data("monday")[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {update_data("monday")[5][1]}  <b>{update_data("monday")[5][2]}</b>'
                                               '\n————————————————————'
                                               f'\n═────<b>{update_data("tuesday")[0][0]}</b>────═'
                                               '\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {update_data("tuesday")[0][1]}  <b>{update_data("tuesday")[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {update_data("tuesday")[1][1]}  <b>{update_data("tuesday")[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {update_data("tuesday")[2][1]}  <b>{update_data("tuesday")[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {update_data("tuesday")[3][1]}  <b>{update_data("tuesday")[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {update_data("tuesday")[4][1]}  <b>{update_data("tuesday")[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {update_data("tuesday")[5][1]}  <b>{update_data("tuesday")[5][2]}</b>'
                                               '\n————————————————————'
                                               f'\n═────<b>{update_data("wednesday")[0][0]}</b>────═'
                                               '\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {update_data("wednesday")[0][1]}  <b>{update_data("wednesday")[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {update_data("wednesday")[1][1]}  <b>{update_data("wednesday")[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {update_data("wednesday")[2][1]}  <b>{update_data("wednesday")[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {update_data("wednesday")[3][1]}  <b>{update_data("wednesday")[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {update_data("wednesday")[4][1]}  <b>{update_data("wednesday")[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {update_data("wednesday")[5][1]}  <b>{update_data("wednesday")[5][2]}</b>'
                                               '\n————————————————————'
                                               f'\n═────<b>{update_data("thursday")[0][0]}</b>────═'
                                               '\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {update_data("thursday")[0][1]}  <b>{update_data("thursday")[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {update_data("thursday")[1][1]}  <b>{update_data("thursday")[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {update_data("thursday")[2][1]}  <b>{update_data("thursday")[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {update_data("thursday")[3][1]}  <b>{update_data("thursday")[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {update_data("thursday")[4][1]}  <b>{update_data("thursday")[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {update_data("thursday")[5][1]}  <b>{update_data("thursday")[5][2]}</b>'
                                               '\n————————————————————'
                                               f'\n═────<b>{update_data("friday")[0][0]}</b>────═'
                                               '\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {update_data("friday")[0][1]}  <b>{update_data("friday")[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {update_data("friday")[1][1]}  <b>{update_data("friday")[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {update_data("friday")[2][1]}  <b>{update_data("friday")[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {update_data("friday")[3][1]}  <b>{update_data("friday")[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {update_data("friday")[4][1]}  <b>{update_data("friday")[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {update_data("friday")[5][1]}  <b>{update_data("friday")[5][2]}</b>'
                                               '\n————————————————————'
                                               f'\n═────<b>{update_data("saturday")[0][0]}</b>────═'
                                               f'\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {update_data("saturday")[0][1]}  <b>{update_data("saturday")[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {update_data("saturday")[1][1]}  <b>{update_data("saturday")[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {update_data("saturday")[2][1]}  <b>{update_data("saturday")[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {update_data("saturday")[3][1]}  <b>{update_data("saturday")[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {update_data("saturday")[4][1]}  <b>{update_data("saturday")[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {update_data("saturday")[5][1]}  <b>{update_data("saturday")[5][2]}</b>'
                                               f'\n<b>7</b> |⌛️<i>13:10-13:50</i> {update_data("saturday")[6][1]}  <b>{update_data("saturday")[6][2]}</b>'
                                               '\n————————————————————')

monday = (f'═────<b>{update_data("monday")[0][0]}</b>────═'
                                               f'\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {update_data("monday")[0][1]}  <b>{update_data("monday")[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {update_data("monday")[1][1]}  <b>{update_data("monday")[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {update_data("monday")[2][1]}  <b>{update_data("monday")[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {update_data("monday")[3][1]}  <b>{update_data("monday")[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {update_data("monday")[4][1]}  <b>{update_data("monday")[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {update_data("monday")[5][1]}  <b>{update_data("monday")[5][2]}</b>'
                                               f'\n————————————————————')

tuesday_second = (f'\n═────<b>{update_data("tuesday")[0][0]}</b>────═'
                                               f'\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {update_data("tuesday")[0][1]}  <b>{update_data("tuesday")[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {update_data("tuesday")[1][1]}  <b>{update_data("tuesday")[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {update_data("tuesday")[2][1]}  <b>{update_data("tuesday")[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {update_data("tuesday")[3][1]}  <b>{update_data("tuesday")[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {update_data("tuesday")[4][1]}  <b>{update_data("tuesday")[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {update_data("tuesday")[5][1]}  <b>{update_data("tuesday")[5][2]}</b>'
                                               f'\n————————————————————')
wednesday_second = (f'\n═────<b>{update_data("wednesday")[0][0]}</b>────═'
                                               f'\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {update_data("wednesday")[0][1]}  <b>{update_data("wednesday")[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {update_data("wednesday")[1][1]}  <b>{update_data("wednesday")[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {update_data("wednesday")[2][1]}  <b>{update_data("wednesday")[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {update_data("wednesday")[3][1]}  <b>{update_data("wednesday")[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {update_data("wednesday")[4][1]}  <b>{update_data("wednesday")[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {update_data("wednesday")[5][1]}  <b>{update_data("wednesday")[5][2]}</b>'
                                               f'\n————————————————————')
thursday_second = (f'\n═────<b>{update_data("thursday")[0][0]}</b>────═'
                                               f'\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {update_data("thursday")[0][1]}  <b>{update_data("thursday")[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {update_data("thursday")[1][1]}  <b>{update_data("thursday")[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {update_data("thursday")[2][1]}  <b>{update_data("thursday")[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {update_data("thursday")[3][1]}  <b>{update_data("thursday")[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {update_data("thursday")[4][1]}  <b>{update_data("thursday")[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {update_data("thursday")[5][1]}  <b>{update_data("thursday")[5][2]}</b>'
                                               f'\n————————————————————')
friday =  (f'\n═────<b>{update_data("friday")[0][0]}</b>────═'
                                               '\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {update_data("friday")[0][1]}  <b>{update_data("friday")[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {update_data("friday")[1][1]}  <b>{update_data("friday")[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {update_data("friday")[2][1]}  <b>{update_data("friday")[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {update_data("friday")[3][1]}  <b>{update_data("friday")[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {update_data("friday")[4][1]}  <b>{update_data("friday")[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {update_data("friday")[5][1]}  <b>{update_data("friday")[5][2]}</b>'
                                               '\n————————————————————')
saturday_second = (f'\n═────<b>{update_data("saturday")[0][0]}</b>────═'
                                               f'\n————————————————————'
                                               f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {update_data("saturday")[0][1]}  <b>{update_data("saturday")[0][2]}</b>'
                                               f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {update_data("saturday")[1][1]}  <b>{update_data("saturday")[1][2]}</b>'
                                               f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {update_data("saturday")[2][1]}  <b>{update_data("saturday")[2][2]}</b>'
                                               f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {update_data("saturday")[3][1]}  <b>{update_data("saturday")[3][2]}</b>'
                                               f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {update_data("saturday")[4][1]}  <b>{update_data("saturday")[4][2]}</b>'
                                               f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {update_data("saturday")[5][1]}  <b>{update_data("saturday")[5][2]}</b>'
                                               f'\n<b>7</b> |⌛️<i>13:10-13:50</i> {update_data("saturday")[6][1]}  <b>{update_data("saturday")[6][2]}</b>'
                                               f'\n————————————————————')