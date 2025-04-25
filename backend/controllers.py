from flask import Blueprint, request, jsonify, current_app, send_from_directory
from werkzeug.utils import secure_filename
from models import db, Amplifier, User, Speaker
from werkzeug.security import check_password_hash
from sqlalchemy.exc import SQLAlchemyError
from functools import wraps
import datetime
import jwt
import os

main_routes = Blueprint('main_routes', __name__)

# ================= AUTH DECORATORS =================

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split(" ")[1]
            except IndexError:
                return jsonify({'error': 'Token format invalid'}), 401

        if not token:
            return jsonify({'error': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.get(data['user_id'])
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401

        return f(current_user, *args, **kwargs)
    return decorated

def admin_required(f):
    @token_required
    @wraps(f)
    def decorated(current_user, *args, **kwargs):
        if not current_user.is_admin:
            return jsonify({'error': 'Admin access required'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

# ========== AMPLIFIER ROUTES ==========

@main_routes.route('/api/amplifiers', methods=['GET'])
def get_amplifiers():
    amplifiers = Amplifier.query.order_by(Amplifier.date_added.desc()).all()
    return jsonify([amp.to_dict() for amp in amplifiers])

@main_routes.route('/api/amplifiers/<int:amp_id>', methods=['GET'])
def get_amplifier(amp_id):
    amp = Amplifier.query.get_or_404(amp_id)
    return jsonify(amp.to_dict())

@main_routes.route('/api/amplifiers', methods=['POST'])
@admin_required
def create_amplifier(current_user):
    data = request.form
    image = request.files.get('image')
    filename = None

    if image:
        filename = secure_filename(image.filename)
        image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    amp = Amplifier(**data, image_filename=filename)
    db.session.add(amp)
    db.session.commit()
    return jsonify(amp.to_dict()), 201

@main_routes.route('/api/amplifiers/<int:amp_id>', methods=['PUT'])
@admin_required
def update_amplifier(current_user, amp_id):
    amp = Amplifier.query.get_or_404(amp_id)
    data = request.form
    image = request.files.get('image')

    if image:
        filename = secure_filename(image.filename)
        image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        amp.image_filename = filename

    for field in data:
        setattr(amp, field, data[field])
    
    db.session.commit()
    return jsonify(amp.to_dict())

@main_routes.route('/api/amplifiers/<int:amp_id>', methods=['DELETE'])
@admin_required
def delete_amplifier(current_user, amp_id):
    amp = Amplifier.query.get_or_404(amp_id)
    db.session.delete(amp)
    db.session.commit()
    return jsonify({'message': 'Amplifier deleted'})

# ========== SPEAKER ROUTES ==========

@main_routes.route('/api/speakers', methods=['GET'])
def get_speakers():
    speakers = Speaker.query.order_by(Speaker.date_added.desc()).all()
    return jsonify([speaker.to_dict() for speaker in speakers])

@main_routes.route('/api/speakers/<int:speaker_id>', methods=['GET'])
def get_speaker(speaker_id):
    speaker = Speaker.query.get_or_404(speaker_id)
    return jsonify(speaker.to_dict())

@main_routes.route('/api/speakers', methods=['POST'])
@admin_required
def create_speaker(current_user):
    data = request.form
    image = request.files.get('image')
    filename = None

    if image:
        filename = secure_filename(image.filename)
        image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    speaker = Speaker(**data, image_filename=filename)
    db.session.add(speaker)
    db.session.commit()
    return jsonify(speaker.to_dict()), 201

@main_routes.route('/api/speakers/<int:speaker_id>', methods=['PUT'])
@admin_required
def update_speaker(current_user, speaker_id):
    speaker = Speaker.query.get_or_404(speaker_id)
    data = request.form
    image = request.files.get('image')

    if image:
        filename = secure_filename(image.filename)
        image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        speaker.image_filename = filename

    for field in data:
        setattr(speaker, field, data[field])

    db.session.commit()
    return jsonify(speaker.to_dict())

@main_routes.route('/api/speakers/<int:speaker_id>', methods=['DELETE'])
@admin_required
def delete_speaker(current_user, speaker_id):
    speaker = Speaker.query.get_or_404(speaker_id)
    db.session.delete(speaker)
    db.session.commit()
    return jsonify({'message': 'Speaker deleted'})

# ========== AUTH ROUTES ==========

@main_routes.route('/api/register', methods=['POST'])
def register():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({'error': 'Name, email and password required'}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already registered'}), 400

    user = User(name=name, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'})

@main_routes.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password required'}), 400

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, current_app.config['SECRET_KEY'], algorithm='HS256')

        return jsonify({
            'message': 'Login successful',
            'token': token,
            'user': {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'is_admin': user.is_admin
            }
        })

    return jsonify({'error': 'Invalid credentials'}), 401

# ========== STATIC FILE ROUTE ==========

@main_routes.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)
