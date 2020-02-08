from unittest.mock import patch, mock_open
from json import dumps

from settingsd.display.display import Display
from settingsd.display.arrangement import Arrangement
from settingsd.display.layout import Layout

def test_arrangement_finds_monitors():
    layoutA = Layout()
    layoutA.add_display("LG", 2, 0, 0, True, True)
    layoutA.add_display("laptop", 3, 0, 1200, True, False)

    layoutB = Layout()
    layoutB.add_display("laptop", 3, 0, 0, True, True)

    arrangement = Arrangement()
    arrangement.add_layout(layoutA)
    arrangement.add_layout(layoutB)

    resultA = arrangement.find_layout(['LG', 'laptop'])
    assert(resultA == layoutA)

    resultB = arrangement.find_layout(['laptop', 'LG'])
    assert(resultB == layoutA)

    resultC = arrangement.find_layout(['laptop'])
    assert(resultC == layoutB)

test_data = [
    [
        {
            "name": "test",
            "scale": 1,
            "x": 0,
            "y": 0,
            "enabled": True,
            "primary": True
        },
    ]
]

@patch('builtins.open', new_callable=mock_open, read_data=dumps(test_data))
def test_loads_arrangments_from_file(_mm):
    arrangement = Arrangement.from_file('monitors.json')
    result = arrangement.find_layout(['test'])
    assert(result.displays[0].name == 'test')
    assert(result.displays[0].scale == 1)
    assert(result.displays[0].x == 0)
    assert(result.displays[0].y == 0)
    assert(result.displays[0].enabled == True)
    assert(result.displays[0].primary == True)
