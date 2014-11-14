from django.contrib import admin
from gerador.models import Advogado, Imovel
from django.utils.safestring import SafeString

# Register your models here.

class ImovelAdmin(admin.ModelAdmin):
	list_display = ('nome', 'link')

	def link(self, obj):
		return SafeString('<a href="/texto/%d" target="_blank">abrir</a>' % obj.id)

admin.site.register(Imovel, ImovelAdmin)
admin.site.register(Advogado)