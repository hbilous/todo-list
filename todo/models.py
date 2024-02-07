from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    DONE_CHOICES = [(True, "Yes"), (False, "No"),]
    content = models.TextField(max_length=500)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline_datetime = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(choices=DONE_CHOICES, default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        return (f"{self.tags} (content: {self.content}, "
                f"deadline: {self.deadline_datetime}). Is done: {self.is_done}")
