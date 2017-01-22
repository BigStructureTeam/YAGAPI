import connexion
from swagger_server.models.error import Error
from swagger_server.models.square import Square
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def squares_average_get(lat_max, lat_min, lon_max, lon_min, start, end, type):
    """
    Average
    The average of people in the given area between the initial instant and the final instant required
    :param lat_max: Latitude of the NO point describing the zone.
    :type lat_max: float
    :param lat_min: Longitude of the South East point describing the zone.
    :type lat_min: float
    :param lon_max: Latitude of the South East point describing the zone.
    :type lon_max: float
    :param lon_min: Longitude of the NO point describing the zone.
    :type lon_min: float
    :param start: The beginning of the interval considered for the average required.
    :type start: float
    :param end: The end of the interval considered for the average required.
    :type end: float
    :param type: Can be &#39;big&#39; or &#39;small&#39;.
    :type type: str

    :rtype: List[Square]
    """
    return 'do some magic!'


def squares_get(lat_max, lat_min, lon_max, lon_min, start, end, type):
    """
    Get detailed squares
    The minute by minute detail of people in the given area between the initial instant and the final instant required
    :param lat_max: Latitude of the NO point describing the zone.
    :type lat_max: float
    :param lat_min: Longitude of the South East point describing the zone.
    :type lat_min: float
    :param lon_max: Latitude of the South East point describing the zone.
    :type lon_max: float
    :param lon_min: Longitude of the NO point describing the zone.
    :type lon_min: float
    :param start: The beginning of the interval considered for the details required.
    :type start: float
    :param end: The end of the interval considered for the details required.
    :type end: float
    :param type: Can be &#39;big&#39; or &#39;small&#39;.
    :type type: str

    :rtype: List[Square]
    """
    return 'do some magic!'


def squares_post(lat_max, lon_min, timestamp, count, type):
    """
    Create square
    Create a new square.
    :param lat_max: Latitude of the NO point describing the zone.
    :type lat_max: float
    :param lon_min: Longitude of the NO point describing the zone.
    :type lon_min: float
    :param timestamp: Timestamp to which the count was made.
    :type timestamp: int
    :param count: Total number of phone localized in the square.
    :type count: int
    :param type: Can be &#39;big&#39; or &#39;small&#39;.
    :type type: str

    :rtype: None
    """
    return 'do some magic!'
