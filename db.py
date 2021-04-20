import sqlite3


def CreateDatabase(database):
    global connection
    try:
        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        cursor.execute("CREATE TABLE Users (user_id integer, location text)")

    except sqlite3.OperationalError:
        connection.rollback()
        pass


def DuplicateCheckUSER(user):
    cursor = connection.cursor()

    cursor.execute("SELECT user_id, location from Users;")
    list_users = cursor.fetchall()

    list_users = [x[0] for x in list_users]

    if user not in list_users:
        return True
    else:
        return False


def ExportParameter(user, parameter):
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Users (user_id, location) VALUES (:user_id, :location);",
                   {
                       'user_id': user,
                       'location': parameter.lower()
                   })

    connection.commit()


def UpdateParameter(user, parameter):
    cursor = connection.cursor()

    cursor.execute("UPDATE Users SET location = (:location) WHERE user_id = (:user_id);",
                   {
                       'location': parameter.lower(),
                       'user_id': user
                   })

    connection.commit()


def GetUserLocation(database, user):
    connection3 = sqlite3.connect(database)

    cursor = connection3.cursor()

    cursor.execute("SELECT location from Users WHERE user_id = (:user)",
                   {
                       'user': user
                   })

    lists = cursor.fetchall()

    lists_ = [x[0] for x in lists]

    return lists_[0]


def GetEverything(database, table):
    connection1 = sqlite3.connect(database=database)

    cursor = connection1.cursor()

    cursor.execute('SELECT * from {};'.format(table))

    lists = cursor.fetchall()

    print(lists)
