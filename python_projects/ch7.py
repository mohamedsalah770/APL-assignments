import pymysql
connect = pymysql.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="school")
cur = connect.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    grade FLOAT
)""")
students = [("Ali", 85.5),("Sara", 92.0),("Mohamed", 78.3)]
cur.executemany("INSERT INTO students (name, grade) VALUES (%s, %s)", students)
connect.commit()
cur.execute("SELECT * FROM students")
rows = cur.fetchall()
for row in rows:
    print(row)
connect.close()
import pymysql
connect = pymysql.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="school"
)
curson = connect.cursor()
name = input("Enter name: ")
grade = float(input("Enter grade: "))
curson.execute("INSERT INTO students (name, grade) VALUES (%s, %s)",(name, grade))
connect.commit()
curson.execute("SELECT * FROM students")
for row in curson.fetchall():
    print(row)
curson.close()
connect.close()
import pymysql
connect = pymysql.connectect(
    host="localhost",
    user="root",
    password="your_password",
    database="school")
curson = connect.cursonsor()
try:
    connect.start_transaction()
    curson.execute("INSERT INTO students (name, grade) VALUES (%s, %s)",("Omar", 90))
    curson.execute("INSERT INTO students (name, grade) VALUES (%s, %s)",("Laila", 95))
    connect.commit()
except Exception as e:
    print("Error:", e)
    connect.rollback()
    print("Transaction rolled back!")
curson.execute("SELECT * FROM students")
for row in curson.fetchall():
    print(row)
curson.close()
connect.close()
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
Base = declarative_base()
class Book(Base):
    tablename = "Books"
    id = Column(Integer, primary_key=True)
    title = Column(String(300))
    author = Column(String(300))
    def repr(self):
        return f"Book (id={self.id}, title='{self.title}', and author={self.author})"
engine = create_engine("mysql+mysqlconnector://root:your_password@localhost/school")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
book1 = Book(title="Python basics", author='Guido')
book2 = Book(title="AI with python", author='Mohamed')
session.add_all([book1, book2])
session.commit()
books = session.query(Book).all()
for b in books:
    print(b)

