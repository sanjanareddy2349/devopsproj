from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Validation
    if not email or not password:
        return "<script>alert('All fields are required.');window.history.back();</script>"
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "<script>alert('Enter a valid email address.');window.history.back();</script>"
    if len(password) < 6:
        return "<script>alert('Password must be at least 6 characters long.');window.history.back();</script>"

    return redirect(url_for('home'))

@app.route('/home')
def home():
    pins = [
        {"id": 1, "title": "Aesthetic Workspace", "image": "static/images/pin1.jpg"},
        {"id": 2, "title": "Cozy Bedroom", "image": "static/images/pin2.jpg"},
        {"id": 3, "title": "Travel Goals", "image": "static/images/pin3.jpg"},
        {"id": 4, "title": "Art Inspiration", "image": "static/images/pin4.jpg"},
        {"id": 5, "title": "Sunset Glow", "image": "static/images/pin5.jpg"},
        {"id": 6, "title": "Beach Vibes", "image": "static/images/pin6.jpg"},
        {"id": 7, "title": "Plant Decor", "image": "static/images/pin7.jpg"},
        {"id": 8, "title": "Café Aesthetic", "image": "static/images/pin8.jpg"},
        {"id": 9, "title": "Book Nook", "image": "static/images/pin9.jpg"},
        {"id": 10, "title": "Boho Decor", "image": "static/images/pin10.jpg"},
        {"id": 11, "title": "City Nights", "image": "static/images/pin11.jpg"},
        {"id": 12, "title": "Vintage Finds", "image": "static/images/pin12.jpg"}
    ]
    return render_template("home.html", pins=pins)

@app.route('/pin/<int:pin_id>')
def pin_detail(pin_id):
    pins = {
        1: {"title": "Aesthetic Workspace", "desc": "Minimal desk setup with warm lighting and red accents.", "image": "static/images/pin1.jpg"},
        2: {"title": "Cozy Bedroom", "desc": "Soft tones and modern decor for comfort and peace.", "image": "static/images/pin2.jpg"},
        3: {"title": "Travel Goals", "desc": "Wanderlust dreams captured in a single frame.", "image": "static/images/pin3.jpg"},
        4: {"title": "Art Inspiration", "desc": "Creative wall collage ideas with Pinterest-style vibes.", "image": "static/images/pin4.jpg"},
        5: {"title": "Sunset Glow", "desc": "Golden skies and peaceful evenings.", "image": "static/images/pin5.jpg"},
        6: {"title": "Beach Vibes", "desc": "Feel the ocean breeze and soft sand.", "image": "static/images/pin6.jpg"},
        7: {"title": "Plant Decor", "desc": "Greenery that brightens up your room.", "image": "static/images/pin7.jpg"},
        8: {"title": "Café Aesthetic", "desc": "Perfect corner for a latte and book.", "image": "static/images/pin8.jpg"},
        9: {"title": "Book Nook", "desc": "A cozy corner filled with stories.", "image": "static/images/pin9.jpg"},
        10: {"title": "Boho Decor", "desc": "Earthy tones and natural textures.", "image": "static/images/pin10.jpg"},
        11: {"title": "City Nights", "desc": "Neon lights and urban magic.", "image": "static/images/pin11.jpg"},
        12: {"title": "Vintage Finds", "desc": "Retro treasures that never fade.", "image": "static/images/pin12.jpg"},
    }
    pin = pins.get(pin_id)
    return render_template("pin.html", pin=pin)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
