from vnpy.trader.vtUtility import (BarGenerator1,
                                  Callback
                                  )
from vnpy.trader.vtObject import VtTickData
from datetime import datetime, time, timedelta

def test_BarGenerator1():
    def onBar(bar):
        assert bar.datetime == datetime(2019,1,1,9,0,0)
        assert bar.volume == 2
    bg = BarGenerator1(onBar, interval='40s')
    tick1 = VtTickData()
    tick1.datetime = datetime(2019,1,1,9,0,1)
    tick1.volume = 1

    tick2 = VtTickData()
    tick2.datetime = datetime(2019,1,1,9,0,39)
    tick2.volume = 2

    tick3 = VtTickData()
    tick3.datetime = datetime(2019,1,1,9,0,39,500)
    tick3.volume = 3
    
    tick4 = VtTickData()
    tick4.datetime = datetime(2019,1,1,9,2,1)
    tick4.volume = 4
    
    bg.updateTick(tick1)
    bg.updateTick(tick2)
    bg.updateTick(tick3)
    bg.updateTick(tick4)
    assert bg.bar.datetime == datetime(2019,1,1,9,2,0)

def test_Callback():
    global g
    g = False
    def funcAt():
        global g
        g = True

    def funcAt1(x, y):
        assert x == 1
        assert y == 2

    now = datetime(2019,1,1,9,0,0)
    delta = timedelta(seconds=5)
    at = (now + delta).time()
    cb = Callback()
    cb.callbackAt(at, funcAt)
    cb.callbackAt(at, funcAt1, 1, 2)
    cb.updateTime(time(9,0,1))
    assert g == False
    cb.updateTime(time(9,0,5))
    assert g == True


if __name__ == '__main__':
    test_Callback()
