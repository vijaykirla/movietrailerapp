# Movie Trailer App

This a movie trailer web application created using the Flask framework as frontend and sqllite3 database and sqlalchemy. It has 3 basic features.
1. Displays the list of movies in home page
2. Displays the movie trailer and its story in single page when user click on a movie
3. Add movie page which enables the user to add movie title,story,poster url and youtube url to database

# Setting up development environment on Windows machine

To set up the environment, the following steps must be followed.
1. [Download and install Python](https://www.youtube.com/watch?v=dX2-V2BocqQ), Skip this step if Python is already installed
2. Open windows power shell with administrator privileges and enter the following command to install Python virtual environment
   `pip install virtualenv`
3. Create a new folder and open the windows power shell to browse to the newly created directory `cd <directory path>`
4. To create virtual environment in the new folder, enter the following command in the power shell window
   `virtualenv flaskvenv -p 'C:\Program Files\python.exe'`
5. After successfully creation of virtual environment, activate the environment with the following command
   ` .\flaskvenv\Scripts\activate`
6. Install Flask and sqlalchemy packages using pip command. Please refer to requirements.txt file to find the list of packages installed
   ```
   pip install Flask
   pip install flask-sqlalchemy
   
   ```
7. Download the `movietrailerapp` repository and copy to the virtual environment folder
8. Browse the `movietrailerapp` folder from power shell window and run the command `python app.py`, the server gets started as shown below

   ```
    Use a production WSGI server instead.
    Debug mode: on
    Restarting with stat
    Debugger is active!
    Debugger PIN: 130-926-720
    Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    ```
    
 # Application structure
 
 The application contains the following structure
 
 ```
 movietrailerapp
	|
	|-------static
	|	   |-------css
	|	   |	    |---------styles.css
	|	   |
	|	   |-------images
	|	   |	    |----------logo.png
	|	   |
	|	   |-------js
	|	   	    |----------jquery-3.1.1.min.js
	|
	|--------templates
	|	   |---------layout.html
	|	   |---------movies.html
	|	   |---------newmovie.html
	|	   |---------single.html
	|
	|--------app.py
  
  ```
  
  # Theme
  
  The theme used in this app is open source and can be found [here](https://www.focusoncode.com/template/movies-trailer-free-responsive-html5-template/)
  
  # Test Data
  
  Enter the data in the add movie page shown below:
  ```
  Movie Title: The Shawshank Redemption (1994)
  Movie story: Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.
  Movie poster url: https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_QL50_.jpg
 Youtube trailer url: https://www.youtube.com/watch?v=6hB3S9bIaco
 
 ```
 

 



   
   
   
   
   
