from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from gtib.models import PageSettings, NewsTypeModel, NewsModel, FAQsModel, FormmModel, FormmChoices, OfferQuestionModel, EventModel, VolunteersModel

class IndexView(View):
    pagesettings = PageSettings.objects.first()
    firstnews = NewsModel.objects.first()
    allnews = NewsModel.objects.all()[1:7]
    quiz = FormmModel.objects.filter(is_highlighted=True)
    formmchoices = FormmModel.objects.filter(quiz=quiz)
    faqs = FAQsModel.objects.all()
    events = EventModel.objects.all()


    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
            "firstnews": self.firstnews,
            "allnews": self.allnews,
            "quiz": self.quiz,
            "formmchoices": self.formmchoices,
            "faqs": self.faqs,
            "events": self.events,
        }
        if NewsModel.objects.filter(Q(type__name__startswith="Layihələr") | Q(type__name__startswith="Tədbirlər")).exists():
            self.projects_and_events_news = NewsModel.objects.filter(Q(type__name__startswith="Layihələr") | Q(type__name__startswith="Tədbirlər"))[:3]
            self.context["projects_and_events_news"] = self.projects_and_events_news

        if NewsModel.objects.filter(Q(type__name__startswith="Elanlar")):
            self.announcement_news = NewsModel.objects.filter(Q(type__name__startswith="Elanlar"))[:3]
            self.context["announcement_news"] = self.announcement_news

        if NewsModel.objects.filter(Q(type__name__startswith="Gənclər") | Q(type__name__startswith="İdman")).exists():
            self.youngs_and_sport_news = NewsModel.objects.filter(Q(type__name__startswith="Gənclər") | Q(type__name__startswith="İdman"))[:3]
            self.context["youngs_and_sport_news"] = self.youngs_and_sport_news

        if NewsModel.objects.filter(Q(type__name__startswith="Biz mediada")).exists():
            self.in_media_news = NewsModel.objects.filter(Q(type__name__startswith="Biz mediada"))[:3]
            self.context["in_media_news"] = self.in_media_news
        
        return render(request, 'index.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "quiz":
            id = request.POST.get("sorgu")
            answer = FormmChoices.objects.get(id=id)
            answer.vote_number += 1
            answer.save()

        elif choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            OfferQuestionModel.objects.create(
                name = name,
                email = email,
                message = message
            )

        return redirect('gtib:index')

class AboutView(View):
    pagesettings = PageSettings.objects.first()

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
        }
        return render(request, 'haqqimizda.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            OfferQuestionModel.objects.create(
                name = name,
                email = email,
                message = message
            )
        return redirect('gtib:about')


class CharterView(View):
    pagesettings = PageSettings.objects.first()

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
        }
        return render(request, 'nizamname.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            OfferQuestionModel.objects.create(
                name = name,
                email = email,
                message = message
            )

        return redirect('gtib:charter')

class VolunteerView(View):
    pagesettings = PageSettings.objects.first()

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
        }
        return render(request, 'volunteer.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "volunteer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone_number = request.POST.get("phonenumber")
            address = request.POST.get("address")
            message = request.POST.get("message")

            VolunteersModel.objects.create(
                name = name,
                email = email,
                phone_number = phone_number,
                address = address,
                message = message
            )
        elif choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            OfferQuestionModel.objects.create(
                name = name,
                email = email,
                message = message
            )

        return redirect('gtib:volunteer')

class DepartmentsView(View):
    pagesettings = PageSettings.objects.first()

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
        }
        return render(request, 'departamentler.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            OfferQuestionModel.objects.create(
                name = name,
                email = email,
                message = message
            )

        return redirect('gtib:departments')

class DirectorsView(View):
    pagesettings = PageSettings.objects.first()

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
        }
        return render(request, 'idareheyeti.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            OfferQuestionModel.objects.create(
                name = name,
                email = email,
                message = message
            )

        return redirect('gtib:directors')
