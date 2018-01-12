from django.db import models
from django.utils.encoding import python_2_unicode_compatible

PRODUCT_TYPE_CHOICES = (
		('dress', 'dress'),
		('seremoni', 'seremoni'),
		('skjorte', 'skjorte'),
		('sko', 'sko'),
		('smoking', 'smoking'),
		('slips', 'slips'),
		('mansjett', 'mansjett'),
		('sloyfe', 'sloyfe')
)

### Index contains 3 parts of database; NewsImage, IndexContent and IndexProduct

class NewsImage(models.Model):
	image = models.FileField()
	description = models.CharField(max_length=500)

	def __str__(self):
		return self.description

# @python_2_unicode_compatible fixed the ae, aa, oo when try to insert into database in admin section		
@python_2_unicode_compatible
class IndexContent(models.Model):
	content = models.TextField(max_length=10000)

	def __str__(self):
		return self.content

class IndexProduct(models.Model):
	title = models.CharField(max_length=250)
	description = models.CharField(max_length=500)
	content = models.CharField(max_length=2000)
	image = models.FileField()
	product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)

	def __str__(self):
		return self.title + ' - ' + self.description + ' - ' + self.product_type

### end of index

class Collection(models.Model):
	name = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)
	content = models.TextField(max_length=3000)
	image = models.FileField()

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Tip(models.Model):
	image = models.FileField()
	headline = models.CharField(max_length=200)
	tip_text = models.TextField(max_length=3000)
	
	def __str__(self):
		return self.headline

@python_2_unicode_compatible
class Dressen_sitte(models.Model):
	image = models.FileField()
	headline = models.CharField(max_length=200)
	tip_text = models.TextField(max_length=3000)
	
	def __str__(self):
		return self.headline

@python_2_unicode_compatible
class Dress_guide(models.Model):
	image = models.FileField()
	headline = models.CharField(max_length=200)
	tip_text = models.TextField(max_length=3000)
	
	def __str__(self):
		return self.headline

@python_2_unicode_compatible
class Contact(models.Model):
	mapImage = models.FileField()
	address = models.TextField(max_length=3000)
	info = models.FileField()
	job = models.TextField(max_length=3000)

	def __str__(self):
		return self.address

### product model

@python_2_unicode_compatible
class Dress(models.Model):
	title = models.CharField(max_length=250)
	description = models.CharField(max_length=500)
	content = models.CharField(max_length=2000)

	product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)
	image = models.FileField()

	def __str__(self):
		return self.title + ' - ' + self.description

@python_2_unicode_compatible
class Seremoni(models.Model):
	title = models.CharField(max_length=250)
	description = models.CharField(max_length=500)
	content = models.CharField(max_length=2000)
	product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)
	image = models.FileField()

	def __str__(self):
		return self.title + ' - ' + self.description

@python_2_unicode_compatible
class Skjorte(models.Model):
	title = models.CharField(max_length=250)
	description = models.CharField(max_length=500)
	content = models.CharField(max_length=2000)
	product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)
	image = models.FileField()

	def __str__(self):
		return self.title + ' - ' + self.description

@python_2_unicode_compatible
class Sko(models.Model):
	title = models.CharField(max_length=250)
	description = models.CharField(max_length=500)
	content = models.CharField(max_length=2000)
	product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)
	image = models.FileField()

	def __str__(self):
		return self.title + ' - ' + self.description

@python_2_unicode_compatible
class Smoking(models.Model):
	title = models.CharField(max_length=250)
	description = models.CharField(max_length=500)
	content = models.CharField(max_length=2000)
	product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)
	image = models.FileField()

	def __str__(self):
		return self.title + ' - ' + self.description

@python_2_unicode_compatible
class Slips(models.Model):
	title = models.CharField(max_length=250)
	description = models.CharField(max_length=500)
	content = models.CharField(max_length=2000)
	product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)
	image = models.FileField()

	def __str__(self):
		return self.title + ' - ' + self.description

@python_2_unicode_compatible
class Mansjett(models.Model):
	title = models.CharField(max_length=250)
	description = models.CharField(max_length=500)
	content = models.CharField(max_length=2000)
	product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)
	image = models.FileField()

	def __str__(self):
		return self.title + ' - ' + self.description

@python_2_unicode_compatible
class Sloyfe(models.Model):
	title = models.CharField(max_length=250)
	description = models.CharField(max_length=500)
	content = models.CharField(max_length=2000)
	product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)
	image = models.FileField()

	def __str__(self):
		return self.title + ' - ' + self.description

### end of product model



