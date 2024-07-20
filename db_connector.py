import pymysql
import pymysql.cursors
import datetime

# MySQL connection details
HOST = 'your_mysql_host'
USER = 'your_mysql_user'
PASSWORD = 'your_mysql_password'
DATABASE = 'your_database_name'

def get_connection():
    try:
        connection = pymysql.connect(host=HOST,
                                     user=USER,
                                     password=PASSWORD,
                                     database=DATABASE,
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def add_user(user_id, user_name):
    connection = get_connection()
    if not connection:
        return {"status": "error", "reason": "database connection failed"}
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (user_id, user_name, creation_date) VALUES (%s, %s, %s)"
            cursor.execute(sql, (user_id, user_name, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            connection.commit()
        return {"status": "ok", "user_added": user_name}
    except pymysql.MySQLError as e:
        return {"status": "error", "reason": "id already exists"}
    finally:
        connection.close()

def get_user(user_id):
    connection = get_connection()
    if not connection:
        return {"status": "error", "reason": "database connection failed"}
    try:
        with connection.cursor() as cursor:
            sql = "SELECT user_name FROM users WHERE user_id = %s"
            cursor.execute(sql, (user_id,))
            result = cursor.fetchone()
            if result:
                return {"status": "ok", "user_name": result['user_name']}
            else:
                return {"status": "error", "reason": "no such id"}
    finally:
        connection.close()

def update_user(user_id, user_name):
    connection = get_connection()
    if not connection:
        return {"status": "error", "reason": "database connection failed"}
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE users SET user_name = %s WHERE user_id = %s"
            cursor.execute(sql, (user_name, user_id))
            connection.commit()
            if cursor.rowcount > 0:
                return {"status": "ok", "user_updated": user_name}
            else:
                return {"status": "error", "reason": "no such id"}
    finally:
        connection.close()

def delete_user(user_id):
    connection = get_connection()
    if not connection:
        return {"status": "error", "reason": "database connection failed"}
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM users WHERE user_id = %s"
            cursor.execute(sql, (user_id,))
            connection.commit()
            if cursor.rowcount > 0:
                return {"status": "ok", "user_deleted": user_id}
            else:
                return {"status": "error", "reason": "no such id"}
    finally:
        connection.close()