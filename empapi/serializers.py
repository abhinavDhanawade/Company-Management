from rest_framework import serializers
from management.models import Employe

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employe
		fields ='__all__'