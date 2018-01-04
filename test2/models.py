from django.db import models

class Book(models.Model):

    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=50, unique=True)
    date_created = models.DateField()

    def __str__(self):
        return self.book_name

class Page(models.Model):

    book_id = models.ForeignKey(Book)
    pg_no = models.IntegerField()
    date_created = models.DateField()

    def __str__(self):
        book_obj = new Book()
        return book_obj.__str__()
