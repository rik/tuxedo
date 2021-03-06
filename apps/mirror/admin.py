from django.contrib import admin

from mirror.models import Mirror, OS, Product, Location, ProductLanguage


class LocationAdmin(admin.ModelAdmin):
    list_display = ('product', 'os', 'path')
    list_filter = ('product', 'os')
    ordering = ('product',)
admin.site.register(Location, LocationAdmin)


class MirrorAdmin(admin.ModelAdmin):
    exclude = ('count',)
    list_display = ('active', 'rating', 'name', 'baseurl', 'count',
                    'admin_contacts')
    list_display_links = ('name',)
    list_editable = ('active',)
    list_filter = ('active',)
    ordering = ('active',)
    search_fields = ['name', 'baseurl']
admin.site.register(Mirror, MirrorAdmin)


class OSAdmin(admin.ModelAdmin):
    list_display = ('name', 'priority')
    ordering = ('priority',)
admin.site.register(OS, OSAdmin)


class ProductLanguageInline(admin.TabularInline):
    model = ProductLanguage
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'priority', 'count', 'active', 'checknow')
    list_filter = ('active', 'checknow')
    ordering = ('name',)
    actions = ('mark_for_checknow',)
    inlines = [ProductLanguageInline]

    def mark_for_checknow(self, request, queryset):
        """Custom action to mark a list of products for sentry checking"""
        rows_updated = queryset.update(checknow=True)
        msg = "%s project(s) marked for Sentry checking."
        self.message_user(request, msg % rows_updated)

    mark_for_checknow.short_description = (
        "Check selected products now with Sentry")
admin.site.register(Product, ProductAdmin)
