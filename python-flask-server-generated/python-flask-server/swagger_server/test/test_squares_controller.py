# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.error import Error
from swagger_server.models.square import Square
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestSquaresController(BaseTestCase):
    """ SquaresController integration test stubs """

    def test_squares_average_get(self):
        """
        Test case for squares_average_get

        Average
        """
        query_string = [('lat_max', 1.2),
                        ('lat_min', 1.2),
                        ('lon_max', 1.2),
                        ('lon_min', 1.2),
                        ('start', 1.2),
                        ('end', 1.2),
                        ('type', 'type_example')]
        response = self.client.open('/v1/squares/average',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_squares_get(self):
        """
        Test case for squares_get

        Get detailed squares
        """
        query_string = [('lat_max', 1.2),
                        ('lat_min', 1.2),
                        ('lon_max', 1.2),
                        ('lon_min', 1.2),
                        ('start', 1.2),
                        ('end', 1.2),
                        ('type', 'type_example')]
        response = self.client.open('/v1/squares',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_squares_post(self):
        """
        Test case for squares_post

        Create square
        """
        query_string = [('lat_max', 1.2),
                        ('lon_min', 1.2),
                        ('timestamp', 56),
                        ('count', 56),
                        ('type', 'type_example')]
        response = self.client.open('/v1/squares',
                                    method='POST',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
