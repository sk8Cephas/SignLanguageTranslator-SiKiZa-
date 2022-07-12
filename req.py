from sqlite3.dbapi2 import connect
from flask import Flask, render_template, url_for, request, redirect

import sqlite3 
from sqlite3 import Error


conn = sqlite3.connect('req.db')
print("connected to database")
sql_create_users_table = 'CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY, firstname text NOT NULL, lastname text NOT NULL,email text NOT NULL);'
                                    
                                   
                                       
                                        
                                        

                                     
conn.execute(sql_create_users_table)
print("table created succcesfully")



sikiza = Flask(__name__) 

# def create_connection(db_file):
#     connection = None;
#     try:
#         conn = sqlite3.connect(db_file)
#         print(sqlite3.version)
#     except Error as e:
#         print(e)

#     return conn


# if __name__ == '__main__':
    # create_connection("module/req.db") 



# def create_table(conn, create_table_sql):
#     try:
#         c = conn.cursor()
#         c.execute(create_table_sql)
#     except Error as e:
#         print(e)

# def main():
#     database = r"module/req.db"

#     sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
#                                         id integer PRIMARY KEY,
#                                         firstname text NOT NULL,
#                                         lastname text NOT NULL,
#                                         email text NOT NULL,
                                        

#                                     ); """

#     conn = create_connection(database)

#     if conn is not None:
        
#         create_table(conn, sql_create_users_table)

#     else:
#         print("Error! cannot create the database connection.")


# if __name__ == '__main__':
#     main()



# @sikiza.route('/d')
# def index():
#     return render_template("api_request.html")



@sikiza.route('/api_request', methods=['POST'])
def api_request():
    if request.method == 'POST':
        try:
            firstname = request.form['fname']
            lastname = request.form['lname']
            email = request.form['email']

            with sqlite3.connect('req.db') as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO databasename.tablename (firstname,lastname,email) VALUES (?,?,?)", (firstname,lastname,email))
                conn.commit()
                msg = 'recorded Successfully'

        except:
            conn.rollback()
            msg = 'error inserting data'
        
        finally:
            render_template("api_request", msg = msg)
            conn.close()
                

        # # c = connect.cursor()
        # guest_fname = request.form.get('fname')
        # guest_lname = request.form.get('lname')
        # guest_email = request.form.get('email')

       

#         try:
#             sql = ("INSERT INTO databasename.tablename (firstname,lastname,email) VALUES (%s, %s, %s)")
#             c.execute(sql,(guest_fname, guest_lname, guest_email,))
#             connection.commit() 
#             #or "conn.commit()" (one of the two)
#             return redirect('/')
#         except:
#             return 'Er ging iets fout met het opslaan van uw gegevens'

       

#     else:
#         return render_template('api_request.html')


if __name__ == '__main__':
    sikiza.run(debug=True)