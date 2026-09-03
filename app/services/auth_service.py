from app.database import Database


class AuthService:

    @staticmethod
    def login(username, password):

        db = Database()

        db.cursor.execute(
            """
            SELECT *
            FROM users
            WHERE username=?
            AND password=?
            """,
            (username, password),
        )

        user = db.cursor.fetchone()

        db.close()

        return user