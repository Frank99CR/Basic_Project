import psycopg2

import psycopg2

connection  = psycopg2.connect(
    host="localhost", 
    port="5432",
    user="root",
    password="root",
    dbname="modulo2_sql"
)
print("Connected to database")

cursor = connection.cursor()

# cursor.execute("SELECT version();")
# cursor.execute("SELECT username, password, age, status FROM sql_modulo2.users;")
cursor.execute(
    "INSERT INTO sql_modulo2.users (username, password, age, status) values ('user@admin.com', 'password123', '25', 'Inactive')"
)
print("Query executed")

connection.commit()
print("Connection changes committed")

# def format_user_data(user_record):
# 	return {
# 		"username": user_record[0],
# 		"password": user_record[1],
# 		"age": user_record[2],
# 		"status":  user_record[3]
# 	}


# results = cursor.fetchall()
# formatted_results = [format_user_data(result) for result in results]
# # print(results)

# print(formatted_results)
