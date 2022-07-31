class calIP():
    def __init__(self, ip, subnet):
        self.ip = ip.split('.')
        self.subnet = subnet.split('.')
        self.netAddr = ''
        self.broadAddr = ''

    def calNetAddr(self):
        ipBlock = 0
        while ipBlock < 4:
            self.netAddr += str(int(self.subnet[ipBlock])
                                & int(self.ip[ipBlock]))
            if (ipBlock < 3):
                self.netAddr += '.'
            ipBlock += 1
        return self.netAddr

    def calBroadAddr(self):
        ipBlock = 0
        while ipBlock < 4:
            self.broadAddr += str((255 - int(self.subnet[ipBlock]))
                                  | int(self.ip[ipBlock]))
            if (ipBlock < 3):
                self.broadAddr += '.'
            ipBlock += 1
        return self.broadAddr

    def printOutput(self):
        print()
        print('Network Address: {}\nBroadcast Address: {}'.format(
            calIP.calNetAddr(self), calIP.calBroadAddr(self)))
