from django import forms
from django.shortcuts import redirect

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'deadline_datetime', 'is_done', 'tags']
        widgets = {
            'deadline_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        }


class TaskUpdate(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["is_done"]

    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_id')
        if task_id:
            task = Task.objects.get(id=task_id)
            task.is_done = not task.is_done
            task.save()
        return redirect('todo:task-list')


class TagUpdate(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
