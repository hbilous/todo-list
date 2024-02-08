from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm, TaskUpdate, TagUpdate
from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "todo/task-list.html"
    queryset = Task.objects.order_by("is_done", "-created_at")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task-form.html"
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskUpdate
    success_url = reverse_lazy("todo:task-list")

    def form_valid(self, form):
        self.object.is_done = not self.object.is_done
        self.object.save()
        return super().form_valid(form)


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")

    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_id')
        if task_id:
            task = Task.objects.get(id=task_id)
            if task.is_done:
                task.delete()
        return redirect('todo:task-list')


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "todo/tag-list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "todo/tag-form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagUpdate
    template_name = "todo/tag-update.form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")

    def post(self, request, *args, **kwargs):
        tag_id = request.POST.get('tag_id')
        if tag_id:
            tag = Tag.objects.get(id=tag_id)
            if tag:
                tag.delete()
        return redirect('todo:tag-list')
