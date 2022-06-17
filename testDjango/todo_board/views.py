from django.shortcuts import render
from .models import TodoList
from .forms import TodoForm
from django.shortcuts import get_object_or_404
from django.views import generic

#class Todo_main(generic.TemplateView):
    #def get(self, request, *args, **kwargs):
    #    template_name = 'todo_board/todo_board_list.html'
    #    return render(request, template_name)

def todo_board_list(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_sesion': login_session }
    

    #context = {'todo_list': TodoList.objects.all()}
    #todo_list = {'todo_list': TodoList.objects.all()}
    #tudo_list = get_object_or_404(TodoList)

    #todo_list = get_object_or_404(TodoList.objects.filter(title=True))
    #context = {'todo_list': todo_list}
    #context['todo_list'] = todo_list
    todo_list = TodoList.objects.all()
    context = {'todo_list' : todo_list}

    return render(request, 'todo_board/todo_board_list.html', context)

def check_post(request):
    template_name = 'todo_board/todo_board_success.html'
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_save()
            message = '일정을 추가하였습니다.'
            return render(request, template_name, {"message": message})
    else:
        template_name = 'todo_board/todo_board_insert.html'
        form = TodoForm
        return render(request, template_name, {"form":form})


def todo_board_detail(request, pk):
    login_session = request.session.get('login_session', '')
    context = { 'login_session': login_session}

    todo_board = get_object_or_404(TodoList, no=pk)
    context['todo_board'] = todo_board
    
    response = render(request, 'todo_board/todo_board_detail.html', context)
    
    return response



