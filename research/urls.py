from django.urls import path, include
from django.views.generic import TemplateView

import research.views
urlpatterns = [
    #path('', TemplateView.as_view(template_name='upload/base_upload.html'), name='upload_research'),
    path('', research.views.upload_to_dashboard_research_list, name='upload_research'),
    path('researchs/', research.views.research_list, name='research_list'),
    path('researchs/upload/', research.views.upload_research, name='upload'),
    path('researchs/<int:pk>/', research.views.delete_research, name='delete_research'),
    path('class/researchs/', research.views.ResearchListView.as_view(), name='class_research_list'),
    path('class/researchs/upload/', research.views.UploadResearchView.as_view(), name='class_upload_research'),
]
