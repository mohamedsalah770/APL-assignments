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
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    grade = Column(Float)
    def __repr__(self):
        return f"Student(id={self.id}, name='{self.name}', grade={self.grade})"
engine = create_engine("mysql+mysqlconnector://root:your_password@localhost/school")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
student1 = Student(name="Mohamed", grade=88.5)
student2 = Student(name="ziad", grade=91.2)
session.add_all([student1, student2])
session.commit()
students = session.query(Student).all()
for s in students:
    print(s)
