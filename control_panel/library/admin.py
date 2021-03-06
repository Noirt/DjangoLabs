from django.contrib import admin
from library.models import *

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'email')
	list_display_links = ('last_name', 'first_name',)
	ordering  = ('last_name', 'first_name',)

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'publisher', 'publication_date')
	list_display_links = ('title',)
	list_editable = ('publisher',)
	'''list_filter = ('authors', 'publisher','publication_date')'''
	ordering  = ('title',)
	search_fields = ('title',)
	date_hierarchy = 'publication_date'
	fieldsets = (
		(None, {'fields': ('title', 'authors')}),
		('Output data', {'classes': ('collapse',),'description': u'About book and publisher', 'fields': ('publisher', 'publication_date'),}),
	    )

class PublisherAdmin(admin.ModelAdmin):
	list_display = ('title', 'country', 'city')
	list_display_links = ('title',)
	ordering  = ('title',)	
	list_filter = ('country', 'city')
	fieldsets = (
		(None, {'fields': ('title', 'website')}),
		('Contact information', {'classes': ('collapse',),'fields': ('country', 'city','address'),}),
	    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
