from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django_testing.settings import MAX_STUD_PER_COURSE
from students.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, data):
        if self.context["view"].action == 'partial_update' and 'students' not in data:
            return data
        if len(data['students']) > MAX_STUD_PER_COURSE:
            raise ValidationError(f'No more than {MAX_STUD_PER_COURSE} students per course')
        return data
