from django.contrib import admin
from .models import Airport, Flight, Passanger
# Register your models here.

class PassangerInline(admin.StackedInline):
	"""
	Passanger Model has flight filed, so we can add flights to passanger from passanger pannel.
	but in Flight model no reference to passanger, to get this done, we make Passanger inline admin
		and add this inline passanger panel to Flight admin.
	"""
	model = Passanger.flights.through
	extra = 1

class FlightAdmin(admin.ModelAdmin):
	# add additional inline section, that is another admin interface.
	inlines = [PassangerInline]


class PassangerAdmin(admin.ModelAdmin):
	filter_horizontal = ('flights', )

admin.site.register(Airport)
#  On Flight Panel, we added Passanger inline Admin panel, so we can add passaanger to flights from same interface
admin.site.register(Flight, FlightAdmin)

# added PassangerAdmin which containse an horizontal view of flights, so we can add passager to flights directly from Passanger Panel
admin.site.register(Passanger, PassangerAdmin)  
