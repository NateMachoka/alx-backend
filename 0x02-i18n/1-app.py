#!/usr/bin/env python3
"""
Basic Flask app setup with Babel for language localization.
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
    Config class to store configuration variables for Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)  # Instantiate Babel and attach it to the app


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Route to render the index page.
    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
