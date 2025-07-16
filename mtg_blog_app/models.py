from django.conf import settings
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=50, unique=True)

    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Post(models.Model):
    """
    Represents a blog post
    """

    DRAFT = "draft"
    PUBLISHED = "published"
    STATUS_CHOICES = [(DRAFT, "Draft"), (PUBLISHED, "Published")]

    title = models.CharField(max_length=255)

    slug = models.SlugField(
        null=False,
        unique_for_date="published",
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="blog_posts",
        null=False,
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "published" to make this post publicly visible',
        blank=True,
    )

    content = models.TextField(blank=True)
    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text="The date and time this article was published",
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    topics = models.ManyToManyField(Topic, related_name="blog_posts")

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments", null=False, blank=False
    )
    name = models.CharField(max_length=80,)
    email = models.EmailField()
    text = models.TextField()
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return f"Comment by {self.name} on {self.post}"
