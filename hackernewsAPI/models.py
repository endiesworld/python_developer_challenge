from turtle import title
from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
"""
id	The item's unique id.
deleted	true if the item is deleted.
type	The type of item. One of "job", "story", "comment", "poll", or "pollopt".
by	The username of the item's author.
time	Creation date of the item, in Unix Time.
text	The comment, story or poll text. HTML.
dead	true if the item is dead.
parent	The comment's parent: either another comment or the relevant story.
poll	The pollopt's associated poll.
kids	The ids of the item's comments, in ranked display order.
url	The URL of the story.
score	The story's score, or the votes for a pollopt.
title	The title of the story, poll or job. HTML.
parts	A list of related pollopts, in display order.
descendants
"""


class News(models.Model):
    id = models.PositiveIntegerField()
    deleted = models.BooleanField()
    type = models.CharField(max_length=20)
    by = models.CharField()
    time = models.DateTimeField()
    text = models.TextField()
    dead = models.BooleanField()
    parent = models.PositiveIntegerField()
    poll = models.PositiveIntegerField()
    kids = ArrayField()
    url = models.URLField()
    score = models.PositiveIntegerField()
    title = models.TextField()
    parts = ArrayField()
    descendants = models.PositiveIntegerField()

    def return_dict(self):
        types = {
            "story": {
                "by": self.by,
                "descendants": self.descendants,
                "id": self.id,
                "kids": self.kids,
                "score": self.score,
                "time": self.time,
                "title": self.title,
                "type": self.type,
                "url": self.url,
            },
            'comments': {
                "by": self.by,
                "id": self.id,
                "kids": self.kids,
                "parent": self.parent,
                "text": self.text,
                "time": self.time,
                "type": self.type
            },
            "job": {
                "by": self.by,
                "id": self.id,
                "score": self.score,
                "text": self.text,
                "time": self.time,
                "title": self.title,
                "type": self.type,
                "url": self.url
            },
            "poll": {
                "by": self.by,
                "descendants": self.descendants,
                "id": self.id,
                "kids": self.kids,
                "parts": self.parts,
                "score": self.score,
                "text": self.text,
                "time": self.time,
                "title": self.title,
                "type": self.type
            },
            "pollopt": {
                "by": self.by,
                "id": self.id,
                "poll": self.poll,
                "score": self.score,
                "text": self.text,
                "time": self.time,
                "type": self.type
            }
        }

        return types

    def __str__(self):
        # return self.return_dict()[self.type]
        return 'The object id: {}, and type is: {}'.format(self.return_dict()[self.type]['id'], self.return_dict()[self.type]['type'])
