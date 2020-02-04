from settingsd.display import *

def test_layout_returns_config():
    layout = Layout()
    layout.add_display("LG", 2, 0, 0)
    layout.add_display("laptop", 3, 0, 1200)

    expected = {
        'LG': { 'scale': 2, 'x': 0, 'y': 0 },
        'laptop': { 'scale': 3, 'x': 0, 'y': 1200 }
    }

    assert(layout.config() == expected)
