import sys

sys.path.append('gen-py')

from tutorial import Calculator
from tutorial.ttypes import InvalidOperation, Operation
from shared.ttypes import SharedStruct

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.server.TNonblockingServer import TNonblockingServer

class CalculatorHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print('ping...')

    def add(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        print('%d-%d=%d' % (n1, n2, n1-n2))

#class MyServer(TNonblockingServer):
#    def __init__(self, processor, lsocket, inputProtocolFactory=None, outputProtocolFactory=None, threads=10):
#        super(TNonblockingServer, self).__init__(processor, lsocket)

    #def close(self):
    #    pass

    #def handler(self):
    #    pass

    #def prepare(self):
    #    pass

    #def serve(self):
    #    pass

    #def wake_up(self):
    #    pass

if __name__ == '__main__':
    handler = CalculatorHandler()
    processor = Calculator.Processor(handler)
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TNonblockingServer(processor, transport)

    server.serve()
