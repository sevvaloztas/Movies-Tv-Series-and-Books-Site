from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt
from app.models import User, Content, Movie, TVSeries, Books
from app.forms import RegistrationForm, LoginForm, ContentForm
import os
import secrets
from PIL import Image

# Blueprint tanımlama
main_bp = Blueprint('main', __name__)
movies_bp = Blueprint('movies', __name__, url_prefix='/movies')
tvseries_bp = Blueprint('tvseries', __name__, url_prefix='/tvseries')
books_bp = Blueprint('books', __name__, url_prefix='/books')

# Anasayfa
@main_bp.route('/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

# Film sayfası
@movies_bp.route('/')
def movies_index():
    movies = Movie.query.all()
    if not movies:
        print("No movies found in the database.")
    return render_template('movies.html', movies=movies)

# Dizi sayfası
@tvseries_bp.route('/')
def tvseries_index():
    tvseries = TVSeries.query.all()
    if not tvseries:
        print("No TV series found in the database.")
    return render_template('tvseries.html', tvseries=tvseries)

# Kitap sayfası
@books_bp.route('/')
def books_index():
    books = Books.query.all()
    if not books:
        print("No Books found in the database.")
    return render_template('books.html', books=books)

# Kayıt sayfası
@main_bp.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        picture_file = save_picture(form.picture.data) if form.picture.data else 'default.jpg'
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, image_file=picture_file)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)

# Giriş sayfası
@main_bp.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

# Çıkış yapma
@main_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

# İçerik ekleme sayfası
@main_bp.route("/add_content", methods=['GET', 'POST'])
@login_required
def add_content():
    form = ContentForm()
    if form.validate_on_submit():
        content = Content(title=form.title.data, type=form.type.data, date_watched=form.date_watched.data,
                          rating=form.rating.data, review=form.review.data, author=current_user)
        db.session.add(content)
        db.session.commit()
        flash('Your content has been added!', 'success')
        return redirect(url_for('main.contents'))
    return render_template('add_content.html', title='Add Content', form=form)

# Kullanıcı içeriği görüntüleme
@main_bp.route("/contents")
@login_required
def contents():
    user_contents = Content.query.filter_by(author=current_user).all()
    return render_template('contents.html', contents=user_contents)

# İstatistikler sayfası
@main_bp.route("/statistics")
@login_required
def statistics():
    return render_template('statistics.html', title='Statistics')

# Profil fotoğrafını kaydetme
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

# Blueprint'leri kaydet
main_bp.register_blueprint(movies_bp)
main_bp.register_blueprint(tvseries_bp)
main_bp.register_blueprint(books_bp)
