from unittest.mock import patch, mock_open
from json import dumps

from settingsd.display.arrangement import Arrangement
from settingsd.display.layout import Layout

@patch('builtins.open', new_callable=mock_open)
def test_arrangement_find_layout_creates_layout_when_not_found(_mo):
    arrangement = Arrangement()
    result = arrangement.find_or_create([('missing_a', 1920, 1080), ('missing_b', 1920, 1080)])
    assert result.displays[0].name == 'missing_a'
    assert result.displays[0].x == 0
    assert result.displays[0].y == 0
    assert result.displays[0].enabled
    assert result.displays[0].primary
    assert result.displays[1].name == 'missing_b'
    assert result.displays[1].x == 1920
    assert result.displays[1].y == 0
    assert result.displays[1].enabled
    assert not result.displays[1].primary

def test_arrangement_finds_monitors():
    layout_a = Layout()
    layout_a.add_display("LG", 2, 0, 0, True, True)
    layout_a.add_display("laptop", 3, 0, 1200, True, False)

    layout_b = Layout()
    layout_b.add_display("laptop", 3, 0, 0, True, True)

    arrangement = Arrangement()
    arrangement.add_layout(layout_a)
    arrangement.add_layout(layout_b)

    result_a = arrangement.find_layout([('LG', 0, 0), ('laptop', 0, 0)])
    assert result_a == layout_a

    result_b = arrangement.find_layout([('laptop', 0, 0), ('LG', 0, 0)])
    assert result_b == layout_a

    result_c = arrangement.find_layout([('laptop', 0, 0)])
    assert result_c == layout_b

TEST_DATA = [
    [
        {
            "name": "test",
            "scale": 1,
            "x": 10,
            "y": 20,
            "enabled": True,
            "primary": True
        },
    ]
]

@patch('os.path.exists')
@patch('builtins.open', new_callable=mock_open, read_data=dumps(TEST_DATA))
def test_load_loads_arrangments_from_file(_mm, _mm2):
    arrangement = Arrangement()
    arrangement.load()
    result = arrangement.find_layout([('test', 0, 0)])
    assert result.displays[0].name == 'test'
    assert result.displays[0].scale == 1
    assert result.displays[0].x == 10
    assert result.displays[0].y == 20
    assert result.displays[0].enabled is True
    assert result.displays[0].primary is True
