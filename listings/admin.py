from django.contrib import admin

# Register your models here.
from .models import Listing
import json
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields








class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','list_date','realtor')
    list_display_links = ('id','title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title','description','address','city','state','zipcode','price',)
    formfield_overrides = {
        map_fields.AddressField: {'widget':
                                  map_widgets.GoogleMapsAddressWidget(attrs={'data-autocomplete-options': json.dumps({'types': ['geocode',
                                                                                                                                'establishment'], 'componentRestrictions': {
                                      'country': 'us'
                                  }
                                  })
                                  })
                                  },
    }


admin.site.register(Listing,ListingAdmin)
