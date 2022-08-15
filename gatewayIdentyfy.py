import requests
z = 0
while z < 256:
    y = 0
    while y < 256:
        ip = 'http://10.10.' + str(z) + '.' + str(y) + '/'
        print('Trying to connect: {} : '.format(ip), end="")
        try:
            x = requests.get(ip, timeout=1.5)
            print(x.status_code)
        except:
            print("Timeout")
        y += 1
    z += 1
