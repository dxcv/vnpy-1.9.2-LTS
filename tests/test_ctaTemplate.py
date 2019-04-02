from vnpy.trader.app.ctaStrategy.ctaTemplate import ExtTemplate
from vnpy.trader.vtObject import VtTradeData
from vnpy.trader.vtConstant import *

def test_ExtTemplate():
    t = ExtTemplate(object, {})
    trade1 = VtTradeData()
    trade1.price = 1.001
    trade1.offset = OFFSET_OPEN
    t.onTrade(trade1)
    assert abs(1.001-t.entryPrice) < 0.01
    assert t.exitPrice is None

    trade2 = VtTradeData()
    trade2.price = 2.001
    trade2.offset = OFFSET_CLOSE
    t.onTrade(trade2)
    assert abs(2.001-t.exitPrice) < 0.01
    assert t.entryPrice is None
    


if __name__ == '__main__':
    test_ExtTemplate()
