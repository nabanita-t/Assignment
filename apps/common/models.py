import uuid
from django.db import models
from rest_framework.exceptions import ValidationError


class BaseModel(models.Model):
    """
    Base Model class to add an id, created_at, updated_at and deleted_at field as common for all models.
    properties: id (uuid), created_at, updated_at, deleted_at (timestamp)
    Methods : The added class methods can not be edited, For any other custom implementation related to any model
    can be added under same model
    """

    class Meta:
        """
        abstract base model class.
        abstract = True (abstract base class),
        ordering = ['field'],
        db_table = 'custom_db_table'
        Note: Django does make one adjustment to the Meta class of an abstract base class: before installing the Meta attribute, it sets abstract=False.
        """
        abstract = True

    objects = models.Manager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, editable=False)

    def __str__(self):
        """
        print: {id}/created_date
        :return:
        """
        return '{}-{}'.format(self.id, self.created_at)

    @classmethod
    def create_instance(cls, data):
        """Create Instance"""
        try:
            obj = cls.objects.create(**data)
            return obj
        except Exception as ex:
            raise ValidationError(str(ex))

    @classmethod
    def get_instance(cls, query):
        """Get Instance or Raise Error"""
        try:
            return cls.objects.get(**query)
        except Exception as ex:
            raise ValidationError(ex)

    @classmethod
    def get_instance_or_none(cls, query):
        """Get Instance or Return None"""
        try:
            return cls.objects.get(**query)
        except cls.DoesNotExist:
            return None

    @classmethod
    def filter_instance(cls, query):
        """Filter Instance"""
        return cls.objects.filter(**query)
