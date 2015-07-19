from mixer.backend.mongoengine import mixer
from ..models.post import Post


def generate_posts(n):
    """Generates dummy posts for development server.
    
    Import this function into the Python shell and then pass in the number
    of posts to generate.

    Example that adds five new posts to the database:
    from {{cookiecutter.repo_name}}.fixtures.posts import generate_posts
    generate_posts(5)
    """
    for _ in range(n):
        post = mixer.blend(Post)

    print('Generated {} posts.'.format(n))
