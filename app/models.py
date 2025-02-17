from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    date_watched = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Content('{self.title}', '{self.type}', '{self.date_watched}')"

class Movie(db.Model):
    __tablename__ = 'movies'  # Tablo adını belirtin
    __table_args__ = {'schema': 'newproje'}  # Şema adını belirtin
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    release_date = db.Column(db.Date, nullable=True)
    poster_url = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"Movie('{self.title}', '{self.release_date}')"
    
class TVSeries(db.Model):
    __tablename__ = 'tvseries'  # Tablo adını belirtin
    __table_args__ = {'schema': 'newproje'}  # Şema adını belirtin

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    release_date = db.Column(db.String(20), nullable=False)
    poster_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"TVSeries('{self.title}', '{self.release_date}')"
    

class Books(db.Model):
    __tablename__ = 'books'
    __table_args__ = {'schema': 'newproje'}  # Şema adını belirtin

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255))
    description = db.Column(db.Text, nullable=False)
    cover_url = db.Column(db.String(255))

    def __repr__(self):
        return f"Books(title={self.title}, author={self.author})"

