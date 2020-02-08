from settingsd.display.layout import Layout

def test_layout_returns_config():
    layout = Layout()
    layout.add_display("LG", 2, 0, 0, True, True)
    layout.add_display("laptop", 3, 0, 1200, True, False)

    expected = {
        'LG': (0, 0, 2, True, True),
        'laptop': (0, 1200, 3, True, False)
    }

    assert layout.config() == expected
