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

#Пока не разобралась, как с помощью parametrize заставить валидацию учитывать тестовый MAX_STUD_PER_COURSE
# поэтому пока что просто в settings 2 стоит
@pytest.mark.django_db
def test_validate(client, student_factory, settings):
    settings.MAX_STUD_PER_COURSE = 2
    students = student_factory(_quantity=3)
    response = client.post('/api/v1/courses/',
                           data={'name': 'new course', 'students': [students[0].id, students[1].id, students[2].id]})
    assert response.status_code == 400


@pytest.mark.django_db
def test_get_course(client, course_factory):
    course = course_factory(_quantity=1)
    response = client.get(f'/api/v1/courses/{course[0].id}/')
    data = response.json()
    assert response.status_code == 200
    assert data['name'] == course[0].name


@pytest.mark.django_db
def test_get_course_by_id(client, course_factory):
    course = course_factory(_quantity=1)
    response = client.get(f'/api/v1/courses/?id={course[0].id}')
    data = response.json()
    assert response.status_code == 200
    assert data[0]['name'] == course[0].name


@pytest.mark.django_db
def test_get_course_by_name(client, course_factory):
    course = course_factory(_quantity=1)
    response = client.get(f'/api/v1/courses/?name={course[0].name}')
    data = response.json()
    assert response.status_code == 200
    assert data[0]['name'] == course[0].name


@pytest.mark.django_db
def test_courses_list(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    data = response.json()
    assert response.status_code == 200
    assert len(data) == len(courses)
    for i, c in enumerate(data):
        assert c['name'] == courses[i].name


@pytest.mark.django_db
def test_post_course(client, student_factory):
    students = student_factory(_quantity=2)
    response = client.post('/api/v1/courses/',
                           data={'name': 'new course', 'students': [students[0].id, students[1].id]})
    data = response.json()
    course = Course.objects.get(id=data['id'])
    assert response.status_code == 201
    assert data['name'] == course.name


@pytest.mark.django_db
def test_patch_course(client, course_factory):
    course = course_factory(_quantity=1)
    response = client.patch(f'/api/v1/courses/{course[0].id}/', data={'name': 'some course'})
    data = response.json()
    course = Course.objects.get(id=data['id'])
    assert response.status_code == 200
    assert data['name'] == course.name


@pytest.mark.django_db
def test_del_course(client, course_factory):
    course = course_factory(_quantity=1)
    response = client.delete(f'/api/v1/courses/{course[0].id}/')
    assert response.status_code == 204
