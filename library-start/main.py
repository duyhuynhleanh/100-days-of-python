from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import sqlite3
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


# db.create_all()

# new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()


class LibraryForm(FlaskForm):
    title = StringField('Book name', validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    rating = StringField("Rating", validators=[DataRequired()])
    submit = SubmitField('Submit')


# all_books = []


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = LibraryForm()
    if form.validate_on_submit():
        # all_books.append({
        #     "title": form.title.data,
        #     "author": form.author.data,
        #     "rating": form.rating.data,
        # })
        new_book = Book(title=form.title.data, author=form.author.data, rating=form.rating.data)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", form=form)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit_rating.html", book=book_selected)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

