from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from gtib.models import (
    PageSettings, NewsTypeModel, NewsModel, 
    FAQsModel, FormmModel, FormmChoices, 
    OfferQuestionModel, EventModel, VolunteersModel,
    PartnerModel, DirectorModel, VolunteerModel, 
    YouthOrganizationModel, EBookModel, PrintModel,
    OfferModel, IdeaModel, PhotoModel,
    VideoModel
    )


class IndexView(View):
    pagesettings = PageSettings.objects.first()
    firstnews = NewsModel.objects.first()
    allnews = NewsModel.objects.all()[1:7]
    quiz = FormmModel.objects.filter(is_highlighted=True)
    formmchoices = FormmModel.objects.filter(quiz=quiz)
    faqs = FAQsModel.objects.all()
    events = EventModel.objects.all()
    partners = PartnerModel.objects.all()


    def get(self, request, *args, **kwargs):
        if len(PageSettings.objects.all()) == 0:
            PageSettings.objects.create()

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

        id = request.GET.get("q")
        if id:
            thisnews = NewsModel.objects.get(id=id)
            data = {
                "image": thisnews.image.url,
                "content": thisnews.content,
                "typename": thisnews.get_typename(),
                "slug": thisnews.slug,
            }
            return JsonResponse(data)
        
        return render(request, 'index.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "quiz":
            id = request.POST.get("sorgu")
            if id:
                answer = FormmChoices.objects.get(id=id)
                answer.vote_number += 1
                answer.save()
            else:
                messages.info(request, "Zəhmət olmasa, seçim edin.")

        elif choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

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

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

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

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

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
            surname = request.POST.get("surname")
            email = request.POST.get("email")
            phone_number = request.POST.get("phonenumber")
            message = request.POST.get("message")

            if name and surname and email and phone_number and message:

                VolunteersModel.objects.create(
                    name = name + " " + surname,
                    email = email,
                    phone_number = phone_number,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa, bütün məlumatları daxil edin.")

        elif choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

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

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

        return redirect('gtib:departments')

class DirectorsView(View):
    pagesettings = PageSettings.objects.first()
    directors = DirectorModel.objects.all()

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
            "directors": self.directors,
        }
        return render(request, 'idareheyeti.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

        return redirect('gtib:directors')

class OurVolunteersView(View):
    pagesettings = PageSettings.objects.first()
    volunteers = VolunteerModel.objects.all()

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
        }

        paginator = Paginator(self.volunteers, 1)
        page_number = request.GET.get("page")
        self.page_obj = paginator.get_page(page_number)

        self.context["page_obj"] = self.page_obj
        return render(request, 'konullulerimiz.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

        return redirect('gtib:ourvolunteers')


class PartnersView(View):
    pagesettings = PageSettings.objects.first()
    partners = PartnerModel.objects.all()

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
            "partners": self.partners,
        }
        return render(request, 'terefdaslar.html', self.context)


    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

        return redirect('gtib:partners')


class EventsView(View):
    pagesettings = PageSettings.objects.first()
    events = NewsModel.objects.filter(type__name__startswith="Tədbirlər")
    anouncements = NewsModel.objects.filter(type__name__startswith="Elanlar")[:6]

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
            "anouncements": self.anouncements,
        }
        paginator = Paginator(self.events, 3)
        page_number = request.GET.get("page")
        self.page_obj = paginator.get_page(page_number)

        self.context["page_obj"] = self.page_obj
        return render(request, 'tedbirler.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

        return redirect('gtib:events')


class ProjectsView(View):
    pagesettings = PageSettings.objects.first()
    projects = NewsModel.objects.filter(type__name__startswith="Layihələr")
    anouncements = NewsModel.objects.filter(type__name__startswith="Elanlar")[:6]

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
            "anouncements": self.anouncements,
        }
        paginator = Paginator(self.projects, 3)
        page_number = request.GET.get("page")
        self.page_obj = paginator.get_page(page_number)

        self.context["page_obj"] = self.page_obj
        return render(request, 'layiheler.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

        return redirect('gtib:projects')

class OurMediasView(View):
    pagesettings = PageSettings.objects.first()
    ourmedias = NewsModel.objects.filter(type__name__startswith="Biz mediada")
    anouncements = NewsModel.objects.filter(type__name__startswith="Elanlar")[:6]

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
            "anouncements": self.anouncements,
        }
        paginator = Paginator(self.ourmedias, 3)
        page_number = request.GET.get("page")
        self.page_obj = paginator.get_page(page_number)

        self.context["page_obj"] = self.page_obj
        return render(request, 'bizmediada.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

        return redirect('gtib:ourmedias')


class YouthOrganizationsView(View):
    pagesettings = PageSettings.objects.first()
    organizations = NewsModel.objects.filter(type__name__startswith="Gənclər Təşkilatları")
    anouncements = NewsModel.objects.filter(type__name__startswith="Elanlar")[:6]

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
            "anouncements": self.anouncements,
        }
        paginator = Paginator(self.organizations, 3)
        page_number = request.GET.get("page")
        self.page_obj = paginator.get_page(page_number)

        self.context["page_obj"] = self.page_obj
        return render(request, 'genclerteskilatlari.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

        return redirect('gtib:youthorganizations')


class YoungsAndSportView(View):
    pagesettings = PageSettings.objects.first()
    youngsandsport = NewsModel.objects.filter(type__name__startswith="Gənclər və İdman")

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
        }
        paginator = Paginator(self.youngsandsport, 3)
        page_number = request.GET.get("page")
        self.page_obj = paginator.get_page(page_number)

        self.context["page_obj"] = self.page_obj
        return render(request, 'genclerveidman.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

        return redirect('gtib:youngsandsport')

class NewsView(View):
    pagesettings = PageSettings.objects.first()
    ournews = NewsModel.objects.filter(type__name__startswith="Xəbərlər")
    anouncements = NewsModel.objects.filter(type__name__startswith="Elanlar")[:6]

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
            "anouncements": self.anouncements,
        }
        paginator = Paginator(self.ournews, 3)
        page_number = request.GET.get("page")
        self.page_obj = paginator.get_page(page_number)

        self.context["page_obj"] = self.page_obj
        return render(request, 'xeberler.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

        return redirect('gtib:news')

class KarabakhView(View):
    pagesettings = PageSettings.objects.first()

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
        }
        return render(request, 'azerbaycan.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

        return redirect('gtib:karabakh')


class CultureView(View):
    pagesettings = PageSettings.objects.first()

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
        }
        return render(request, 'medeniyyet.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

        return redirect('gtib:culture')

class TourismView(View):
    pagesettings = PageSettings.objects.first()

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
        }
        return render(request, 'turizm.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

        return redirect('gtib:tourism')
    

class EBooksView(View):
    pagesettings = PageSettings.objects.first()
    ebooks = EBookModel.objects.all()

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
        }
        paginator = Paginator(self.ebooks, 2)
        page_number = request.GET.get("page")
        self.page_obj = paginator.get_page(page_number)

        self.context["page_obj"] = self.page_obj
        return render(request, 'elektronkitablar.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

        return redirect('gtib:ebooks')

class PrintsView(View):
    pagesettings = PageSettings.objects.first()
    prints = NewsModel.objects.filter(type__name__startswith="Nəşrlərimiz")

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
        }
        paginator = Paginator(self.prints, 3)
        page_number = request.GET.get("page")
        self.page_obj = paginator.get_page(page_number)

        self.context["page_obj"] = self.page_obj
        return render(request, 'nesrlerimiz.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

        return redirect('gtib:prints')

class OffersView(View):
    pagesettings = PageSettings.objects.first()

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
        }
        return render(request, 'teklifler.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")
        
        elif choice == "uoffers":
            name = request.POST.get("name")
            surname = request.POST.get("surname")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and surname and email and message:
                OfferModel.objects.create(
                    name = name,
                    surname = surname,
                    email = email,
                    message = message,
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

        return redirect('gtib:offers')

class IdeasView(View):
    pagesettings = PageSettings.objects.first()

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
        }
        return render(request, 'idea-banki.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")
        
        elif choice == "idea":
            name = request.POST.get("name")
            surname = request.POST.get("surname")
            email = request.POST.get("email")
            file = request.FILES.get("uploadfile")
            idea = request.POST.get("idea")

            if name and surname and email and idea:
                IdeaModel.objects.create(
                    name = name,
                    surname = surname,
                    email = email,
                    file = file,
                    idea = idea,
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

        return redirect('gtib:ideas')



class PhotosView(View):
    pagesettings = PageSettings.objects.first()
    photos = PhotoModel.objects.all()

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
        }
        paginator = Paginator(self.photos, 12)
        page_number = request.GET.get("page")
        self.page_obj = paginator.get_page(page_number)

        self.context["page_obj"] = self.page_obj
        return render(request, 'foto.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

        return redirect('gtib:photos')
    

class VideosView(View):
    pagesettings = PageSettings.objects.first()
    videos = PhotoModel.objects.all()

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
        }
        paginator = Paginator(self.videos, 12)
        page_number = request.GET.get("page")
        self.page_obj = paginator.get_page(page_number)

        self.context["page_obj"] = self.page_obj
        return render(request, 'video.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

        return redirect('gtib:videos')
    

class AnouncementsView(View):
    pagesettings = PageSettings.objects.first()
    anouncements = NewsModel.objects.filter(type__name__startswith="Elanlar")

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
        }
        paginator = Paginator(self.anouncements, 12)
        page_number = request.GET.get("page")
        self.page_obj = paginator.get_page(page_number)

        self.context["page_obj"] = self.page_obj
        return render(request, 'elanlar.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

        return redirect('gtib:anouncements')


class NewsDetailView(View):
    pagesettings = PageSettings.objects.first()
    anouncements = NewsModel.objects.filter(type__name__startswith="Elanlar")[:6]

    def get(self, request, typename, slug, *args, **kwargs):
        self.news = NewsModel.objects.get(slug=slug)
        self.context = {
            "pagesettings": self.pagesettings,
            "news": self.news,
            "typename": typename,
            "anouncements": self.anouncements,
        }
        return render(request, 'xeber.html', self.context)

    def post(self, request, typename, slug, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

        return redirect('gtib:newsdetail', {'typename': typename, 'slug': slug,})


class PhotoGalleryView(View):
    pagesettings = PageSettings.objects.first()
    photos = PhotoModel.objects.all()

    def get(self, request, *args, **kwargs):
        self.context = {
            "pagesettings": self.pagesettings,
        }
        paginator = Paginator(self.photos, 12)
        page_number = request.GET.get("page")
        self.page_obj = paginator.get_page(page_number)

        self.context["page_obj"] = self.page_obj
        return render(request, 'foto-gallery.html', self.context)

    def post(self, request, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "offer":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            if name and email and message:
                OfferQuestionModel.objects.create(
                    name = name,
                    email = email,
                    message = message
                )
            else:
                messages.info(request, "Zəhmət olmasa bütün məlumatları daxil edin.")

        return redirect('gtib:photogallery')