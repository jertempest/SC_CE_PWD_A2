from django.contrib.auth import get_user_model
from django.db.models import Sum, Q, Count

from mtg_blog_app.models import Comment, Post

User = get_user_model()


def question_1_return_active_users():
    """
    Return the results of a query which returns a list of all
    active users in the database.
    """
    return User.objects.filter(is_active=True)


def question_2_return_regular_users():
    """
    Return the results of a query which returns a list of users that
    are *not* staff and *not* superusers
    """
    return User.objects.filter(is_staff=False,is_superuser=False)

def question_3_return_all_posts_for_user(user):
    """
    Return all the Posts authored by the user provided. Posts should
    be returned in reverse chronological order from when they
    were created.
    """
    return Post.objects.filter(author=user).order_by('-created')

def question_4_return_all_posts_ordered_by_title():
    """
    Return all Post objects, ordered by their title.
    """
    return Post.objects.all().order_by('title')


def question_5_return_all_post_comments(post):
    """
    Return all the comments made for the post provided in order
    of last created.
    """
    return Comment.objects.filter(post=post).order_by('-created')

def question_6_return_the_post_with_the_most_comments():
    """
    Return the Post object containing the most comments in
    the database. Do not concern yourself with approval status;
    return the object which has generated the most activity.
    """
    return Post.objects.annotate(num_comments=Count('comments')).order_by('-num_comments').first()

def question_7_create_a_comment(post):
    """
    Create and return a comment for the post object provided.
    """
    comment = Comment.objects.create(
        post = post,
        name = 'You\'re wrong!',
        email = 'trolling_u@exampl.com',
        text = 'You have this so backwards, that it isn\'t even close',
        approved = True
    )
    
    return comment

def question_8_set_approved_to_false(comment):
    """
    Update the comment record provided and set approved=False
    """
    comment.approved = False
    comment.save()
    return comment


def question_9_delete_post_and_all_related_comments(post):
    """
    Delete the post object provided, and all related comments.
    """
    post.delete()

def ask_all():
    user = User.objects.first()
    post = Post.objects.first()
    comment = Comment.objects.first()

    q1 = question_1_return_active_users()
    q2 = question_2_return_regular_users()

    print(f'Q1 - Active users: {q1}')
    print(f'Q2 - Regular users: {q2}')

    if user:
        q3 = question_3_return_all_posts_for_user(user)
        print(f'Q3 - All posts for user: {q3}')
    else:
        print('Q3 - No users found to get posts for')

    if post:
        q4 = question_4_return_all_posts_ordered_by_title()
        q5 = question_5_return_all_post_comments(post)
        q6 = question_6_return_the_post_with_the_most_comments()
        q7 = question_7_create_a_comment(post)
        print(f'Q4 - All posts ordered by title: {q4}')
        print(f'Q5 - All comments for post: {q5}')
        print(f'Q6 - Post with the most comments: {q6}')
        print(f'Q7 - Create comment: {q7}')
    else:
        print('No posts found')

    if comment:
        q8 = question_8_set_approved_to_false(comment)
        print(f"Q8 - Updated comment: {q8}")
    else:
        print('No comment found')

    if post is not None:
        question_9_delete_post_and_all_related_comments(post)
        print(f'Q9 - Deleted post "{post.title}" and related comments.')
    else:
        print('No posts to delete.')
