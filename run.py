from app import db, create_app

# Flask uygulamasını başlat
app = create_app()

with app.app_context():
    db.create_all()
    print("Database tables created.")

if __name__ == '__main__':
    app.run(debug=True)


