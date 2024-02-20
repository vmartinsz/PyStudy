import connect

connection = connect.connection

def addUser(username, password, email):
    cursor = connection.cursor()

    try:
        cursor.execute('INSERT INTO Users (username, password, email) VALUES (%s, %s, %s)',
                       (username, password, email))
        connection.commit()

    except Exception as e:
        raise Exception(f'Error: {e}')
    
    finally:
        cursor.close()

def getUser(username, password):
    cursor = connection.cursor()

    try:
        cursor.execute('SELECT * FROM Users WHERE username = %s AND password = %s', (username, password))
        result = cursor.fetchall()
        return result
    
    except Exception as e:
        raise Exception(f'Error> {e}')
    
    finally:
        cursor.close()

def editUser(object, value, idUser):
    cursor = connection.cursor()

    try:
        query = f'UPDATE Users SET {object} = %s WHERE idUser = %s'
        params = (value, idUser)
        cursor.execute(query, params)
        connection.commit()

    except Exception as e:
        raise Exception(f'Error: {e}')
    
    finally:
        cursor.close()

def deleteUser(username, password):
    cursor = connection.cursor()

    try:
        cursor.execute('DELETE FROM Users WHERE username = %s AND password = %s', 
                       (username, password))
        connection.commit()

    except Exception as e:
        raise Exception(f'Error: {e}')
    
    finally:
        cursor.close()

def specificData(unknown, tableName,dataPersonal, value):
    cursor = connection.cursor()

    try:
        query = f'SELECT {unknown} FROM {tableName} WHERE {dataPersonal} = %s'
        params = (value,)
        cursor.execute(query, params)
        result = cursor.fetchone()

        if result:
            return result[0]
        else:
            return None
        
    except Exception as e:
        raise Exception(f'Error: {e}')
    
    finally:
        cursor.close()

def addActivity(activityName, matter, stage, idUser):
    cursor = connection.cursor()

    try:
        cursor.execute('INSERT INTO Activities (nameActivity, matter, stage, idUser) VALUES (%s, %s, %s, %s)',
                   (activityName, matter, stage, idUser))
        connection.commit()

    except Exception as e:
        raise Exception(f'Error: {e}')
    
    finally:
        cursor.close()

def deleteActivity(idActivity):
    cursor = connection.cursor()
    try:
            cursor.execute('DELETE FROM Activities WHERE idActivities = %s', (idActivity,))
            connection.commit()

    except Exception as e:
        raise Exception(f'ErroR: {e}')
    
    finally:
        cursor.close()


def editActivity(nameActivity, matter, stage, idActivity):
    cursor = connection.cursor()

    try:
        query = f'UPDATE Activities SET nameActivity = %s, matter = %s, stage = %s WHERE idActivities = %s'
        params = (nameActivity, matter, stage, idActivity)
        cursor.execute(query, params)
        connection.commit()

    except Exception as e:
        raise Exception(f'Error: {e}')
    
    finally:
        cursor.close()

def listActivities(idUser):
    cursor = connection.cursor()

    try:
        cursor.execute('SELECT * FROM Activities WHERE idUser = %s', 
                       (idUser,))
        columns = [col[0] for col in cursor.description]
        results = cursor.fetchall()
        activities_list = []

        for row in results:
            activity_dict = dict(zip(columns, row))
            activities_list.append(activity_dict)
        return activities_list
    
    except Exception as e:
        raise Exception(f'Error: {e}')
    
    finally:
        cursor.close()


def deleteAllActivities():
    cursor = connection.cursor()

    try:
        cursor.execute('DELETE FROM Activities')
        connection.commit()
    
    except Exception as e:
        raise Exception(f'Error: {e}')
    
    finally:
        cursor.close()


def deleteAllUsers():
    cursor = connection.cursor()

    try:
        cursor.execute('DELETE FROM Users')
        connection.commit()
    
    except Exception as e:
        raise Exception(f'Error: {e}')
    
    finally:
        cursor.close()


