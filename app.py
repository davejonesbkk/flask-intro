from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps
import sqlite3

#read this for help with decorators and wrappers!
#http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/


app = Flask(__name__)

app.secret_key = 'my precious'
app.database = "saple.db"

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('login'))
	return wrap

@app.route('/')
@login_required
def home():
	#return 'Hello, world'
	posts = []
	try:
		g.db  = connect_db() #g is an object specific to Flask used to store temp objects during a request
		cur = g.db.execute('select * from posts')
		
		
		for row in cur.fetchall():
			posts.append(dict(title=row[0], description=row[1]))

		#posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
		#print posts
		g.db.close()
	except sqlite3.OperationalError:
		flash("You have no database")
	return render_template("index.html", posts=posts)	

@app.route('/welcome')
def welcome():
	return render_template("welcome.html")	

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid credentials. Please try again'
		else:
			session['logged_in'] = True
			flash('You were logged in')
			return redirect(url_for('home'))
	return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('You were just logged out')
	return redirect(url_for('welcome'))

def connect_db():
	return sqlite3.connect(app.database)




#start the server with the 'run()' method
if __name__ == '__main__':
	app.run(debug=True)

