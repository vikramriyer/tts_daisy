from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# some utility methods
def is_alpha_numeric(name):
    if 1!=1:
        raise ValidationError("Username is not valid. ")

# Create your models here.
class Editor2(models.Model):

    book_name = models.ForeignKey(Books)
    user_name = models.ForeignKey('auth.User')

class Books(models.Model):

    book_name = models.CharField(max_length=100, unique=True)
    user_name = models.ForeignKey('auth.User')
    date_added = models.DateField(default=timezone.now())
    publish_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, default='inactive') # convert to enum type later
    description = models.TextField()
    last_accessed = models.DateField(default=timezone.now())

    def publish(self):
        '''
        This method will be called once all the pages are edited and the
        daisy pipeline is run and finally the conversion of book is
        successful.
        '''
        self.publish_date = timezone.now()
        self.status = 'completed'
        self.save()

    def __str__(self):
        return self.book_name

class Pages(models.Model):

    book_name = models.ForeignKey(Books)
    page_number = models.IntegerField()
    text = models.TextField()
    image = models.ImageField()

    def load_page(self, book_name, page_number):
        '''
        load the next page from the requested book.
        page_number has the current page number that is loaded,
        so search the next page number in the db and load it for a
        particular book.
        if page number is null or 0, then load the first page of the
        requested book. 
        '''
        pass
