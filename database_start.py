import schedule_classes.T10.messages_10t_2 as msg_10t_2
import schedule_classes.T10.messages_10t_1 as msg_10t_1

import sqlite3 as sql

db = sql.connect('database.db')
cur = db.cursor()

async def main_db_start():
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                tg_id INTEGER,
                class_id TEXT DEFAULT '',
                group_id INTEGER DEFAULT 0,
                isNotified INTEGER DEFAULT 0
                )""")    
    db.commit()

async def create_subjects_1():
    cur.execute('''CREATE TABLE IF NOT EXISTS subjects_10t_1 (
        title TEXT NOT NULL,
        subj_id INTEGER DEFAULT 0,
        subjects TEXT NOT NULL,
        cabines INTEGER NOT NULL
    )''')
    db.commit()

async def create_subjects_2():
    cur.execute('''CREATE TABLE IF NOT EXISTS subjects_10t_2 (
        title TEXT NOT NULL,
        subj_id INTEGER DEFAULT 0,
        subjects TEXT NOT NULL,
        cabines INTEGER NOT NULL
    )''')
    db.commit()

async def t10_db_start_1():
    for i in range(1, 7):
        cur.execute('INSERT INTO subjects_10t_1 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=msg_10t_1.subjects['monday']['title'], subjects=msg_10t_1.subjects['monday']['subjects'][f'{i}'], cabines=msg_10t_1.subjects['monday']['cabines'][f'{i}']))
        db.commit()
    for i in range(1, 7):
        cur.execute('INSERT INTO subjects_10t_1 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=msg_10t_1.subjects['tuesday']['title'], subjects=msg_10t_1.subjects['tuesday']['subjects'][f'{i}'], cabines=msg_10t_1.subjects['tuesday']['cabines'][f'{i}']))
        db.commit()
    for i in range(1, 7):
        cur.execute('INSERT INTO subjects_10t_1 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=msg_10t_1.subjects['wednesday']['title'], subjects=msg_10t_1.subjects['wednesday']['subjects'][f'{i}'], cabines=msg_10t_1.subjects['wednesday']['cabines'][f'{i}']))
        db.commit()
    for i in range(1, 7):
        cur.execute('INSERT INTO subjects_10t_1 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=msg_10t_1.subjects['thursday']['title'], subjects=msg_10t_1.subjects['thursday']['subjects'][f'{i}'], cabines=msg_10t_1.subjects['thursday']['cabines'][f'{i}']))
        db.commit()
    for i in range(1, 7):
        cur.execute('INSERT INTO subjects_10t_1 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=msg_10t_1.subjects['friday']['title'], subjects=msg_10t_1.subjects['friday']['subjects'][f'{i}'], cabines=msg_10t_1.subjects['friday']['cabines'][f'{i}']))
        db.commit()
    for i in range(1, 8):
        cur.execute('INSERT INTO subjects_10t_1 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=msg_10t_1.subjects['saturday']['title'], subjects=msg_10t_1.subjects['saturday']['subjects'][f'{i}'], cabines=msg_10t_1.subjects['saturday']['cabines'][f'{i}']))
        db.commit()


async def t10_db_start_2():
    for i in range(1, 7):
        cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=msg_10t_2.subjects['monday']['title'], subjects=msg_10t_2.subjects['monday']['subjects'][f'{i}'], cabines=msg_10t_2.subjects['monday']['cabines'][f'{i}']))
        db.commit()
    for i in range(1, 7):
        cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=msg_10t_2.subjects['tuesday']['title'], subjects=msg_10t_2.subjects['tuesday']['subjects'][f'{i}'], cabines=msg_10t_2.subjects['tuesday']['cabines'][f'{i}']))
        db.commit()
    for i in range(1, 7):
        cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=msg_10t_2.subjects['wednesday']['title'], subjects=msg_10t_2.subjects['wednesday']['subjects'][f'{i}'], cabines=msg_10t_2.subjects['wednesday']['cabines'][f'{i}']))
        db.commit()
    for i in range(1, 7):
        cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=msg_10t_2.subjects['thursday']['title'], subjects=msg_10t_2.subjects['thursday']['subjects'][f'{i}'], cabines=msg_10t_2.subjects['thursday']['cabines'][f'{i}']))
        db.commit()
    for i in range(1, 7):
        cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=msg_10t_2.subjects['friday']['title'], subjects=msg_10t_2.subjects['friday']['subjects'][f'{i}'], cabines=msg_10t_2.subjects['friday']['cabines'][f'{i}']))
        db.commit()
    for i in range(1, 8):
        cur.execute('INSERT INTO subjects_10t_2 (subj_id, title, subjects, cabines) VALUES("{subj_id}", "{title}", "{subjects}", "{cabines}")'.format(subj_id=i, title=msg_10t_2.subjects['saturday']['title'], subjects=msg_10t_2.subjects['saturday']['subjects'][f'{i}'], cabines=msg_10t_2.subjects['saturday']['cabines'][f'{i}']))
        db.commit()
