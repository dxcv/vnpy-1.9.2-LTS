from vnpy.trader.vtUtility import BarGenerator1
from vnpy.trader.vtObject import VtTickData
from datetime import datetime

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
    
if __name__ == '__main__':
    test_BarGenerator1()
