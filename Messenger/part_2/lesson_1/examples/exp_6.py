# Пинг ресурса

from subprocess import Popen, PIPE


def ping_ip(ip_address):
    args = ['ping', ip_address]
    reply = Popen(args, stdout=PIPE, stderr=PIPE)

    print(reply)
    CODE = reply.wait(5)
    if CODE == 0:
        return True, reply.stdout
    else:
        return False, reply.stderr


print(ping_ip('192.168.1.1'))
print(ping_ip('a'))
