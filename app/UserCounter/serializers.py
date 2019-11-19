from rest_framework import serializers


class testser(serializers.BaseSerializer):
    def to_representation(self, obj, id):
        return {
            'user_id': id,
            'counter': obj.value
        }
