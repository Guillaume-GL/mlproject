from mlproject.lib import hello_world
from mlproject.distance import haversine


def test_length_of_hello_world():
    assert len(hello_world()) != 0


def test_haversine():
    assert haversine(48.865070, 2.380009, 48.235070, 2.393409) == \
    70.00789153218594
