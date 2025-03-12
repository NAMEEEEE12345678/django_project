from django.shortcuts import render, get_object_or_404, redirect
from .forms import VacancyForm
from .models import Category, Job, Vacancy

# Список ваканский
def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancy_list.html',{
        'vacancies' : vacancies
    })

# Просмотр конкретной вакансии 
def vacancyes_detail(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    return render(request, 'vacancy_detail.html', {
        'vacancy': vacancy
    })

# Добавление вакансии 
def vacancy_create(request):
    if request.method == "POST":
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacancy_list')
    else:
        form = VacancyForm()
    return render(request, 'vacancy_form.html', {
        'form':form
    })

# Редактирование вакансии 
def vacancy_update(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    if request.method == "POST":
        form = VacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            return redirect('vacancy_detail', pk=vacancy.pk)
    else:
        form = VacancyForm(instance=vacancy)
    return render(request, 'vacancy_form.html', {
        'form' :form
    })

# Удаление вакансии 
def vacancy_delete(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    if request.method == "POST":
        vacancy.delete()
        return redirect('vacancy_list')
    return render(request, 'vacancy_confirm_delete.html',{
        'vacancy':vacancy
    })

def home_page(request):
    categories = Category.objects.all()
    jobs = Job.objects.all()

    context = {
        'categories': categories,
        'jobs': jobs
    }
    return render(request, "home.html", context )

def about_page(request):
    return render(request, "about.html")

def contact_page(request):
    return render(request, "contact.html")