from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.utils.text import slugify


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

    about1 = models.TextField("Haqqımızda 1-ci hissə", blank=True, null=True)
    about2 = models.TextField("Haqqımızda 2-ci hissə", blank=True, null=True)
    about3 = models.TextField("Haqqımızda 3-cü hissə", blank=True, null=True)
    about4 = models.TextField("Haqqımızda 4-cü hissə", blank=True, null=True)

    about_img1 = models.ImageField("Şəkil 1", blank=True, null=True)
    about_img2 = models.ImageField("Şəkil 2", blank=True, null=True)

    charter = RichTextField("Nizamnamə", blank=True, null=True)
    charter_img = models.ImageField("Şəkil", blank=True, null=True)

    karabakh = RichTextUploadingField("Qarabağ Azərbaycandır!", blank=True, null=True)
    culture = RichTextField("Mədəniyyət", blank=True, null=True)
    tourism = RichTextField("Turizm", blank=True, null=True)
    
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
    meta_title = models.CharField("Meta başlıq", max_length=300, blank=True, null=True)
    meta_description = models.TextField("Meta izah", blank=True, null=True)
    meta_keyword = models.TextField("Meta açar sözlər", blank=True, null=True)
    type = models.ForeignKey(NewsTypeModel, verbose_name="Növ", on_delete=models.CASCADE, related_name="typenews")
    categories = models.ManyToManyField(NewsCategoryModel, verbose_name="Kateqoriyalar", related_name="categorynews")
    image = models.ImageField("Başlıq şəkli")
    title = models.CharField("Başlıq", max_length=300)
    content = RichTextField("Mövzu")
    pub_date = models.DateTimeField("Nəşr olunma tarixi", auto_now_add=True)
    modified_date = models.DateTimeField("Yenilənmə tarixi", auto_now=True)
    slug = models.SlugField("Slaq", max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = "Xəbər"
        verbose_name_plural = "Xəbərlər"
        ordering = ("-id",)

    def _generate_unique_slug(self):
        unique_slug = slugify(self.title)
        num = 1
        while NewsModel.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(unique_slug, num)
            num += 1
        return unique_slug

    def get_typename(self):
        typename = slugify(self.type.name)
        return typename

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

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
    message = models.TextField("Mesaj", blank=True, null=True)
    apply_date = models.DateTimeField("Müraciət tarixi", default=timezone.now)

    class Meta:
        verbose_name = "Könüllü müraciəti"
        verbose_name_plural = "Könüllü müraciətləri"
        ordering = ("-id",)

    def __str__(self) -> str:
        return self.name

class VolunteerModel(models.Model):
    image = models.ImageField("Şəkil", blank=True, null=True)
    name = models.CharField("Ad", max_length=100)
    surname = models.CharField("Soyad", max_length=100)
    fathername = models.CharField("Ata adı", max_length=100)
    about = models.TextField("Haqqında", blank=True, null=True)
    start_date = models.DateField("Könüllü olma tarixi", blank=True, null=True)
    events = models.TextField("İştirak etdiyi tədbirlər", blank=True, null=True)

    class Meta:
        verbose_name = "Könüllü"
        verbose_name_plural = "Könüllülər"
        ordering = ("-id",)

    def __str__(self) -> str:
        return self.name + " " + self.surname


class DirectorModel(models.Model):
    image = models.ImageField("Şəkil", blank=True, null=True)
    name = models.CharField("Ad", max_length=100)
    surname = models.CharField("Soyad", max_length=100)
    fathername = models.CharField("Ata adı", max_length=100)
    position = models.CharField("Vəzifə", max_length=256, blank=True, null=True)
    about = models.TextField("Haqqında", blank=True, null=True)
    start_date = models.DateField("Vəzifəyə başlama tarixi", blank=True, null=True)

    class Meta:
        verbose_name = "İdarə heyəti üzvü"
        verbose_name_plural = "İdarə heyəti"
        ordering = ("-id",)

    def __str__(self) -> str:
        return self.name + " " + self.surname


class PartnerModel(models.Model):
    logo = models.ImageField("Loqo", blank=True, null=True)
    name = models.CharField("Ad", max_length=256)
    link = models.URLField("Keçid linki", max_length=256, blank=True, null=True)

    class Meta:
        verbose_name = "Tərəfdaş"
        verbose_name_plural = "Tərəfdaşlar"
        ordering = ("-id",)

    def __str__(self) -> str:
        return self.name


class EBookModel(models.Model):
    image = models.ImageField("Şəkil")
    title = models.CharField("Başlıq", max_length=256)
    description = models.TextField("Haqqında")
    slug = models.SlugField("Slaq", max_length=256)
    book_file = models.FileField("Kitab", upload_to="uploads/", blank=True, null=True)

    class Meta:
        ordering = ("-id",)
        verbose_name = "Elektron kitab"
        verbose_name_plural = "Elektron kitablar"

    def _generate_unique_slug(self):
        unique_slug = slugify(self.title)
        num = 1
        while EBookModel.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(unique_slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class OfferModel(models.Model):
    name = models.CharField("Ad", max_length=50)
    surname = models.CharField("Soyad", max_length=50)
    email = models.EmailField("Email", max_length=256)
    message = models.TextField("Mesaj")
    sent_date = models.DateTimeField("Göndərildi")

    class Meta:
        ordering = ("-id",)
        verbose_name = "Təklif"
        verbose_name_plural = "Təkliflər"

    def save(self, *args, **kwargs):
        if self.id is None:
            self.sent_date = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name + " " + self.surname


class IdeaModel(models.Model):
    name = models.CharField("Ad", max_length=50)
    surname = models.CharField("Soyad", max_length=50)
    email = models.EmailField("Email", max_length=256)
    file = models.FileField("Fayl", upload_to="uploads/")
    idea = models.TextField("İdeya haqqında")
    sent_date = models.DateTimeField("Göndərildi")

    class Meta:
        ordering = ("-id",)
        verbose_name = "İdeya"
        verbose_name_plural = "İdeyalar"

    def save(self, *args, **kwargs):
        if self.id is None:
            self.sent_date = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name + " " + self.surname



class PhotoModel(models.Model):
    image = models.ImageField("Şəkil")
    title = models.CharField("Başlıq", max_length=256)
    pub_date = models.DateField("Tarix")
    slug = models.SlugField("Slaq", max_length=300, blank=True, null=True)

    class Meta:
        ordering = ("-id",)
        verbose_name = "Foto qalereya"
        verbose_name_plural = "Foto qalereya"

    def _generate_unique_slug(self):
        unique_slug = slugify(self.title)
        num = 1
        while PhotoModel.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(unique_slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class PhotosModel(models.Model):
    image = models.ImageField("Şəkil")
    title = models.CharField("Başlıq", max_length=256)
    pub_date = models.DateField("Tarix")
    gallery = models.ForeignKey(PhotoModel, on_delete=models.CASCADE, verbose_name="Qalereya")

    class Meta:
        ordering = ("-id",)
        verbose_name = "Foto"
        verbose_name_plural = "Fotolar"

    def __str__(self):
        return self.title


class VideoModel(models.Model):
    image = models.ImageField("Şəkil")
    title = models.CharField("Başlıq", max_length=256)
    pub_date = models.DateField("Tarix")

    class Meta:
        ordering = ("-id",)
        verbose_name = "Foto"
        verbose_name_plural = "Fotolar"

    def __str__(self):
        return self.title

