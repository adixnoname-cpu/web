from config import app
import os

print("App Root Path:", app.root_path)
print("Static Folder:", app.static_folder)
print("Uploads config:", app.config['UPLOADS_FOLDER'])

uploads_dir = os.path.join(app.root_path, app.config['UPLOADS_FOLDER'])
print("Calculated uploads_dir (what utils.py uses):", uploads_dir)

# Correct way
correct_dir = os.path.join(app.static_folder, 'uploads')
print("Correct static folder uploads:", correct_dir)
