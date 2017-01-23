import connexion
import math
from swagger_server.models.error import Error
from swagger_server.models.square import Square
from swagger_server.models.zone import Zone
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from neo4j.v1 import GraphDatabase, basic_auth


def squares_average_get(lat_max, lat_min, lon_max, lon_min, start, end):
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

    :rtype: List[Square]
    """

    # TODO: on ne prend pas en compte les 0, ce n'est pas une vraiment une moyenne

    # Open connexion with Neo4j db
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "arthur"))
    session = driver.session()
    # TODO: Check parameters
    deg_lat_min, dix_lat_min, cent_lat_min, mil_lat_min = decompose(lat_min)
    deg_lat_max, dix_lat_max, cent_lat_max, mil_lat_max = decompose(lat_max)
    deg_lon_min, dix_lon_min, cent_lon_min, mil_lon_min = decompose(lon_min)
    deg_lon_max, dix_lon_max, cent_lon_max, mil_lon_max = decompose(lon_max)

    result = session.run("CALL ga.timetree.events.range({start: toInteger("+str(start)+"), end: toInteger("+str(end)+")}) YIELD node "
                         "WITH node "
                         "MATCH (lat:LatTreeRoot)-[:CHILD]->(deg:Degre) "
                         "WHERE deg.value >= toInteger("+str(deg_lat_min)+") AND deg.value <= toInteger("+str(deg_lat_max)+") "
                         "WITH node, deg "
                         "MATCH (deg)-[:CHILD]->(dix:Dixieme) "
                         "WHERE CASE WHEN "+("true" if deg_lat_min==deg_lat_max else "false")+" AND dix.value >= toInteger("+str(dix_lat_min)+") AND dix.value <= toInteger("+str(dix_lat_max)+") THEN true "
                         "WHEN deg.value = toInteger("+str(deg_lat_min)+") AND dix.value < toInteger("+str(dix_lat_min)+") THEN false "
                         "WHEN deg.value = toInteger("+str(deg_lat_max)+") AND dix.value > toInteger("+str(dix_lat_max)+") THEN false "
                         "ELSE true END "
                         "WITH node, deg.value AS deg_lat, dix "
                         "MATCH (dix)-[:CHILD]->(cent:Centieme) "
                         "WHERE CASE WHEN "+("true" if deg_lat_min==deg_lat_max and dix_lat_min==dix_lat_max else "false")+" AND cent.value >= toInteger("+str(cent_lat_min)+") AND cent.value <= toInteger("+str(cent_lat_max)+") THEN true "
                         "WHEN deg_lat = toInteger("+str(deg_lat_min)+") AND dix.value = toInteger("+str(dix_lat_min)+") AND cent.value < toInteger("+str(cent_lat_min)+") THEN false "
                         "WHEN deg_lat = toInteger("+str(deg_lat_max)+") AND dix.value = toInteger("+str(dix_lat_max)+") AND cent.value > toInteger("+str(cent_lat_max)+") THEN false "
                         "ELSE true END "
                         "WITH node, deg_lat, dix.value AS dix_lat, cent "
                         "MATCH (cent)-[:CHILD]->(mil:Millieme) "
                         "WHERE CASE WHEN "+("true" if deg_lat_min==deg_lat_max and dix_lat_min==dix_lat_max and cent_lat_min==cent_lat_max else "false")+" AND mil.value >= toInteger("+str(mil_lat_min)+") AND mil.value <= toInteger("+str(mil_lat_max)+") THEN true "
                         "WHEN deg_lat = toInteger("+str(deg_lat_min)+") AND dix_lat = toInteger("+str(dix_lat_min)+") AND cent.value = toInteger("+str(cent_lat_min)+") AND mil.value < toInteger("+str(mil_lat_min)+") THEN false "
                         "WHEN deg_lat = toInteger("+str(deg_lat_max)+") AND dix_lat = toInteger("+str(dix_lat_max)+") AND cent.value = toInteger("+str(cent_lat_max)+") AND mil.value > toInteger("+str(mil_lat_max)+") THEN false "
                         "ELSE true END "
                         "WITH node, deg_lat, dix_lat, cent.value AS cent_lat, mil "
                         "MATCH (node)-[:LAT]->(mil) "
                         "WITH node, deg_lat, dix_lat, cent_lat, mil.value AS mil_lat "
                         "MATCH (lon:LonTreeRoot)-[:CHILD]->(deg:Degre) "
                         "WHERE deg.value >= toInteger("+str(deg_lon_min)+") AND deg.value <= toInteger("+str(deg_lon_max)+") "
                         "WITH node, deg_lat, dix_lat, cent_lat, mil_lat, deg "
                         "MATCH (deg)-[:CHILD]->(dix:Dixieme) "
                         "WHERE CASE WHEN "+("true" if deg_lon_min==deg_lon_max else "false")+" AND dix.value >= toInteger("+str(dix_lon_min)+") AND dix.value <= toInteger("+str(dix_lon_max)+") THEN true "
                         "WHEN deg.value = toInteger("+str(deg_lon_min)+") AND dix.value < toInteger("+str(dix_lon_min)+") THEN false "
                         "WHEN deg.value = toInteger("+str(deg_lon_max)+") AND dix.value > toInteger("+str(dix_lon_max)+") THEN false "
                         "ELSE true END "
                         "WITH node, deg_lat, dix_lat, cent_lat, mil_lat, deg.value AS deg_lon, dix "
                         "MATCH (dix)-[:CHILD]->(cent:Centieme) "
                         "WHERE CASE WHEN "+("true" if deg_lon_min==deg_lon_max and dix_lon_min==dix_lon_max else "false")+" AND cent.value >= toInteger("+str(cent_lon_min)+") AND cent.value <= toInteger("+str(cent_lon_max)+") THEN true "
                         "WHEN deg_lon = toInteger("+str(deg_lon_min)+") AND dix.value = toInteger("+str(dix_lon_min)+") AND cent.value < toInteger("+str(cent_lon_min)+") THEN false "
                         "WHEN deg_lon = toInteger("+str(deg_lon_max)+") AND dix.value = toInteger("+str(dix_lon_max)+") AND cent.value > toInteger("+str(cent_lon_max)+") THEN false "
                         "ELSE true END "
                         "WITH node, deg_lat, dix_lat, cent_lat, mil_lat, deg_lon, dix.value AS dix_lon, cent "
                         "MATCH (cent)-[:CHILD]->(mil:Millieme) "
                         "WHERE CASE WHEN "+("true" if deg_lon_min==deg_lon_max and dix_lon_min==dix_lon_max and cent_lon_min==cent_lon_max else "false")+" AND mil.value >= toInteger("+str(mil_lon_min)+") AND mil.value <= toInteger("+str(mil_lon_max)+") THEN true "
                         "WHEN deg_lon = toInteger("+str(deg_lon_min)+") AND dix_lon = toInteger("+str(dix_lon_min)+") AND cent.value = toInteger("+str(cent_lon_min)+") AND mil.value < toInteger("+str(mil_lon_min)+") THEN false "
                         "WHEN deg_lon = toInteger("+str(deg_lon_max)+") AND dix_lon = toInteger("+str(dix_lon_max)+") AND cent.value = toInteger("+str(cent_lon_max)+") AND mil.value > toInteger("+str(mil_lon_max)+") THEN false "
                         "ELSE true END "
                         "WITH node, deg_lat, dix_lat, cent_lat, mil_lat, deg_lon, dix_lon, cent.value AS cent_lon, mil "
                         "MATCH (node)-[:LON]->(mil) "
                         "RETURN deg_lat, dix_lat, cent_lat, mil_lat, deg_lon, dix_lon, cent_lon, mil.value AS mil_lon, avg(node.count) AS count ")
    # Create zone array using result of the query
    squares = []
    for record in result:
        lat = record['deg_lat'] + record['dix_lat']/10. + record['cent_lat']/100. + record['mil_lat']/1000.
        lon = record['deg_lon'] + record['dix_lon']/10. + record['cent_lon']/100. + record['mil_lon']/1000.
        count = record['count']
        squares.append({"lat_max":lat, "lon_min":lon, "count":count, "start":start, "end":end})
    # Close connection
    session.close()
    return squares

def squares_get(lat_max, lat_min, lon_max, lon_min, start, end):
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

    :rtype: List[Square]
    """

    return 'do some magic!'


def squares_post(timestamp, zones):
    """
    Create squares
    Create new squares.
    :param timestamp: Timestamp to which the counts were made.
    :type timestamp: int
    :param zones: Array of zones and associated counts.
    :type zones: list | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        zones = [Zone.from_dict(d) for d in connexion.request.get_json()]
        # Open connexion with Neo4j db
        driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "arthur"))
        session = driver.session()
        # Create new squares
        for zone in zones:
            add_square(session, timestamp, zone.lat_max, zone.lon_min, zone.count).consume().counters
        # Close connection
        session.close()
    return "todo"


def add_square(session, timestamp, lat, lon, count):
    """ Add a small square in the graph database. """

    deg_lat, dix_lat, cent_lat, mil_lat = decompose(lat)
    deg_lon, dix_lon, cent_lon, mil_lon = decompose(lon)

    res = session.run("MERGE (lat:LatTreeRoot) "
                "WITH lat "
                "MERGE (lat)-[:CHILD]->(deg:Degre {value:toInteger("+str(deg_lat)+")}) "
                "WITH deg "
                "MERGE (deg)-[:CHILD]->(dix:Dixieme {value:toInteger("+str(dix_lat)+")}) "
                "WITH dix "
                "MERGE (dix)-[:CHILD]->(cent:Centieme {value:toInteger("+str(cent_lat)+")}) "
                "WITH cent "
                "MERGE (cent)-[:CHILD]->(mil_lat:Millieme {value:toInteger("+str(mil_lat)+")}) "
                "WITH mil_lat "
                "MERGE (lon:LonTreeRoot) "
                "WITH mil_lat, lon "
                "MERGE (lon)-[:CHILD]->(deg:Degre {value:toInteger("+str(deg_lon)+")}) "
                "WITH mil_lat, deg "
                "MERGE (deg)-[:CHILD]->(dix:Dixieme {value:toInteger("+str(dix_lon)+")}) "
                "WITH mil_lat, dix "
                "MERGE (dix)-[:CHILD]->(cent:Centieme {value:toInteger("+str(cent_lon)+")}) "
                "WITH mil_lat, cent "
                "MERGE (cent)-[:CHILD]->(mil_lon:Millieme {value:toInteger("+str(mil_lon)+")}) "
                "WITH mil_lat, mil_lon "
                "CREATE (mil_lat)<-[:LAT]-(n:Square {count:toInteger("+str(count)+")})-[:LON]->(mil_lon) "
                "WITH n "
                "CALL ga.timetree.events.attach({node: n, time: toInteger("+str(timestamp)+"), resolution: 'Minute', relationshipType: 'TIME'}) "
                "YIELD node RETURN node")
    return res

def decompose(nb):
    """ Returns a tuple containing the decomposed latitude or longitude. """

    ent = math.floor(nb)
    dix = math.floor(nb*10%10)
    cent = math.floor(nb*100%10)
    mil = math.floor(nb*1000%10)

    return (ent, dix, cent, mil)
