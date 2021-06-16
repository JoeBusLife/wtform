"""Seed file to make sample data for pets db."""

from models import db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

pet1 = Pet(name="Hogart", species="porcupine", photo_url="https://static.toiimg.com/photo/imgsize-577122,msid-79709875/79709875.jpg", age=13, available=True)
pet2 = Pet(name="Red-Orange", species="cat", photo_url="https://cdn.shopify.com/s/files/1/0925/5048/products/funny-cat-red-orange-wig-510520_1024x1024.jpg?v=1573933202", age=12, available=True)
pet3 = Pet(name="Doge", species="dog", photo_url="https://nypost.com/wp-content/uploads/sites/2/2021/06/doge-2.jpg?quality=80&strip=all&w=618&h=410&crop=1", age=11, available=True)
        
db.session.add_all([pet1,pet2,pet3])
db.session.commit()