from re import sub


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


calculate = calIP("192.168.1.2", "255.255.255.0")

calculate.calBroadAddr()
