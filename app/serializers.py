from rest_framework import serializers

from app.models import User, ActivityPeriod


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']


class UserSerailizer(serializers.ModelSerializer):

    activity_periods = ActivitySerializer(many=True)

    class Meta:

        model = User
        fields = ['id', 'real_name', 'tz', 'activity_periods']
