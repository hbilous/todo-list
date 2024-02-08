from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline_datetime = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        tags_str = ", ".join(tag.name for tag in self.tags.all())
        status = "Done" if self.is_done else "Not done"
        return (f"{tags_str} (content: {self.content}, "
                f"deadline: {self.deadline_datetime}). Is done: {status}")
