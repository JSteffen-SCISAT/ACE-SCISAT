__docformat__ = 'epytext'

from django.db import models
from publications.models import Publication,List

class PublicationLists(models.Model):
    id = models.AutoField(primary_key=True)
    publication = models.ForeignKey('Publication', models.CASCADE)
    list = models.ForeignKey('List', models.CASCADE)
	
    class Meta:
        managed = False
        db_table = 'publications_publication_lists'
        unique_together = (('publication', 'list'),)
