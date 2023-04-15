from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, select
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin@localhost:5432/techucheba"
db = SQLAlchemy(app)


migrate = Migrate(app, db)
migrate.init_app(app, db)

class Employee(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255), nullable=False)
    middle_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255), nullable=False)

    role_id = db.Column(db.Integer, ForeignKey("role.role_id"))
    role = db.relationship('Role', 
                           backref = db.backref('roles', 
                                                lazy='dynamic'))
    
    position_id = db.Column(db.Integer, ForeignKey("position.position_id"))
    position = db.relationship('Position',
                               backref = db.backref('position',
                                                    lazy = 'dynamic'))

    def __init__(self, first_name, middle_name, last_name, role, position):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.role = role
        self.position = position
    
class Role(db.Model):
    role_id = db.Column(db.Integer, primary_key = True)
    role_name = db.Column(db.String(50), nullable = False)
    
    def __init__(self, role_name):
        self.role_name = role_name

class Position(db.Model):
    position_id = db.Column(db.Integer, primary_key = True)
    position_name = db.Column(db.String(255), nullable = False)
    
    def __init__(self, position_name):
        self.position_name = position_name

class Courses(db.Model):
    course_id = db.Column(db.Integer, primary_key = True)
    course_name = db.Column(db.Text, nullable = False)

    def __init__(self, course_name):
        self.course_name = course_name
    
course_lisenters = db.Table('course_lisenters',
                            db.Column('lisenter_id', db.Integer, db.ForeignKey('employee.user_id')),
                            db.Column('course_id', db.Integer, db.ForeignKey('courses.course_id')),
                            db.Column('is_done', db.Boolean))


@app.route('/')
def home():
    userList = db.session.query(Employee.first_name, Employee.last_name, Position.position_name).join(Position).all()
    print(userList)
    return render_template('index.html', user = userList)

if __name__ == '__main__':
    with app.app_context():
       db.create_all()
    app.run(debug=True)

    



    



    

