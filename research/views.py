from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import ResearchForm
from .models import Research


class Home(TemplateView):
    template_name = 'upload/home_upload.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload/upload.html', context)


def research_list(request):
    researchs = Research.objects.all()
    return render(request, 'upload/research_list.html', {
        'researchs': researchs
    })


def upload_research(request):
    researchs = Research.objects.all()
    if request.method == 'POST':
        form = ResearchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('research_list')
    else:
        form = ResearchForm()
    return render(request, 'upload/upload_research.html', {
        'form': form, 'researchs': researchs
    })


def delete_research(request, pk):
    if request.method == 'POST':
        research = Research.objects.get(pk=pk)
        research.delete()
    return redirect('research_list')


class ResearchListView(ListView):
    model = Research
    template_name = 'upload/class_research_list.html'
    context_object_name = 'researchs'


class UploadResearchView(CreateView):
    model = Research
    form_class = ResearchForm
    success_url = reverse_lazy('class_research_list')
    template_name = 'upload/upload_research.html'


def upload_to_dashboard_research_list(request):
    researchs = Research.objects.all()
    return render(request, 'upload/base_upload.html', {
        'researchs': researchs
    })

def upload_to_home_research_list(request):
    researchs = Research.objects.all()
    return render(request, 'dashboard/home.html', {
        'researchs': researchs
    })