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

@blog_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
  form = BlogPostForm()
  if form.validate_on_submit():
    blog_post = BlogPost(title=form.title.data, text=form.text.data, user_id=current_user.id)
    db.session.add(blog_post)
    db.session.commit()
    flash('Blog post created')
    print('Blog post was created')
    return redirect(url_for('core.index'))
  return render_template('create_post.html', form=form)