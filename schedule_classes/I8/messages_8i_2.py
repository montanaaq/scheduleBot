import sqlite3 as sql

db_sub = sql.connect('database/subjects.db')
cur_sub = db_sub.cursor()

async def create_subjects_2():
    cur_sub.execute('''CREATE TABLE IF NOT EXISTS subjects_8i_2 (
        title TEXT NOT NULL,
        subj_id INTEGER DEFAULT 0,
        subjects TEXT NOT NULL,
        cabines INTEGER NOT NULL
    )''')
    db_sub.commit()


async def i8_db_start_2():
    for i in range(1, 7):
        cur_sub.execute('INSERT INTO subjects_8i_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['monday']['title'], subjects=subjects['monday']['subjects'][f'{i}'], cabines=subjects['monday']['cabines'][f'{i}']))
        db_sub.commit()
    for i in range(1, 8):
        cur_sub.execute('INSERT INTO subjects_8i_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['tuesday']['title'], subjects=subjects['tuesday']['subjects'][f'{i}'], cabines=subjects['tuesday']['cabines'][f'{i}']))
        db_sub.commit()
    for i in range(1, 8):
        cur_sub.execute('INSERT INTO subjects_8i_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['wednesday']['title'], subjects=subjects['wednesday']['subjects'][f'{i}'], cabines=subjects['wednesday']['cabines'][f'{i}']))
        db_sub.commit()
    for i in range(1, 8):
        cur_sub.execute('INSERT INTO subjects_8i_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['thursday']['title'], subjects=subjects['thursday']['subjects'][f'{i}'], cabines=subjects['thursday']['cabines'][f'{i}']))
        db_sub.commit()
    for i in range(1, 8):
        cur_sub.execute('INSERT INTO subjects_8i_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['friday']['title'], subjects=subjects['friday']['subjects'][f'{i}'], cabines=subjects['friday']['cabines'][f'{i}']))
        db_sub.commit()
    for i in range(1, 8):
        cur_sub.execute('INSERT INTO subjects_8i_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=subjects['saturday']['title'], subjects=subjects['saturday']['subjects'][f'{i}'], cabines=subjects['saturday']['cabines'][f'{i}']))
        db_sub.commit()


subjects = {
    'monday': {
        'title': 'Понедельник',
        'subjects': {
            '1': 'Разговоры о важном',
            '2': 'Биология',
            '3': 'Алгебра',
            '4': 'Литер',
            '5': 'ОБЖ',
            '6': 'Химия'
        },
        'cabines': {
            '1':'316',
            '2':'212',
            '3':'216',
            '4':'316',
            '5':'316',
            '6':'310'
        }
    },
    'tuesday': {
        'title': 'Вторник',
        'subjects': {
            '1': 'География',
            '2': 'Рус.яз',
            '3': 'Родн.яз',
            '4': 'Биофизика',
            '5': 'Физика',
            '6': 'История',
            '7': 'Физ-ра'
        },
        'cabines': {
            '1':'212',
            '2':'316',
            '3':'316/110/313а',
            '4':'312',
            '5':'210',
            '6':'105',
            '7': 'Спорт зал'
        }
    },
    'wednesday': {
        'title': 'Среда',
        'subjects': {
            '1': 'Родн.лит',
            '2': 'Геометрия',
            '3': 'Вероятность',
            '4': 'Рус.яз',
            '5': 'Общество',
            '6': 'География',
            '7': 'Кл.час'
        },
        'cabines': {
            '1':'208/318/313a',
            '2':'216',
            '3':'216',
            '4':'316',
            '5':'105',
            '6':'212',
            '7': '316'
        }
    },
    'thursday': {
        'title': 'Четверг',
        'subjects': {
            '1': 'Физика',
            '2': 'Англ.яз',
            '3': 'Франц.яз',
            '4': 'Проектирование',
            '5': 'Химия',
            '6': 'Физика',
            '7': 'Технология'
        },
        'cabines': {
            '1':'210',
            '2':'215',
            '3':'316',
            '4':'317',
            '5':'310',
            '6':'210',
            '7': '110'
        }
    },
    'friday': {
        'title': 'Пятница',
        'subjects': {
            '1': 'Алгебра',
            '2': 'Литер',
            '3': 'Информатика',
            '4': 'Франц.яз',
            '5': 'Информатика',
            '6': 'Биология',
            '7': 'Геометрия'
        },
        'cabines': {
            '1':'216',
            '2':'316',
            '3':'218',
            '4':'313',
            '5':'218',
            '6':'312',
            '7':'216'
        }
    },
    'saturday': {
        'title': 'Суббота',
        'subjects': {
            '1': 'Физ-ра',
            '2': 'Программирование',
            '3': 'Англ.яз',
            '4': 'Англ.яз',
            '5': 'История',
            '6': 'Родн.яз',
            '7': 'Музыка'
        },
        'cabines': {
            '1':'219',
            '2':'218',
            '3':'215',
            '4':'215',
            '5':'105',
            '6':'129/18/313a',
            '7':'129'
        }
    }
}

async def return_schedule(schedule):
    monday = cur_sub.execute('SELECT title, subjects, cabines FROM subjects_8i_2 WHERE title="Понедельник"').fetchall()
    tuesday = cur_sub.execute('SELECT title, subjects, cabines FROM subjects_8i_2 WHERE title="Вторник"').fetchall()
    wednesday = cur_sub.execute('SELECT title, subjects, cabines FROM subjects_8i_2 WHERE title="Среда"').fetchall()
    thursday = cur_sub.execute('SELECT title, subjects, cabines FROM subjects_8i_2 WHERE title="Четверг"').fetchall()
    friday = cur_sub.execute('SELECT title, subjects, cabines FROM subjects_8i_2 WHERE title="Пятница"').fetchall()
    saturday = cur_sub.execute('SELECT title, subjects, cabines FROM subjects_8i_2 WHERE title="Суббота"').fetchall()
    if schedule == 'full':
        full_schedule_second = (                         f'═────<b>{monday[0][0]}</b>────═'
                                                    '\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>12:25-13:05</i> {monday[0][1]}  <b>{monday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>13:20-14:00</i> {monday[1][1]}  <b>{monday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>14:10-14:50</i> {monday[2][1]}  <b>{monday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>15:05-15:45</i> {monday[3][1]}  <b>{monday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>15:50-16:30</i> {monday[4][1]}  <b>{monday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>16:35-17:15</i> {monday[5][1]}  <b>{monday[5][2]}</b>'
                                                    '\n————————————————————'
                                                    f'\n═────<b>{tuesday[0][0]}</b>────═'
                                                    '\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>12:25-13:05</i> {tuesday[0][1]}  <b>{tuesday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>13:20-14:00</i> {tuesday[1][1]}  <b>{tuesday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>14:10-14:50</i> {tuesday[2][1]}  <b>{tuesday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>15:05-15:45</i> {tuesday[3][1]}  <b>{tuesday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>15:50-16:30</i> {tuesday[4][1]}  <b>{tuesday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>16:35-17:15</i> {tuesday[5][1]}  <b>{tuesday[5][2]}</b>'
                                                    f'\n<b>7</b> |⌛️<i>17:20-18:00</i> {tuesday[6][1]}  <b>{tuesday[6][2]}</b>'
                                                    '\n————————————————————'
                                                    f'\n═────<b>{wednesday[0][0]}</b>────═'
                                                    '\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>12:25-13:05</i> {wednesday[0][1]}  <b>{wednesday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>13:20-14:00</i> {wednesday[1][1]}  <b>{wednesday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>14:10-14:50</i> {wednesday[2][1]}  <b>{wednesday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>15:05-15:45</i> {wednesday[3][1]}  <b>{wednesday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>15:50-16:30</i> {wednesday[4][1]}  <b>{wednesday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>16:35-17:15</i> {wednesday[5][1]}  <b>{wednesday[5][2]}</b>'
                                                    f'\n<b>7</b> |⌛️<i>17:20-18:00</i> {wednesday[6][1]}  <b>{wednesday[6][2]}</b>'
                                                    '\n————————————————————'
                                                    f'\n═────<b>{thursday[0][0]}</b>────═'
                                                    '\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>12:25-13:05</i> {thursday[0][1]}  <b>{thursday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>13:20-14:00</i> {thursday[1][1]}  <b>{thursday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>14:10-14:50</i> {thursday[2][1]}  <b>{thursday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>15:05-15:45</i> {thursday[3][1]}  <b>{thursday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>15:50-16:30</i> {thursday[4][1]}  <b>{thursday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>16:35-17:15</i> {thursday[5][1]}  <b>{thursday[5][2]}</b>'
                                                    f'\n<b>7</b> |⌛️<i>17:20-18:00</i> {thursday[6][1]}  <b>{thursday[6][2]}</b>'
                                                    '\n————————————————————'
                                                    f'\n═────<b>{friday[0][0]}</b>────═'
                                                    '\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>12:25-13:05</i> {friday[0][1]}  <b>{friday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>13:20-14:00</i> {friday[1][1]}  <b>{friday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>14:10-14:50</i> {friday[2][1]}  <b>{friday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>15:05-15:45</i> {friday[3][1]}  <b>{friday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>15:50-16:30</i> {friday[4][1]}  <b>{friday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>16:35-17:15</i> {friday[5][1]}  <b>{friday[5][2]}</b>'
                                                    f'\n<b>7</b> |⌛️<i>17:20-18:00</i> {friday[6][1]}  <b>{friday[6][2]}</b>'
                                                    '\n————————————————————'
                                                    f'\n═────<b>{saturday[0][0]}</b>────═'
                                                    f'\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>12:25-13:05</i> {saturday[0][1]}  <b>{saturday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>13:20-14:00</i> {saturday[1][1]}  <b>{saturday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>14:10-14:50</i> {saturday[2][1]}  <b>{saturday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>15:05-15:45</i> {saturday[3][1]}  <b>{saturday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>15:50-16:30</i> {saturday[4][1]}  <b>{saturday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>16:35-17:15</i> {saturday[5][1]}  <b>{saturday[5][2]}</b>'
                                                    f'\n<b>7</b> |⌛️<i>17:20-18:00</i> {saturday[6][1]}  <b>{saturday[6][2]}</b>'
                                                    '\n————————————————————')
        return full_schedule_second
    if schedule == 'monday':
        monday = (f'═────<b>{monday[0][0]}</b>────═'
                                                    f'\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>12:25-13:05</i> {monday[0][1]}  <b>{monday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>13:20-14:00</i> {monday[1][1]}  <b>{monday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>14:10-14:50</i> {monday[2][1]}  <b>{monday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>15:05-15:45</i> {monday[3][1]}  <b>{monday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>15:50-16:30</i> {monday[4][1]}  <b>{monday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>16:35-17:15</i> {monday[5][1]}  <b>{monday[5][2]}</b>'
                                                    f'\n————————————————————')
        return monday
    if schedule == 'tuesday':
        tuesday_second = (f'\n═────<b>{tuesday[0][0]}</b>────═'
                                                    f'\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>12:25-13:05</i> {tuesday[0][1]}  <b>{tuesday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>13:20-14:00</i> {tuesday[1][1]}  <b>{tuesday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>14:10-14:50</i> {tuesday[2][1]}  <b>{tuesday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>15:05-15:45</i> {tuesday[3][1]}  <b>{tuesday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>15:50-16:30</i> {tuesday[4][1]}  <b>{tuesday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>16:35-17:15</i> {tuesday[5][1]}  <b>{tuesday[5][2]}</b>'
                                                    f'\n<b>7</b> |⌛️<i>17:20-18:00</i> {tuesday[6][1]}  <b>{tuesday[6][2]}</b>'
                                                    f'\n————————————————————')
        return tuesday_second
    if schedule == 'wednesday':
        wednesday_second = (f'\n═────<b>{wednesday[0][0]}</b>────═'
                                                    f'\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>12:25-13:05</i> {wednesday[0][1]}  <b>{wednesday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>13:20-14:00</i> {wednesday[1][1]}  <b>{wednesday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>14:10-14:50</i> {wednesday[2][1]}  <b>{wednesday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>15:05-15:45</i> {wednesday[3][1]}  <b>{wednesday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>15:50-16:30</i> {wednesday[4][1]}  <b>{wednesday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>16:35-17:15</i> {wednesday[5][1]}  <b>{wednesday[5][2]}</b>'
                                                    f'\n<b>7</b> |⌛️<i>17:20-18:00</i> {wednesday[6][1]}  <b>{wednesday[6][2]}</b>'
                                                    f'\n————————————————————')
        return wednesday_second
    if schedule == 'thursday':
        thursday_second = (f'\n═────<b>{thursday[0][0]}</b>────═'
                                                    f'\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>12:25-13:05</i> {thursday[0][1]}  <b>{thursday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>13:20-14:00</i> {thursday[1][1]}  <b>{thursday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>14:10-14:50</i> {thursday[2][1]}  <b>{thursday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>15:05-15:45</i> {thursday[3][1]}  <b>{thursday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>15:50-16:30</i> {thursday[4][1]}  <b>{thursday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>16:35-17:15</i> {thursday[5][1]}  <b>{thursday[5][2]}</b>'
                                                    f'\n<b>7</b> |⌛️<i>17:20-18:00</i> {thursday[6][1]}  <b>{thursday[6][2]}</b>'
                                                    f'\n————————————————————')
        return thursday_second
    if schedule == 'friday':
        friday = (f'\n═────<b>{friday[0][0]}</b>────═'
                                                    f'\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>12:25-13:05</i> {friday[0][1]}  <b>{friday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>13:20-14:00</i> {friday[1][1]}  <b>{friday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>14:10-14:50</i> {friday[2][1]}  <b>{friday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>15:05-15:45</i> {friday[3][1]}  <b>{friday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>15:50-16:30</i> {friday[4][1]}  <b>{friday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>16:35-17:15</i> {friday[5][1]}  <b>{friday[5][2]}</b>'
                                                    f'\n<b>7</b> |⌛️<i>17:20-18:00</i> {friday[6][1]}  <b>{friday[6][2]}</b>'
                                                    f'\n————————————————————')
        return friday
    if schedule == 'saturday':
        saturday_second = (f'\n═────<b>{saturday[0][0]}</b>────═'
                                                    f'\n————————————————————'
                                                    f'\n<b>1</b> |⌛️<i>12:25-13:05</i> {saturday[0][1]}  <b>{saturday[0][2]}</b>'
                                                    f'\n<b>2</b> |⌛️<i>13:20-14:00</i> {saturday[1][1]}  <b>{saturday[1][2]}</b>'
                                                    f'\n<b>3</b> |⌛️<i>14:10-14:50</i> {saturday[2][1]}  <b>{saturday[2][2]}</b>'
                                                    f'\n<b>4</b> |⌛️<i>15:05-15:45</i> {saturday[3][1]}  <b>{saturday[3][2]}</b>'
                                                    f'\n<b>5</b> |⌛️<i>15:50-16:30</i> {saturday[4][1]}  <b>{saturday[4][2]}</b>'
                                                    f'\n<b>6</b> |⌛️<i>16:35-17:15</i> {saturday[5][1]}  <b>{saturday[5][2]}</b>'
                                                    f'\n<b>7</b> |⌛️<i>17:20-18:00</i> {saturday[6][1]}  <b>{saturday[6][2]}</b>'
                                                    f'\n————————————————————')
        return saturday_second        
