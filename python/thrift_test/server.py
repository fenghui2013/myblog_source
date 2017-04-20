import sys

sys.path.append('gen-py')

from tutorial import Calculator
from tutorial.ttypes import InvalidOperation, Operation
from shared.ttypes import SharedStruct

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class CalculatorHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print('ping...')

    def add(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        print('%d-%d=%d' % (n1, n2, n1-n2))

if __name__ == '__main__':
    handler = CalculatorHandler()
    processor = Calculator.Processor(handler)
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print('server is running ...')
    server.serve()
    print('done')
