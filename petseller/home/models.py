from django.db import models
from django.contrib.auth.models import User

"""
what is BaseModel?
Models are the single, definitive source of information about your data.
Models contain the essential fields and behaviors of the data you’re storing. Django follows the DRY (Don’t Repeat Yourself) principle, and models are a great way to encapsulate your data in a single place.

why BaseModel?
Models are Python classes that define the fields and behaviors of the data you’re storing. Django provides a powerful ORM (Object-Relational Mapping) system that allows you to interact with your database using Python code instead of SQL.
This makes it easier to work with databases and allows you to focus on your application logic rather than the underlying database structure.


"""

class BaseModel(models.Model):
    """
    Abstract base model to be inherited by other models.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

        # The ordering option specifies the default ordering for the model's objects when they are retrieved from the database.
        # In this case, the objects will be ordered by the created_at field in descending order (newest first).
        # This means that when you query the model, the results will be sorted by the created_at field, with the most recently created objects appearing first.

"""
what is Meta class?
The Meta class is an inner class in a Django model that provides metadata to the model. It allows you to define options and configurations for the model, such as database table name, ordering, verbose name, and more.
The Meta class is used to customize the behavior of the model and how it interacts with the database. It is not required, but it is commonly used to define additional properties for the model.

What is one complex and advance example of Meta class?
The Meta class can be used to define complex relationships between models, such as many-to-many relationships, and to specify how those relationships should be handled in the database. For example, you can use the Meta class to define a through model for a many-to-many relationship, which allows you to add additional fields to the relationship.

exmaple of META class:

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

    class Meta:
        ordering = ['publication_date']
        unique_together = ('title', 'author')
        verbose_name_plural = "Books"
        db_table = 'library_books'

        # The unique_together option specifies that the combination of title and author must be unique in the database.
        # The verbose_name_plural option specifies the plural name for the model in the admin interface.
        # The db_table option specifies the name of the database table to use for the model.
        # This allows you to customize the behavior of the model and how it interacts with the database.
        # It is not required, but it is commonly used to define additional properties for the model.

why write abstract = True?
# The abstract = True option in the Meta class indicates that this model is an abstract base class and should not be created as a separate table in the database.
# Instead, it will be used as a base class for other models that inherit from it.
# This allows you to define common fields and behaviors for multiple models without creating a separate table for the base model.

what is abstract model?
# An abstract model is a model that is not meant to be instantiated or used directly. Instead, it serves as a base class for other models.
# Abstract models are useful for defining common fields and behaviors that can be shared across multiple models.
# By using abstract models, you can avoid code duplication and keep your models DRY (Don't Repeat Yourself).
# When you create a model that inherits from an abstract model, Django will create a separate table for the child model, but not for the abstract model itself.
# This allows you to define common fields and behaviors for multiple models without creating a separate table for the base model.

what is the purpose of abstract model?
# The purpose of an abstract model is to provide a way to define common fields and behaviors that can be shared across multiple models.
# This allows you to avoid code duplication and keep your models DRY (Don't Repeat Yourself).

what is verbose?
# The term "verbose" generally refers to something that is wordy or uses more words than necessary to convey a message.
# In the context of programming, verbose often refers to code or output that is detailed and includes a lot of information, which can be helpful for debugging or understanding the code, but may also be overwhelming or unnecessary in some cases.


"""

class Category(BaseModel):
    """
    Model representing a category of animals.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class AnimalBreed(BaseModel):
    """
    Model representing a breed of animals.
    """
    animal_breed = models.CharField(max_length=100)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='animal_breeds')

    def __str__(self):
        return self.name
    
class AnimalColor(BaseModel):
    """
    Model representing a color of animals.
    """
    animal_color = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Create your models here.
class Animal(BaseModel):
    """
    Model representing an animal.
    """
    animal_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='animals')
    animal_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='animals_category')
    animal_name = models.CharField(max_length=100)
    animal_breed = models.ManyToManyField(AnimalBreed, related_name='animal_breeds', null=True, blank=True)
    animal_color = models.ManyToManyField(AnimalColor, related_name='animal_colors', null=True, blank=True)
    age = models.IntegerField()
    animal_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    animal_views = models.IntegerField(default=0)
    animal_likes = models.IntegerField(default=1)
    animal_image = models.ImageField(upload_to='animal_images/')
    animal_location = models.ManyToManyField('Location', through='AnimalLocation')
    created_at = models.DateTimeField(auto_now_add=True)
    animal_slug = models.SlugField(unique=True, max_length=100)

    # what is slug field?
    # A slug field is a short label for something, containing only letters, numbers, underscores or hyphens.
    # It is generally used in URLs to identify a particular resource in a human-readable way.
    # For example, a slug for "Hello World!" could be "hello-world".
    # Slugs are often used in web applications to create user-friendly URLs.
    # For example, instead of having a URL like "/articles/12345", you might have "/articles/hello-world".
    # This makes the URL more readable and easier to remember.

    def __str__(self):
        return self.name
    
class Location(BaseModel):
    """
    Model representing a location.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class AnimalLocation(BaseModel):

    """
    Model representing the location of an animal.
    """
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.animal.name} - {self.location.name}"

