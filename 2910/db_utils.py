import mysql.connector
from config import USER, PASSWORD, HOST

class DbConnectionError(Exception):
    pass

def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    
    return cnx

def get_completed_tasks():
    completed = []
    try:
        db_name = 'TASKStest'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print (f'Connected to db: {db_name}')
        
        query = "SELECT * FROM Monday WHERE Completed = 1"
        
        cur.execute(query)
        
        result = cur.fetchall()
        completed = result
        print(completed)
        cur.close()
        
    except Exception:
        raise DbConnectionError('Failed to read data from DB during get_completed_tasks function')
    
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
    
def add_task():
    try:
        db_name = 'TASKStest'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print (f'Connected to db: {db_name}')
        
        new_task = {
            'TaskTitle': 'test task title',
            'TaskDescription': 'test task description',
            'Completed': '1'
        }

        query = "INSERT INTO Monday (TaskTitle, TaskDescription, Completed) VALUES (%s, %s, %s)"

        cur.execute(query, (new_task['TaskTitle'], new_task['TaskDescription'], new_task['Completed']))

        db_connection.commit()
        cur.close()
        
    except Exception:
        raise DbConnectionError('Failed to add task during add_task func')
    
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
            
if __name__ == '__main__':
    # add_task()
    get_completed_tasks()