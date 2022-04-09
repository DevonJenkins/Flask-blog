from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import BlogPost
from myapp.blog_posts.forms import BlogPostForm

blog_posts = Blueprint('blog_posts', __name__)


# Add this to the bottom of __init__.py

# Linking and registering blog_posts views Blueprint
from myapp.blog_posts.views import blog_posts
app.register_blueprint(blog_posts)