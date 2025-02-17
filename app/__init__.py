from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config

from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

# Flask uygulamasını oluştur
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:15haziran@localhost:3306/newproje'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['UPLOAD_FOLDER'] = 'static/profile_pics'

# SQLAlchemy ile MySQL veritabanı bağlantısı oluştur
db = SQLAlchemy(app)
migrate = Migrate(app, db)

bcrypt = Bcrypt(app)
csrf = CSRFProtect(app)

# LoginManager instance oluştur ve ayarla
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'

from app import routes

# Migrate instance oluştur
migrate.init_app(app, db)

# Ana route oluştur ve movies tablosunu yükle
@app.route('/')
def index():
    from sqlalchemy import create_engine, MetaData, Table

    # SQLAlchemy ile MySQL veritabanı bağlantısını yeniden oluştur
    engine = create_engine('mysql://root:15haziran@localhost:3306/newproje')
    metadata = MetaData(bind=engine)

    # movies tablosunu yükle
    movies_table = Table('movies', metadata, autoload=True)

    # Örnek sorgu
    query = movies_table.select()
    result = engine.execute(query)

    # Sonuçları yazdırma (örnek olarak)
    for row in result:
        print(row)

    return 'Sonuçlar konsola yazdırıldı'

if __name__ == '__main__':
    app.run(debug=True)

# create_app fonksiyonu Flask uygulamasını başlatmak için
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)  # SQLAlchemy'yi Flask uygulamasına bağla

    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Blueprints kaydı
    from app.routes import main_bp, movies_bp, tvseries_bp, books_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(movies_bp, url_prefix='/movies')
    app.register_blueprint(tvseries_bp, url_prefix='/tvseries')
    app.register_blueprint(books_bp, url_prefix='/books')


    return app




