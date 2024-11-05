#!/usr/bin/env python3
"""
Flask app setup with Babel for language localization
and template parameterization.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _

app = Flask(__name__)


class Config:
    """
    Config class to store configuration variables for Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for supported languages based on client request.
    Returns:
        str: Best matching language.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Route to render the index page.
    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
