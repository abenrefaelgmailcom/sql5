# sql5
combination with python


הסבר הפתרון:
בדיקת קיום ומחיקת הקובץ:

os.path.exists(db_name) בודק אם הקובץ קיים.
os.remove(db_name) מוחק את הקובץ אם הוא קיים.
יצירת הטבלה והכנסת נתונים:

נוצרה הטבלה shopping עם שלוש עמודות.
הנתונים הוכנסו לטבלה באמצעות executemany.
שליפת נתונים וביצוע שינויים:

שימוש בפקודות SQL לשליפת נתונים, מחיקה ועדכון.
ספירת שורות בטבלה:

SELECT COUNT(*) סופרת את מספר השורות בטבלה.
סגירת החיבור:

החיבור נשמר ונסגר בסוף התוכנית
