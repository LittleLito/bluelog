from flask import Blueprint, render_template

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
def index():
    return render_template('blog/index.html')
