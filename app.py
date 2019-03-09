import os
import re
from flask import Flask,render_template,request,redirect,flash,url_for
from flask_sqlalchemy import SQLAlchemy

# Creating a Flask application object and setting up the URI of the database to be used.

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "moviesdatabase.db"))

app = Flask(__name__)
app.secret_key = 'random string'    
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Creating an object of SQLAlchemy class with Flask application object as the parameter
db = SQLAlchemy(app)

class Movies(db.Model):
    # Movies class inherited from db model    
    id = db.Column('id',db.Integer,primary_key = True)
    title = db.Column(db.Text)
    story = db.Column(db.Text)
    poster_url = db.Column(db.Text)
    youtube_url = db.Column(db.Text)
    youtube_url_id = db.Column(db.Text)

    def __init__(self,title,story,poster_url,youtube_url,youtube_url_id):
        self.title = title
        self.story = story
        self.poster_url = poster_url
        self.youtube_url = youtube_url
        self.youtube_url_id = youtube_url_id

@app.route('/')
def movies():
    # This method is used to retrieve movies from movies database and render html
    return render_template('movies.html', movies=Movies.query.all())

@app.route('/trailer/<youtubeid>')
def trailer(youtubeid):
    '''
    This method is used to retrieve single movie from movies database based on youtube trailer id
    and render the html
    '''
    movie = None
    movie = Movies.query.filter_by(youtube_url_id = youtubeid).first()
    return render_template('single.html',movie = movie)

@app.route('/new',methods = ['GET','POST'])
def addmovie():
    '''
    This method checks the http request, if the request method is post, it validated the entered data
    and saves the new movie to database and redirects to the movies page, else if the request is get then
    it renders the newmovie html
    '''
    if request.method == 'POST':
        if not request.form['title'] or not request.form['story'] or not request.form['poster_url'] or not request.form['youtube_url']:
            flash('Please enter all the fields', 'error')
        else:
            # Extract the youtube ID from the url
            youtube_id_match = re.search(r'(?<=v=)[^&#]+', request.form['youtube_url'])
            youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', request.form['youtube_url'])
            trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

            movie = Movies(request.form['title'],request.form['story'],request.form['poster_url'],request.form['youtube_url'],trailer_youtube_id)
            db.session.add(movie)
            db.session.commit()

            flash('Record was successfully added')
            return redirect(url_for('movies'))


    return render_template('newmovie.html')

if __name__ == "__main__":
    '''
    When the application runs db.create_all will check for the database and creates 
    if no database is found
    '''
    db.create_all()
    app.run(debug=True)

