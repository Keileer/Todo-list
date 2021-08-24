from django.shortcuts import render, redirect
from .models import TodoList
from .forms import TodoListForm


def main(request):
    all_todo = TodoList.objects.all()
    all_date = TodoList.objects.filter(deadline__year="2021").order_by("deadline").values_list("deadline",
                                                                                               flat=True).distinct()
    form = TodoListForm(initial={"description": ""})
    if request.method == "POST":
        form = TodoListForm(request.POST)
        form.save()
        return redirect("main-page")
    return render(request, 'main.html', locals())


def remove_todo(request, pk):
    TodoList.objects.get(id=pk).delete()
    return redirect("main-page")
