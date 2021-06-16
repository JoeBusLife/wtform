from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import PetFormNew, PetFormEdit
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "soup"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def home():
    """ Show all pets, most recent first """
    pets = Pet.query.order_by(desc('id')).all()
    return render_template('home.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def new_pet_form():
    """ render form to add new pet. Also recieves submitted form and adds to database if vaild """
    form = PetFormNew()
    if form.validate_on_submit():
        form_data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**form_data)
        
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('pet_new.html', form=form)
    
    
@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_pet_with_edit_form(pet_id):
    """ render form to edit a pet. Also recieves submitted form and edits pet in database if vaild """
    pet = Pet.query.get_or_404(pet_id)
    form = PetFormEdit(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        
        db.session.commit()
        return redirect('/')
    else:
        return render_template('pet.html', pet=pet, form=form)