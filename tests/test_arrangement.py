from settingsd.display import *

def test_arrangement_finds_monitors():
    layoutA = Layout()
    layoutA.add_display("LG", 2, 0, 0)
    layoutA.add_display("laptop", 3, 0, 1200)

    layoutB = Layout()
    layoutB.add_display("laptop", 3, 0, 0)
    
    arrangement = Arrangement()
    arrangement.add_layout(layoutA)
    arrangement.add_layout(layoutB)

    resultA = arrangement.find_layout(['LG', 'laptop'])
    assert(resultA == layoutA)

    resultB = arrangement.find_layout(['laptop', 'LG'])
    assert(resultB == layoutA)

    resultC = arrangement.find_layout(['laptop'])
    assert(resultC == layoutB)