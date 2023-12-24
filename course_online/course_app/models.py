from django.db import models

# Create your models here.
class Course(models.Model):
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField()
    durasi = models.IntegerField()

    def __str__(self):
        return self.judul

class Materi(models.Model):
    course = models.ForeignKey(Course, related_name='materi', on_delete=models.CASCADE)
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField()
    embed_link = models.URLField()

    def __str__(self):
        return self.judul
