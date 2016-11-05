from rest_framework import serializers
from nameIt.models import First, Last, Title, FONT_CHOICES

class TitleURLSerializer(serializers.HyperlinkedModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='titleDetail')
    class Meta:
        model = Title
        fields = ('id', 'value', 'font', 'link')

class FirstURLSerializer(serializers.HyperlinkedModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='firstDetail')
    class Meta:
        model = First
        fields = ('id', 'value', 'font', 'link')

class LastURLSerializer(serializers.HyperlinkedModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='lastDetail')
    class Meta:
        model = Last
        fields = ('id', 'value', 'font', 'link')

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ('id', 'value', 'font')

class FirstSerializer(serializers.ModelSerializer):
    class Meta:
        model = First
        fields = ('id', 'value', 'font')

class LastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Last
        fields = ('id', 'value', 'font')