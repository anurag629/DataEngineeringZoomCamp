from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Chinook.sqlite'
db = SQLAlchemy(app)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form.get('content')
        new_entry = Entry(content=content)
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for('index'))
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
