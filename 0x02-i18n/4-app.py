#!/usr/bin/env python3
"""
Flask app with i18n support using Babel.
Allows users to switch between English and French languages.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Configuration class for Babel settings in Flask.
    Attributes:
        LANGUAGES (list): List of supported languages for localization.
        BABEL_DEFAULT_LOCALE (str): Default locale for the app.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for the app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best locale based on the 'locale' query parameter
    or the user's accepted languages.
    Returns:
        str: The locale to use for this request.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Renders the index page with localized content.
    Returns:
        str: Rendered HTML of the index page.
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
