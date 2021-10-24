from math import inf

from .certificate import Certificate
from .element import Element


def create_certificate(element_1: Element, element_2: Element) -> Certificate:
    expired_certificate = Certificate(inf, element_1.id)

    if element_1.speed == element_2.speed:
        return expired_certificate

    delta_x0 = element_2.x0 - element_1.x0

    if delta_x0 <= 0:
        return expired_certificate

    delta_speed = element_1.speed - element_2.speed
    expiration_time = delta_x0 / delta_speed

    return Certificate(expiration_time, element_1.id)
