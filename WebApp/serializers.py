from rest_framework import serializers
from WebApp.models import Users
class UsersSerializer(serializers.ModelSerializer):
    EmpName=serializers.CharField(required=False)
    EmpRank = serializers.IntegerField(required=False)
    EmpId = serializers.IntegerField(required=False)
    class Meta:
        model=Users
        fields='__all__'