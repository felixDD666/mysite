from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
#EMAILS
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Cliente, Cita, Categoria, Post


from django.utils import timezone


def principal(request):
    posts = Post.objects.order_by("-creation_date")
    numPost = Post.objects.count()-3;
    return render(request,'polls/principal.html',{
        "posts":posts,
        "numPost": numPost
        })

def formacionC(request):
    return render(request,'polls/formacionC.html',{})

def servicio1(request):
    return render(request,'polls/servicio1.html',{})

def servicio2(request):
    return render(request,'polls/servicio2.html',{})

def servicio3(request):
    return render(request,'polls/servicio3.html',{})

def servicio4(request):
    return render(request,'polls/servicio4.html',{})
 
def servicio5(request):
    return render(request,'polls/servicio5.html',{})
    
def servicio6(request):
    return render(request,'polls/servicio6.html',{})

def homePosts(request):
    posts = Post.objects.order_by("-creation_date")
    categories = Categoria.objects.order_by("-dateOfCreation")
    return render(request,'polls/homePosts.html',{
            "posts":posts,
            "categories":categories,
        },
    )

def one_post(request, idpost):
    posts = Post.objects.get(id=idpost)

    return render(request,'polls/post.html',{
            "post":posts,
        },
    )


def posts_by_category(request, idcategory):
    category = Category.objects.get(id=idcategory)
    posts = category.post_set.order_by("-creation_date")

    return render_to_response(
        "home.html",
        {
            "posts":posts,
        },
    )

def contacta(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            mensaje = form.cleaned_data['mensaje']
            try:
                send_mail("Nuevo mensaje de:" + nombre, "Email: " + email + "\ntelefono: " + telefono + "\nContenido: " + mensaje , "951753.durex@gmail.com", ['alvaro.delpino21@gmail.com '])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "polls/contacta.html", {'form': form})
def thanks(request):
    return HttpResponse('Thank you for your message.')


"""
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        """