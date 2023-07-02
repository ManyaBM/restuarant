from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///restaurant.db"
db = SQLAlchemy(app)

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    country = db.Column(db.String(64))
    type = db.Column(db.String(64))
    price = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.name}, {self.country}, {self.type}"

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit',methods=['POST'])
def submit():
    name = request.form['name']
    country = request.form['country']
    type = request.form['type']
    price = request.form['price']
    flag = request.form['flag']
    new_food = Food(name=name,country=country,type=type,price=price)
    try:
        db.session.add(new_food) 
        db.session.commit()
        return render_template('confirmation.html',flag=flag)
    except Exception as e:
        return str(e)
    
@app.route('/foods')
def foods():
    foods = Food.query.all()
    return render_template('foods.html', foods=foods)

@app.route('/delete-food/<int:food_id>')
def delete_food(food_id):
    food = Food.query.get(food_id)
    try:
        db.session.delete(food)
        db.session.commit()
        return render_template('confirmation.html',flag="D")
    except Exception as e:
        return str(e)
    
@app.route('/update-foods/<int:food_id>', methods=['GET', 'POST'])
def update_food(food_id):
    food = Food.query.get(food_id)
    if request.method == 'POST':
        # Update food details
        try:
            food.name = request.form['name']
            food.country = request.form['country']
            food.type = request.form['type']
            food.price = request.form['price']
            db.session.commit()
            return render_template('confirmation.html',flag="U")
        except Exception as e:
            return str(e)
    else:
        # Display update form
        return render_template('update_food.html', food=food)


if __name__=='__main__':
    app.run(debug=True,port=10000)