import sqlite3 as sql

db_sub = sql.connect('database/subjects.db')
cur_sub = db_sub.cursor()

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
            '5': 'Инд.проект',
            '6': 'Информатика'
        },
        'cabines': {
            '1':'219',
            '2':'206',
            '3':'206',
            '4':'215',
            '5':'216',
            '6':'105'
        }
    },
    'thursday': {
        'title': 'Четверг',
        'subjects': {
            '1': 'Физ-ра',
            '2': 'Химия',
            '3': 'Геометрия',
            '4': 'Информатика',
            '5': 'Англ.яз',
            '6': 'Кл.час',
            '7': 'Физика'
        },
        'cabines': {
            '1':'219',
            '2':'310',
            '3':'216',
            '4':'218',
            '5':'215',
            '6':'216',
            '7': '210'
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
            '6': 'Эл.физика',
            '7': 'Акт.вопр биология'
        },
        'cabines': {
            '1':'216',
            '2':'105',
            '3':'212',
            '4':'315',
            '5':'312',
            '6':'210',
            '7': '311'
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

async def return_schedule(schedule):
    monday = cur_sub.execute('SELECT title, subjects, cabines FROM subjects_10t_2 WHERE title="Понедельник"').fetchall()
    tuesday = cur_sub.execute('SELECT title, subjects, cabines FROM subjects_10t_2 WHERE title="Вторник"').fetchall()
    wednesday = cur_sub.execute('SELECT title, subjects, cabines FROM subjects_10t_2 WHERE title="Среда"').fetchall()
    thursday = cur_sub.execute('SELECT title, subjects, cabines FROM subjects_10t_2 WHERE title="Четверг"').fetchall()
    friday = cur_sub.execute('SELECT title, subjects, cabines FROM subjects_10t_2 WHERE title="Пятница"').fetchall()
    saturday = cur_sub.execute('SELECT title, subjects, cabines FROM subjects_10t_2 WHERE title="Суббота"').fetchall()
    if schedule == 'full':
        full_schedule_second = (                         f'═────<b>{monday[0][0]}</b>────═'
                                                    '\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {monday[0][1]}  <b>{monday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {monday[1][1]}  <b>{monday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {monday[2][1]}  <b>{monday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {monday[3][1]}  <b>{monday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {monday[4][1]}  <b>{monday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {monday[5][1]}  <b>{monday[5][2]}</b>'
                                                    '\n————————————————————'
                                                    f'\n═────<b>{tuesday[0][0]}</b>────═'
                                                    '\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {tuesday[0][1]}  <b>{tuesday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {tuesday[1][1]}  <b>{tuesday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {tuesday[2][1]}  <b>{tuesday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {tuesday[3][1]}  <b>{tuesday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {tuesday[4][1]}  <b>{tuesday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {tuesday[5][1]}  <b>{tuesday[5][2]}</b>'
                                                    '\n————————————————————'
                                                    f'\n═────<b>{wednesday[0][0]}</b>────═'
                                                    '\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {wednesday[0][1]}  <b>{wednesday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {wednesday[1][1]}  <b>{wednesday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {wednesday[2][1]}  <b>{wednesday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {wednesday[3][1]}  <b>{wednesday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {wednesday[4][1]}  <b>{wednesday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {wednesday[5][1]}  <b>{wednesday[5][2]}</b>'
                                                    '\n————————————————————'
                                                    f'\n═────<b>{thursday[0][0]}</b>────═'
                                                    '\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {thursday[0][1]}  <b>{thursday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {thursday[1][1]}  <b>{thursday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {thursday[2][1]}  <b>{thursday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {thursday[3][1]}  <b>{thursday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {thursday[4][1]}  <b>{thursday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {thursday[5][1]}  <b>{thursday[5][2]}</b>'
                                                    f'\n<b>7</b> |⌛️<i>13:10-13:50</i> {thursday[6][1]}  <b>{thursday[6][2]}</b>'
                                                    '\n————————————————————'
                                                    f'\n═────<b>{friday[0][0]}</b>────═'
                                                    '\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {friday[0][1]}  <b>{friday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {friday[1][1]}  <b>{friday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {friday[2][1]}  <b>{friday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {friday[3][1]}  <b>{friday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {friday[4][1]}  <b>{friday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {friday[5][1]}  <b>{friday[5][2]}</b>'
                                                    f'\n<b>7</b> |⌛️<i>13:10-13:50</i> {friday[6][1]}  <b>{friday[6][2]}</b>'
                                                    '\n————————————————————'
                                                    f'\n═────<b>{saturday[0][0]}</b>────═'
                                                    f'\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {saturday[0][1]}  <b>{saturday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {saturday[1][1]}  <b>{saturday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {saturday[2][1]}  <b>{saturday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {saturday[3][1]}  <b>{saturday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {saturday[4][1]}  <b>{saturday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {saturday[5][1]}  <b>{saturday[5][2]}</b>'
                                                    f'\n<b>7</b> |⌛️<i>13:10-13:50</i> {saturday[6][1]}  <b>{saturday[6][2]}</b>'
                                                    '\n————————————————————')
        return full_schedule_second
    if schedule == 'monday':
        monday = (f'═────<b>{monday[0][0]}</b>────═'
                                                    f'\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {monday[0][1]}  <b>{monday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {monday[1][1]}  <b>{monday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {monday[2][1]}  <b>{monday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {monday[3][1]}  <b>{monday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {monday[4][1]}  <b>{monday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {monday[5][1]}  <b>{monday[5][2]}</b>'
                                                    f'\n————————————————————')
        return monday
    if schedule == 'tuesday':
        tuesday_second = (f'\n═────<b>{tuesday[0][0]}</b>────═'
                                                    f'\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {tuesday[0][1]}  <b>{tuesday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {tuesday[1][1]}  <b>{tuesday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {tuesday[2][1]}  <b>{tuesday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {tuesday[3][1]}  <b>{tuesday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {tuesday[4][1]}  <b>{tuesday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {tuesday[5][1]}  <b>{tuesday[5][2]}</b>'
                                                    f'\n————————————————————')
        return tuesday_second
    if schedule == 'wednesday':
        wednesday_second = (f'\n═────<b>{wednesday[0][0]}</b>────═'
                                                    f'\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {wednesday[0][1]}  <b>{wednesday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {wednesday[1][1]}  <b>{wednesday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {wednesday[2][1]}  <b>{wednesday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {wednesday[3][1]}  <b>{wednesday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {wednesday[4][1]}  <b>{wednesday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {wednesday[5][1]}  <b>{wednesday[5][2]}</b>'
                                                    f'\n————————————————————')
        return wednesday_second
    if schedule == 'thursday':
        thursday_second = (f'\n═────<b>{thursday[0][0]}</b>────═'
                                                    f'\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {thursday[0][1]}  <b>{thursday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {thursday[1][1]}  <b>{thursday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {thursday[2][1]}  <b>{thursday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {thursday[3][1]}  <b>{thursday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {thursday[4][1]}  <b>{thursday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {thursday[5][1]}  <b>{thursday[5][2]}</b>'
                                                    f'\n<b>7</b> |⌛️<i>13:10-13:50</i> {thursday[6][1]}  <b>{thursday[6][2]}</b>'
                                                    f'\n————————————————————')
        return thursday_second
    if schedule == 'friday':
        friday = (f'\n═────<b>{friday[0][0]}</b>────═'
                                                    f'\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {friday[0][1]}  <b>{friday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {friday[1][1]}  <b>{friday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {friday[2][1]}  <b>{friday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {friday[3][1]}  <b>{friday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {friday[4][1]}  <b>{friday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {friday[5][1]}  <b>{friday[5][2]}</b>'
                                                    f'\n<b>7</b> |⌛️<i>13:10-13:50</i> {friday[6][1]}  <b>{friday[6][2]}</b>'
                                                    f'\n————————————————————')
        return friday
    if schedule == 'saturday':
        saturday_second = (f'\n═────<b>{saturday[0][0]}</b>────═'
                                                    f'\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>08:00-08:40</i> {saturday[0][1]}  <b>{saturday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>08:50-09:30</i> {saturday[1][1]}  <b>{saturday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>09:40-10:20</i> {saturday[2][1]}  <b>{saturday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>10:40-11:20</i> {saturday[3][1]}  <b>{saturday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>11:40-12:20</i> {saturday[4][1]}  <b>{saturday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>12:25-13:05</i> {saturday[5][1]}  <b>{saturday[5][2]}</b>'
                                                    f'\n<b>7</b> |⌛️<i>13:10-13:50</i> {saturday[6][1]}  <b>{saturday[6][2]}</b>'
                                                    f'\n————————————————————')
        return saturday_second        
