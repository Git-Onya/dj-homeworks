from rest_framework.test import APIClient
import pytest as pytest
from model_bakery import baker
from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_course(client, course_factory):
    course = course_factory(_quantity=1)
    for c in course:
        course_id = c.id
        course_name = c.name
    response = client.get(f'/api/v1/courses/{course_id}/')
    data = response.json()
    assert response.status_code == 200
    assert data['name'] == course_name


@pytest.mark.django_db
def test_courses_list(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    data = response.json()
    assert response.status_code == 200
    assert len(data) == len(courses)
    for i, c in enumerate(data):
        assert c['name']==courses[i].name

@pytest.mark.django_db
def test_post_course(client, course_factory):
    response = client.post('/api/v1/courses/', data = {'name': 'ggg', 'students': 1})


    # data = response.json()
    assert response.status_code == 201
    # assert