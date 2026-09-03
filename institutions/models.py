from django.db import models


class Institution(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE,
        related_name="departments"
    )

    def __str__(self):
        return f"{self.name} - {self.institution.name}"