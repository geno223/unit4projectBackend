from .models import Outfits
from rest_framework import serializers

# serializing and deserializing data (and data is the data from the table) to json
class OutfitSerializer(serializers.HyperlinkedModelSerializer):
    # for configuring the todoserializer above
    class Meta:
            #model to serialize
            model=Outfits
            #fields to show
            fields=('id', 'clothes_type', 'clothes_price', 'clothes_image')