from vnpy.trader.vtFunction import inTimeRange

def test_inTimeRange():
    from datetime import time
    timeRange = [['9:00:00','10:15:00'],
                 ['10:30:00','11:30:00'],
                 ['13:30:00','15:00:00'],
                 ['21:00:00','23:00:00'],
                ]

    now = time(8,59,59)
    assert inTimeRange(now, timeRange) == False
    now = time(9,0,0)
    assert inTimeRange(now, timeRange) == True
    now = time(10,16,0)
    assert inTimeRange(now, timeRange) == False
    now = time(23,0,1)
    assert inTimeRange(now, timeRange) == False

if __name__ == '__main__':
    test_inTimeRange()
