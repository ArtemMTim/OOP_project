from unittest.mock import patch

from src.utils import data_from_json, objects_from_data


@patch("json.load")
def test_data_from_json(mock_json_load, json_data):
    mock_json_load.return_value = json_data
    assert data_from_json("products.json") == json_data


def test_objects_from_data_init(json_data):
    objects = objects_from_data(json_data)
    assert objects[0].name == "Смартфоны"
    assert objects[1].name == "Телевизоры"
    assert (
        objects[1].description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
