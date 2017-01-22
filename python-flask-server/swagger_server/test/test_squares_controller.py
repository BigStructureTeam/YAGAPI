# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.error import Error
from swagger_server.models.square import Square
from swagger_server.models.zone import Zone
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
                        ('end', 1.2)]
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
                        ('end', 1.2)]
        response = self.client.open('/v1/squares',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_squares_post(self):
        """
        Test case for squares_post

        Create squares
        """
        zones = [Zone()]
        query_string = [('timestamp', 56)]
        response = self.client.open('/v1/squares',
                                    method='POST',
                                    data=json.dumps(zones),
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
