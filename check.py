import mysql.connector

def main():
    try:
        # MySQL veritabanı bağlantısı kurma
        db_connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='15haziran',
            database='newproje'
        )

        # MySQL bağlantısı üzerinden bir cursor (imleç) oluşturma
        cursor = db_connection.cursor()

        # SQL sorgusu
        sql_query = """
        SELECT newproje.movies.id AS newproje_movies_id,
               newproje.movies.title AS newproje_movies_title,
               newproje.movies.description AS newproje_movies_description,
               newproje.movies.release_date AS newproje_movies_release_date,
               newproje.movies.poster_url AS newproje_movies_poster_url
        FROM newproje.movies
        """

        query = "SELECT * FROM movies WHERE id = 1"

        # SQL sorgusunu çalıştırma
        cursor.execute(sql_query)

        # Sonuçları alıp işleme
        movies = cursor.fetchall()

        # Sonuçları yazdırma (örnek olarak)
        for movie in movies:
            print(movie)

    except mysql.connector.Error as err:
        print(f"Hata: {err}")

    finally:
        # Bağlantıyı kapatma
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()

if __name__ == "__main__":
    main()
