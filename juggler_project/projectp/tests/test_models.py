from django.test import TestCase
from ..models import Project
from ..models import Task


class TestProjectModel(TestCase):
    """
    Test the project model.
    """
    def setUp(self):
        self.project = Project(name="Computer Vision")
        self.project.save()

    def test_create_project(self):
        self.assertIsInstance(self.project, Project)

    def test_str_representation(self):
        self.assertEquals(str(self.project), "Computer Vision")

    def test_update_project(self):
        pk = self.project.pk
        project = Project.objects.get(pk=pk)
        project.name = "SOS Device for Cyclist"
        project.save()
        self.assertEquals(project.name, "SOS Device for Cyclist")

    def test_delete_project(self):
        pk = self.project.pk
        project = Project.objects.get(pk=pk)
        project.delete()
        self.assertFalse(Project.objects.filter(pk=pk).exists())


class TestTaskModel(TestCase):
    """
    Test the task model.
    """
    def setUp(self):
        self.project = Project(name="Computer Vision")
        self.project.save()
        self.task = Task(title="Present Paper",
                         description="Present recent papers in the field of computer vision.",
                         project=self.project,
                         time_estimate=0.4)
        self.task.save()

    def test_create_task(self):
        self.assertIsInstance(self.task, Task)

    def test_str_representation(self):
        self.assertEquals(str(self.task), "Present Paper")

    def test_update_task(self):
        pk = self.task.pk
        task = Task.objects.get(pk=pk)
        task.completed = True
        task.save()
        self.assertTrue(task.completed)

    def test_delete_taks(self):
        pk = self.task.pk
        task = Task.objects.get(pk=pk)
        task.delete()
        self.assertFalse(Task.objects.filter(pk=pk).exists())
