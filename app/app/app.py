import os
from flask import Flask, redirect, url_for, request, render_template
import psycopg2

from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
POSTGRES = {
    'user': 'docker',
    'pw': 'super_strong_password',
    'db': 'psko_app',
    'host': 'db',
    'port': '5432',
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
print(app.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(app)

db.init_app(app)


# Create our database model
class Todo(db.Model):
    __tablename__ = "todo"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    description = db.Column(db.String(255))

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '{}: {}'.format(self.name, self.description)


@app.route('/')
def todo():
    _items = Todo.query.all()
    items = [item for item in _items]

    return render_template('index.html', items=items)


@app.route('/new', methods=['POST'])
def new():

    todo = Todo(name=request.form['name'],description=request.form['description'])
    db.session.add(todo)
    db.session.commit()
    #Todo.add(todo)

    return redirect(url_for('todo'))

@app.route('/test', methods=['GET'])
def test():
    conn_string = "host="+ creds.PGHOST +" port="+ "5432" +" dbname="+ creds.PGDATABASE +" user=" + creds.PGUSER +" password="+ creds.PGPASSWORD
    conn=psycopg2.connect(conn_string)
    print("Connected!")

    sql_command = "SELECT * FROM todo;"
    print (sql_command)

    # Load the data
    data = pd.read_sql(sql_command, conn)

    print(data.shape)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
