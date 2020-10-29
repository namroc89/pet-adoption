from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'plasticbeach1235'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def show_homepage():
    """Shows user homepage, with list of animals"""
    pets = Pet.query.all()

    return render_template('home.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Get:Shows form for adding pet
    Post: Adds pet to home page and database"""
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        photo_url = photo_url if photo_url else None
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url,
                      age=age, notes=notes, available=available)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)


@app.route("/pet/<int:id>")
def show_details(id):
    """show details for selected pet"""
    pet = Pet.query.get_or_404(id)

    return render_template('pet_details.html', pet=pet)


@app.route("/pet/<pet_id>/edit", methods=["GET", "POST"])
def show_edit_form(pet_id):
    """Get: shows edit form.
    Post: Edits pet"""
    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.photo_url = pet.photo_url if pet.photo_url else None
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect(f'/pet/{pet_id}')
    else:
        return render_template('edit_pet.html', form=form)


@app.route("/pet/<pet_id>/remove", methods=['POST'])
def remove_pet(pet_id):
    """removes pet"""
    Pet.query.filter_by(id=pet_id).delete()
    db.session.commit()
    return redirect("/")
