# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.error import Error
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDefaultController(BaseTestCase):
    """ DefaultController integration test stubs """

    def test_squares_streaming_get(self):
        """
        Test case for squares_streaming_get

        Most recent counts.
        """
        response = self.client.open('/v1/squares/streaming',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
