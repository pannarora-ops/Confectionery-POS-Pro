from app.database import Database

db = Database()

rows = db.fetchall("SELECT * FROM products")

print("Total Products:", len(rows))

for row in rows:
    print(dict(row))

db.close()