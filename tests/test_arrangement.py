from unittest.mock import patch, mock_open
from json import dumps

from settingsd.display.arrangement import Arrangement
from settingsd.display.layout import Layout

def test_arrangement_finds_monitors():
    layout_a = Layout()
    layout_a.add_display("LG", 2, 0, 0, True, True)
    layout_a.add_display("laptop", 3, 0, 1200, True, False)

    layout_b = Layout()
    layout_b.add_display("laptop", 3, 0, 0, True, True)

    arrangement = Arrangement()
    arrangement.add_layout(layout_a)
    arrangement.add_layout(layout_b)

    result_a = arrangement.find_layout(['LG', 'laptop'])
    assert result_a == layout_a

    result_b = arrangement.find_layout(['laptop', 'LG'])
    assert result_b == layout_a

    result_c = arrangement.find_layout(['laptop'])
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
def test_from_file_loads_arrangments_from_file(_mm, _mm2):
    arrangement = Arrangement.from_file('monitors.json')
    result = arrangement.find_layout(['test'])
    assert result.displays[0].name == 'test'
    assert result.displays[0].scale == 1
    assert result.displays[0].x == 10
    assert result.displays[0].y == 20
    assert result.displays[0].enabled is True
    assert result.displays[0].primary is True

def test_from_file_returns_empty_if_file_doesnt_exist():
    arrangement = Arrangement.from_file('not_there.json')
    assert arrangement is not None
