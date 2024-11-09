from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import NameForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

def save_name(first_name, last_name):
    with open('names.txt', 'a') as file:
        file.write(f"{first_name} {last_name}")


def name_view(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            # Ma'lumotni faylga yozamiz
            save_name(first_name, last_name)

            # Yuborilgan ma'lumotni ko'rsatish
            return HttpResponse(f"Data saved: {first_name} {last_name}")
    else:
        form = NameForm()

    return render(request, 'home.html', {'form': form})