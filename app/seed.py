from app import db
from app.models import Movie

# Örnek veriler
movie1 = Movie(
    title="The Shawshank Redemption",
    description="Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
    release_date="1994-09-23",
    poster_url="https://example.com/shawshank.jpg"
)
movie2 = Movie(
    title="The Godfather",
    description="The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
    release_date="1972-03-24",
    poster_url="https://example.com/godfather.jpg"
)

# Veritabanına ekleme
db.session.add(movie1)
db.session.add(movie2)
db.session.commit()

print("Veriler başarıyla eklendi.")
