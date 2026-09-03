from django.db import models


class Hospital(models.Model):

    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Department(models.Model):

    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Doctor(models.Model):

    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=200)

    def __str__(self):
        return self.name