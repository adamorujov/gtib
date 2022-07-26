from django.urls import path
from gtib import views

app_name = "gtib"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('haqqimizda/', views.AboutView.as_view(), name="about"),
    path('nizamname/', views.CharterView.as_view(), name="charter"),
    path('departamentler/', views.DepartmentsView.as_view(), name="departments"),
    path('idareheyeti/', views.DirectorsView.as_view(), name="directors"),
    path('konulluler/', views.OurVolunteersView.as_view(), name="ourvolunteers"),
    path('terefdaslar/', views.PartnersView.as_view(), name="partners"),

    path('qarabagazerbaycandir/', views.KarabakhView.as_view(), name="karabakh"),
    path('medeniyyet/', views.CultureView.as_view(), name="culture"),
    path('turizm/', views.TourismView.as_view(), name="tourism"),

    path('layiheler/', views.ProjectsView.as_view(), name="projects"),
    path('tedbirler/', views.EventsView.as_view(), name="events"),
    path('bizmediada/', views.OurMediasView.as_view(), name="ourmedias"),

    path('fotolar/', views.PhotosView.as_view(), name="photos"),
    path('elanlar/', views.AnouncementsView.as_view(), name="anouncements"),
    path('foto-qalereya/', views.PhotoGalleryView.as_view(), name="photogallery"),

    path('genclerteskilatlari/', views.YouthOrganizationsView.as_view(), name="youthorganizations"),
    path('genclerveidman/', views.YoungsAndSportView.as_view(), name="youngsandsport"),
    path('xeberler/', views.NewsView.as_view(), name="news"),

    path('elektronkitablar/', views.EBooksView.as_view(), name="ebooks"),
    path('nesrlerimiz/', views.PrintsView.as_view(), name="prints"),

    path('konulluol/', views.VolunteerView.as_view(), name="volunteer"),
    path('teklifler/', views.OffersView.as_view(), name="offers"),
    path('ideya-banki/', views.IdeasView.as_view(), name="ideas"),

    path('<str:typename>/<slug:slug>/', views.NewsDetailView.as_view(), name="newsdetail"),
]