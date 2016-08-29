from unittest import TestCase

from protov import MessageValidator
from tests.simple_pb2 import HelloRequest, Entity


class ProtoVTestCase(TestCase):

    def test_validate(self):
        validator = MessageValidator(HelloRequest)
        request = HelloRequest(name='Foo', age=5, tags=['abc', 'def', 'ghewereri'], codes={404: 'Not Found',  400: 'Bad Request'},
                               entities=[Entity(id='fine'), Entity(id='fine2')])

        validator.validate(request)
