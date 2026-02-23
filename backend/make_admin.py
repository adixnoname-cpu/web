import sys
from app import app
from database import db, User

if len(sys.argv) < 2:
    print("Usage: python make_admin.py <username>")
    sys.exit(1)

target_username = sys.argv[1]

with app.app_context():
    user = User.query.filter_by(username=target_username).first()
    if not user:
        print(f"Error: User '{target_username}' not found.")
        sys.exit(1)
    
    user.admin = True
    db.session.commit()
    print(f"Success! User '{target_username}' is now an Admin.")
