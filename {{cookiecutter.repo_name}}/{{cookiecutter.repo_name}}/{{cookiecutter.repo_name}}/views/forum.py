from flask import Blueprint, render_template, redirect, url_for, flash
from ..forms import ForumPostForm
from ..models.forum_posts import ForumPost

forum_bp = Blueprint('forum', __name__, url_prefix='/forum')

@forum_bp.route('/')
def forum_index():
    """Generates the index page of the forum."""

    # TODO: Fix this non-working query. And add tests. :/
    posts = ForumPost.objects(published=True)[:25].order_by('-created_at')
    data = {}
    data['title'] = '{{cookiecutter.repo_name}} Forum'
    data['posts'] = posts
    data['breadcrumbs'] = ['Forum']
    return render_template('forum/index.html', data=data)

@forum_bp.route('/add-post/', methods=['GET', 'POST'])
def add_post():
    form = ForumPostForm()
    if form.validate_on_submit():
        post = ForumPost(title=form.title.data,
                    content=form.content.data,
                    published=True)
        post.save()
        submitted_data = (form.title.data, form.content.data)
        # TODO: pass in the type of alert to show: warning, default, etc.
        flash('Your post was saved!')
        # TODO: redirect to completed post, not the forum index
        return redirect('/forum/p/{}/'.format(post.id))

    data = {}
    data['title'] = 'Add New Forum Post'
    data['breadcrumbs'] = ['Forum', 'Add Post']
    return render_template('forum/add_post.html', form=form, data=data)

@forum_bp.route('/p/<post_id>/')
def post_detail(post_id):
    # will raise DoesNotExist if no document matches this id
    post = ForumPost.objects.get(id=post_id)
    data = {}
    data['title'] = post.title
    data['post'] = post
    data['breadcrumbs'] = ['Forum', data['title']]
    return render_template('forum/post_detail.html',data=data);
