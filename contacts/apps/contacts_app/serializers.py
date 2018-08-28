from rest_framework import serializers

class contactsSerilizers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'url'

        )