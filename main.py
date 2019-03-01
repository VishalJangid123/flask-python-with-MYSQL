from flask import Flask,render_template,request, redirect,url_for,jsonify
app = Flask(__name__)


from flaskext.mysql import MySQL
 
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'Movie'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/deletemovie/<name>')
def deletemovie(name):
    connection = mysql.get_db()
    cursor = connection.cursor()
    query="DELETE FROM moive where moviename = %s;"
    cursor.execute(query,(name))
    connection.commit()
    return redirect(url_for('index'))
    
@app.route('/viewmovie')
def index():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from moive;")
    data = cursor.fetchall();
    return render_template("viewMovie.html", data=data)

@app.route('/addmovie',methods=['GET','POST'])
def addmovie():
    if request.method=='POST':
        moviename =request.form['moviename']
        movietiming =request.form['movietiming']
        movielocation =request.form['movielocation']
        connection = mysql.get_db()
        cursor = connection.cursor()
        query="INSERT INTO moive(moviename,Location,timings) VALUES(%s,%s,%s)"
        cursor.execute(query,(moviename,movielocation,movietiming))
        connection.commit()
        return redirect(url_for('index'))
    return render_template("addMovie.html")    

@app.route('/editmovie/<name>',methods=['GET','POST'])
def editmovie(name):
    connection = mysql.get_db()
    cursor = connection.cursor()
    query="select * from moive where movieName = %s"
    cursor.execute(query,(name))
    data =cursor.fetchall()
    connection.commit()
    
    return render_template("editMovie.html", data=data)
##return render_template("editMovie.html",item = data) 
    
@app.route('/updatemovie',methods=['GET','POST'])
def updatemovie():
    if request.method=='POST':
        moviename =request.form['moviename']
        movietiming =request.form['movietiming']
        movielocation =request.form['movielocation']
        connection = mysql.get_db()
        cursor = connection.cursor()
        query="UPDATE moive SET Location = %s,timings = %s where moviename = %s "
        cursor.execute(query,(movielocation,movietiming,moviename))
        connection.commit()
        return redirect(url_for('index'))
  
    


if __name__ == '__main__':
   app.run(debug = True)
