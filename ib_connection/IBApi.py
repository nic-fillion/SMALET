from ibapi.client import EClient
from ibapi.wrapper import EWrapper

class IBApi(EWrapper, EClient):
    def __init__(self):
        EWrapper.__init__(self)
        EClient.__init__(self, self)

    def tickPrice(self, reqId, tickType, price, attrib):
        print(reqId)
        print(tickType)
        print(price)
	    
        if tickType == 2 and reqId == 1:
            print('The current ask price is: ', price)