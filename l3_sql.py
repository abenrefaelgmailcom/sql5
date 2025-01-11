import sqlite3
import os  # נדרש לבדוק אם קובץ קיים ולמחוק אותו

# אתגר: בדיקה אם קובץ מסד הנתונים קיים ומחיקתו אם כן
db_name = "hw_solutionnn.db"
if os.path.exists(db_name):
    os.remove(db_name)
    print(f"db '{db_name}' deleted.")
else:
    print(f"db '{db_name}' not exist, create new one.")

# התחברות למסד הנתונים
conn = sqlite3.connect(db_name)
conn.row_factory = sqlite3.Row  # מאפשר שימוש בשמות עמודות
cursor = conn.cursor()

# יצירת הטבלה shopping
cursor.execute('''
CREATE TABLE shopping (
    id INTEGER PRIMARY KEY,
    name TEXT,
    amount INTEGER
)
''')
print("table shopping created.")

# הכנסת נתונים לטבלה
data = [
    (1, 'Avokado', 5),
    (2, 'Milk', 2),
    (3, 'Bread', 3),
    (4, 'Chocolate', 8),
    (5, 'Bamba', 5),
    (6, 'Orange', 10)
]
cursor.executemany('INSERT INTO shopping VALUES (?, ?, ?)', data)
print("data inserted into table.")

# שליפת כל הנתונים מהטבלה
cursor.execute("SELECT * FROM shopping")
rows = cursor.fetchall()
print("\nall info in table:")
for row in rows:
    print(dict(row))

# שליפת נתונים שבהם הכמות גדולה מ-5
cursor.execute("SELECT * FROM shopping WHERE amount > 5")
rows = cursor.fetchall()
print("\ndata where amount in bigger then 5:")
for row in rows:
    print(dict(row))

# מחיקת שורה מהטבלה
cursor.execute("DELETE FROM shopping WHERE name LIKE 'Orange'")
print("\nraw with the product 'Orange' deleted.")

# עדכון שם המוצר 'Bamba' ל-'Bisli'
cursor.execute("UPDATE shopping SET name = 'Bisli' WHERE name LIKE 'Bamba'")
print("producr name 'Bamba' changed to-'Bisli'.")

# עדכון כמות המוצר 'Milk' ל-1
cursor.execute("UPDATE shopping SET amount = 1 WHERE name LIKE 'Milk'")
print("amount of product 'Milk' updated to - 1.")

# ספירת מספר השורות בטבלה
cursor.execute("SELECT COUNT(*) FROM shopping")
count = cursor.fetchone()[0]
print(f"\nnumber of raws in table: {count}")

# שליפת כל הנתונים מהטבלה לאחר העדכונים
cursor.execute("SELECT * FROM shopping WHERE id > 0")
rows = cursor.fetchall()
print("\nall the data in the table after updates:")
for row in rows:
    print(dict(row))

# שמירת השינויים וסגירת החיבור
conn.commit()
conn.close()
print("\nconnection to db is closed.")



# ########## סיכום בשבילי
# הסבר הפתרון:
# בדיקת קיום ומחיקת הקובץ:
#
# os.path.exists(db_name) בודק אם הקובץ קיים.
# os.remove(db_name) מוחק את הקובץ אם הוא קיים.
# יצירת הטבלה והכנסת נתונים:
#
# נוצרה הטבלה shopping עם שלוש עמודות.
# הנתונים הוכנסו לטבלה באמצעות executemany.
# שליפת נתונים וביצוע שינויים:
#
# שימוש בפקודות SQL לשליפת נתונים, מחיקה ועדכון.
# ספירת שורות בטבלה:
#
# SELECT COUNT(*) סופרת את מספר השורות בטבלה.
# סגירת החיבור:
#
# החיבור נשמר ונסגר בסוף התוכנית.