app.listen(process.env.PORT || 5000);
from flask import Flask , render_template , url_for , request
import requests
app = Flask(__name__)
title1="batman"
@app.route("/")
def main():
   rawdata= requests.get("https://fake-api-rest-app.herokuapp.com/movies?q="+title1)
   movies =rawdata.json()
   return render_template("home.html",movies=movies)

@app.route("/<title>")
def movies_by_title(title):
 rawdata= requests.get("https://fake-api-rest-app.herokuapp.com/movies?q="+title)
 movies =rawdata.json()
 return render_template("home.html",movies=movies)


@app.route("/single_movie/<title>")
def single_movie(title):
 rawdata= requests.get("https://fake-api-rest-app.herokuapp.com/movies?title="+title)
 movies =rawdata.json()
 return render_template("single_movie.html",movies=movies)

@app.route("/search")
def search_form():
 return  render_template("search.html")

@app.route("/search_by_title", methods=["POST"])
def search_by_title():
 title =request.form["title"]
 if title !="":
  rawdata= requests.get("https://fake-api-rest-app.herokuapp.com/movies?q="+title)
  movies =rawdata.json()
 return render_template("search.html",movies=movies)

if __name__=="__main__":
    app.run(debug=True)
