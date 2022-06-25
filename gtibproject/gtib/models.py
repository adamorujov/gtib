from django.db import models
from ckeditor.fields import RichTextField


class PageSettings(models.Model):
    logo = models.ImageField("Loqo", blank=True, null=True)
    footer_logo = models.ImageField("Footer loqo", blank=True, null=True)
    headerbgimg = models.ImageField("Arxa fon şəkli", blank=True, null=True)
    favicon = models.ImageField("Ikon", blank=True, null=True)
    title = models.CharField("Əsas səhifə başlığı", max_length=256, blank=True, null=True)
    description = models.TextField("Əsas səhifə meta izahı", blank=True, null=True)
    keywords = models.TextField("Əsas səhifə açar sözləri", blank=True, null=True)

    phone_number = models.CharField("Telefon", max_length=30, blank=True, null=True)
    email = models.EmailField("Email", max_length=256, blank=True, null=True)
    address = models.TextField("Ünvan", blank=True, null=True)
    footer_map = models.ImageField("Xəritə", blank=True, null=True)
    footer_map_link = models.URLField("Xəritə linki", blank=True, null=True)

    about = models.TextField("Haqqımızda", blank=True, null=True)
    charter = models.TextField("Nizamnamə", blank=True, null=True)
    
    class Meta:
        verbose_name = "Parametr"
        verbose_name_plural = "Parametrlər"

    def save(self, *args, **kwargs):
        settings = PageSettings.objects.all()
        if len(settings) == 0 or self == PageSettings.objects.first():
            return super(PageSettings, self).save(*args, **kwargs)
        else:
            pass
    
    def __str__(self) -> str:
        return "Parametrlər"

    
class SocialMediaAccount(models.Model):
    setting = models.ForeignKey(PageSettings, verbose_name="Parametrlər", on_delete=models.CASCADE, related_name="socialmediaaccounts")
    name = models.CharField("Ad", max_length=25)
    link = models.URLField("Link", max_length=256)
    image = models.ImageField("Şəkil", blank=True, null=True)

    class Meta:
        verbose_name = "Sosial Media Hesabı"
        verbose_name_plural = "Sosial Media Hesabları"
        ordering = ("-id",)

    def __str__(self) -> str:
        return self.name

class NewsTypeModel(models.Model):
    name = models.CharField("Növ", max_length=256)

    class Meta:
        verbose_name = "Növ"
        verbose_name_plural = "Xəbər növləri"
        ordering = ("-id",)

    def __str__(self) -> str:
        return self.name

class NewsCategoryModel(models.Model):
    name = models.CharField("Kateqoriya", max_length=256)

    class Meta:
        verbose_name = "Kateqoriya"
        verbose_name_plural = "Xəbər kateqoriyaları"
        ordering = ("-id",)

    def __str__(self) -> str:
        return self.name

class NewsModel(models.Model):
    type = models.ForeignKey(NewsTypeModel, verbose_name="Növ", on_delete=models.CASCADE, related_name="typenews")
    categories = models.ManyToManyField(NewsCategoryModel, verbose_name="Kateqoriyalar", related_name="categorynews")
    image = models.ImageField("Başlıq şəkli")
    title = models.CharField("Başlıq", max_length=300)
    content = RichTextField("Mövzu")
    pub_date = models.DateTimeField("Nəşr olunma tarixi", auto_now_add=True)
    modified_date = models.DateTimeField("Yenilənmə tarixi", auto_now=True)

    class Meta:
        verbose_name = "Xəbər"
        verbose_name_plural = "Xəbərlər"
        ordering = ("-id",)

    def __str__(self) -> str:
        return self.title


class EventModel(models.Model):
    image = models.ImageField("Başlıq şəkli")
    title = models.CharField("Başlıq", max_length=300)
    content = RichTextField("Mövzu")
    date = models.DateField("Tarix", blank=True, null=True)
    time = models.TimeField("Vaxt", blank=True, null=True)
    address = models.CharField("Ünvan", max_length=256)

    class Meta:
        verbose_name = "Tədbir"
        verbose_name_plural = "Tədbirlər"
        ordering = ("-id",)

    def __str__(self) -> str:
        return self.title

class FAQsModel(models.Model):
    question = models.CharField("Sual", max_length=500)
    answer = models.TextField("Cavab")

    class Meta:
        verbose_name = "Sual"
        verbose_name_plural = "Tez-tez verilən suallar"
        ordering = ("-id",)

    def __str__(self) -> str:
        return self.question


class FormmModel(models.Model):
    quiz = models.CharField("Sorğu", max_length=256)
    is_highlighted = models.BooleanField("Önə çıxan", default=False)

    class Meta:
        verbose_name = "Sorğu"
        verbose_name_plural = "Sorğular"
        ordering = ("-id",)

    def __str__(self) -> str:
        return self.quiz

class FormmChoices(models.Model):
    quiz = models.ForeignKey(FormmModel, verbose_name="Sorğu", on_delete=models.CASCADE, related_name="formchoices")
    choice = models.CharField("Seçim", max_length=256)
    vote_number = models.IntegerField("Səs sayı", default=0)

    class Meta:
        verbose_name = "Seçim"
        verbose_name_plural = "Sorğu seçimləri"
        ordering = ("-id",)

    def __str__(self) -> str:
        return self.choice


class OfferQuestionModel(models.Model):
    name = models.CharField("Ad Soyad", max_length=100)
    email = models.EmailField("Email", max_length=256)
    message = models.TextField("Mesaj")

    class Meta:
        verbose_name = "Təklif/Sual"
        verbose_name_plural = "Təklif və Suallar"
        ordering = ("-id",)

    def __str__(self) -> str:
        return self.name


class VolunteersModel(models.Model):
    name = models.CharField("Ad soyad", max_length=100)
    email = models.EmailField("Email", max_length=256)
    phone_number = models.CharField("Telefon", max_length=20)
    address = models.CharField("Ünvan", max_length=256)
    message = models.TextField("Mesaj")

    class Meta:
        verbose_name = "Könüllü"
        verbose_name_plural = "Könüllülər"
        ordering = ("-id",)

    def __str__(self) -> str:
        return self.name