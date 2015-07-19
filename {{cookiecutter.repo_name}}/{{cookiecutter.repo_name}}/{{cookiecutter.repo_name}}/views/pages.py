from flask import Blueprint, render_template, redirect, url_for, flash
from ..models.pages import Page

pages_bp = Blueprint('pages', __name__)

@pages_bp.route('/')
def index():
    """Generates the index page of the application."""

    data = {}
    data['title'] = '{{cookiecutter.repo_name}}'
    data['leader_text'] = '''Elit recusandae modi vitae voluptatum nam praesentium, placeat blanditiis est aperiam eligendi ea odio deserunt! Veritatis placeat nesciunt voluptate natus cum, consequatur praesentium praesentium est maxime earum dolorem? Excepturi laborum.'''
    return render_template('pages/index.html', data=data)


@pages_bp.route('/about/')
def about():
    """Generates the about page."""
    data = {}
    data['title'] = 'About {{cookiecutter.repo_name}}'
    return render_template('pages/about.html', data=data)

