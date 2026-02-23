from app import app
from database import User, db

app.config["TESTING"] = True
client = app.test_client()

with app.app_context():
    # Create a dummy user
    try:
        user = User(username='testuser', email='test@test.com', password='password')
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
    
    user_id = User.query.filter_by(username='testuser').first().id

    with client.session_transaction() as sess:
        sess['user_id'] = user_id

response = client.post('/profile/change-username', data={'username': 'newuser123'})
print("Status Code:", response.status_code)
if response.status_code == 500:
    print("500 ERROR CAUGHT!")
else:
    print("Headers:", response.headers)
    print("Redirect location:", response.location)
