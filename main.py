from flask import *
import mysql.connector
from classes.db_connection import Db_Connection


'''mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="bomoko"
)'''

bmk = Flask(__name__)

@bmk.route('/', methods=['GET', 'POST'])
@bmk.route('/home', methods=['GET', 'POST'])
@bmk.route('/index', methods=['GET', 'POST'])
@bmk.route('/accueil', methods=['GET', 'POST'])
def Index():
    if request.method == 'POST':
        inst = Db_Connection()
        mydb = inst.GetConnectionString()
        cur = mydb.cursor()
        notif = request.form['notification']
        sql = 'insert into notification(contenu) values(%s)'
        val = (notif,)
        cur.execute(sql, val)
        mydb.commit()
        cur.close()
        mydb.close()
        return render_template('index.html')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    bmk.run(debug=True, port=5353)