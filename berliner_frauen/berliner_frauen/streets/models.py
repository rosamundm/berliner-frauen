from django.db import models


class Category(models.Model):
    """
    Category of the person's occupation or what they
    were known for
    """

    name = models.CharField(max_length=50)
    category_slug = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.category_slug = self.name.replace(" & ", "-").casefold()
        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Person(models.Model):
    core_data_added = models.BooleanField()
    entry_complete = models.BooleanField()
    name = models.CharField(max_length=60)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=50, null=True, blank=True)
    place_of_death = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ManyToManyField(
        Category,
        related_name="people",
        blank=True,
    )
    person_slug = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        umlaut_map = {
            ord("ä"): "ae",
            ord("Ä"): "ae",
            ord("ö"): "oe",
            ord("Ö"): "oe",
            ord("ü"): "ue",
            ord("Ü"): "ue",
        }
        self.person_slug = self.name.translate(umlaut_map).casefold()
        self.person_slug = self.person_slug.replace(" ", "-")
        super(Person, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "People"


class District(models.Model):
    name = models.CharField(max_length=50)
    district_slug = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        umlaut_map = {
            ord("ä"): "ae",
            ord("Ä"): "ae",
            ord("ö"): "oe",
            ord("Ö"): "oe",
            ord("ü"): "ue",
            ord("Ü"): "ue",
        }
        self.district_slug = self.name.translate(umlaut_map).casefold()
        super(District, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Street(models.Model):
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="streets"
    )
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    name = models.CharField(max_length=50)
    eponym = models.OneToOneField(Person, on_delete=models.CASCADE, null=True)
    street_slug = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        umlaut_map = {
            ord("ä"): "ae",
            ord("Ä"): "ae",
            ord("ö"): "oe",
            ord("Ö"): "oe",
            ord("ü"): "ue",
            ord("Ü"): "ue",
        }
        self.street_slug = self.name.translate(umlaut_map).casefold()
        super(Street, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
