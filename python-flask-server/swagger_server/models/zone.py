# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Zone(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, lat_max: float=None, lon_min: float=None, count: int=None):
        """
        Zone - a model defined in Swagger

        :param lat_max: The lat_max of this Zone.
        :type lat_max: float
        :param lon_min: The lon_min of this Zone.
        :type lon_min: float
        :param count: The count of this Zone.
        :type count: int
        """
        self.swagger_types = {
            'lat_max': float,
            'lon_min': float,
            'count': int
        }

        self.attribute_map = {
            'lat_max': 'lat_max',
            'lon_min': 'lon_min',
            'count': 'count'
        }

        self._lat_max = lat_max
        self._lon_min = lon_min
        self._count = count

    @classmethod
    def from_dict(cls, dikt) -> 'Zone':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Zone of this Zone.
        :rtype: Zone
        """
        return deserialize_model(dikt, cls)

    @property
    def lat_max(self) -> float:
        """
        Gets the lat_max of this Zone.
        Latitude of the NO corner of the square.

        :return: The lat_max of this Zone.
        :rtype: float
        """
        return self._lat_max

    @lat_max.setter
    def lat_max(self, lat_max: float):
        """
        Sets the lat_max of this Zone.
        Latitude of the NO corner of the square.

        :param lat_max: The lat_max of this Zone.
        :type lat_max: float
        """

        self._lat_max = lat_max

    @property
    def lon_min(self) -> float:
        """
        Gets the lon_min of this Zone.
        Longitude of the NO corner of the square.

        :return: The lon_min of this Zone.
        :rtype: float
        """
        return self._lon_min

    @lon_min.setter
    def lon_min(self, lon_min: float):
        """
        Sets the lon_min of this Zone.
        Longitude of the NO corner of the square.

        :param lon_min: The lon_min of this Zone.
        :type lon_min: float
        """

        self._lon_min = lon_min

    @property
    def count(self) -> int:
        """
        Gets the count of this Zone.
        Total number of phone localized in the square.

        :return: The count of this Zone.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count: int):
        """
        Sets the count of this Zone.
        Total number of phone localized in the square.

        :param count: The count of this Zone.
        :type count: int
        """

        self._count = count

