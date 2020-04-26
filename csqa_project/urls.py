from django.contrib import admin
from django.urls import path, include
from main.views import homeFeedView, testView
from pages.views import aboutPageView
from questions.views import (questionView, newView, answerView,
                            myQuestionsView, myAnswersView, questionVoteView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeFeedView),
    path('test/', testView),
    path('about/', aboutPageView),
    path('accounts/', include('allauth.urls')),
    path('question/<int:id>/', questionView),
    path('question/<int:id>/vote', questionVoteView),
    path('question/<int:id>/answer', answerView),
    path('question/new/', newView),
    path('question/my_answers/', myAnswersView, name='my-answers'),
    path('question/my_questions/', myQuestionsView, name='my-questions'),
]
