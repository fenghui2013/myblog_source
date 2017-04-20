import sys

sys.path.append('gen-py')

from tutorial import Calculator
from tutorial.ttypes import InvalidOperation, Operation, Work

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def main():
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    client = Calculator.Client(protocol)

    transport.open()

    client.ping()
    sum_ = client.add(1, 1)
    print("1+1=%d" % sum_)
    
    client.sub(2, 1)

    transport.close()

if __name__ == '__main__':
    main()
