from flask import Flask
from flask_frozen import Freezer
from app import app

# Configure the app for static file generation
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

# Create the freezer
freezer = Freezer(app)

if __name__ == '__main__':
    # Freeze the app
    freezer.freeze() 