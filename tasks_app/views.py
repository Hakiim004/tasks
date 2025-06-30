from django.shortcuts import redirect, render , get_object_or_404

from tasks_app.models import Task
from .forms import task_appForm
# Create your views here.
----------------------------------------------------------------------------------------------------------------------------------------------------
Si l'utilisateur soumet un formulaire (méthode POST), les données sont récupérées.

form.is_valid() : vérifie que les données sont valides.

form.save() : enregistre la nouvelle tâche dans la base de données.
----------------------------------------------------------------------------------------------------------------------------------------------------
def task_view(request):
    if request.method == 'POST':
        form = task_appForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = task_appForm()
    tasks = Task.objects.all().order_by('-created_at')
    context = {'form':form ,
               'tasks':tasks ,
    }
    return render(request, 'home.html' , context)
------------------------------------------------------------------------------------------------------------------------------------------------------
Cette fonction gère la modification d'une tâche existante.

request : la requête HTTP.

pk : la clé primaire de la tâche à modifier (chaque tâche a un identifiant unique dans la base de données).

Essaie de récupérer la tâche avec l’ID pk.

Si elle n’existe pas, retourne automatiquement une erreur 404 Not Found.



def update_task(request , pk):
    tasks = get_object_or_404(Task  , pk = pk  )
    form = task_appForm(request.POST or None , instance= tasks)

    Si c’est une requête POST : on prend les données envoyées.

    Si ce n’est pas une requête POST (donc GET), on envoie juste None, donc le formulaire affichera les données existantes de la tâche.

    instance=tasks signifie que le formulaire est lié à cette tâche précise.


    if form.is_valid():
        form.save()
Si les données envoyées dans le formulaire sont valides :

    on les enregistre dans la base de données.

    on redirige vers la page home (⚠️ problème ici, voir remarque ci-dessous).

    return     redirect('home')
    return render(request , 'update.html' ,{'form':form})

def delete_task(request , pk):
    tasks = get_object_or_404(Task , pk=pk)
    if request.method =='POST':
        tasks.delete()
        redirect('home')
    return render(request , "delete.html", {'tasks':tasks })


def toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('home')
