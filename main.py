from calculate import calIP

ip = input("Enter Device IP: ")
subnet = input("Enter Subnetmask: ")
calculate = calIP(ip, subnet)

calculate.printOutput()
