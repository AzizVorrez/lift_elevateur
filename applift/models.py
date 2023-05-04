from django.db import migrations, models

class Communes(models.Model):
    lib_comm = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.lib_comm

class Cities(models.Model):
    lib_city = models.CharField(max_length=255, blank=False)
    id_com = models.ForeignKey(Communes, on_delete=models.CASCADE)

    def __str__(self):
        return self.lib_city

class Keywords(models.Model):
    keywords = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.keywords