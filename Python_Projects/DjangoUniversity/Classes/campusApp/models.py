from django.db import models


class UniversityCampus(models.Model):
    Campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    Campus_id = models.IntegerField(default="", blank=True, null=False)
    State = models.CharField(max_length=2, default="", blank=True, null=False)

    object = models.Manager()

    # Returns the input value of the Campus Name and State
    # field as a tuple to display in the browser instead of the default titles
    def __str__(self):
        display_Campus = '{0.Campus_name}: {0.State}'
        return display_Campus.format(self)

    # Removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campus"


