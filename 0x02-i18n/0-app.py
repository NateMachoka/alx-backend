#!/usr/bin/env python3
"""
Basic Flask app setup for a single route that renders a simple HTML page.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Route to render the index page.
    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
