import io
from app import app
from database import User, db

app.config["TESTING"] = True
client = app.test_client()

with app.app_context():
    # Ensure test user exists
    user = User.query.filter_by(username='testuser').first()
    if not user:
        user = User(username='testuser', email='test@test.com', password='password')
        db.session.add(user)
        db.session.commit()
    
    user_id = user.id

with client.session_transaction() as sess:
    sess['user_id'] = user_id

data = {
    'file': (io.BytesIO(b"abcdef"), 'test.jpg')
}

print("Testing /profile/change-avatar...")
try:
    response = client.post('/profile/change-avatar', data=data, content_type='multipart/form-data')
    print("Status Code:", response.status_code)
except Exception as e:
    import traceback
    traceback.print_exc()

