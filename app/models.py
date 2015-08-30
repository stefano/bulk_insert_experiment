from django.db import models


class TestModel(models.Model):
    field_1 = models.IntegerField()
    field_2 = models.CharField(max_length=255)
    field_3 = models.DateTimeField()

    class Meta:
        app_label = 'app'
