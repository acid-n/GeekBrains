from ipaddress import ip_address
from subprocess import Popen, PIPE


def host_ping(list_ip_addresses, timeout=10, requests=2):
    results = {'Доступные узлы': "", 'Недоступные узлы': ""}
    for address in list_ip_addresses:
        try:
            address = ip_address(address)
        except ValueError:
            pass
        proc = Popen(f'ping {address} -W {timeout} -c {requests}', shell=True, stdout=PIPE)
        proc.wait()

        if proc.returncode == 0:
            results['Доступные узлы'] += f'{str(address)}\n'
            res_string = f'{address} - узел доступен'
        else:
            results['Недоступные узлы'] += f'{str(address)}\n'
            res_string = f'{address} - узел недоступен'
        print(res_string)
    return results


if __name__ == '__main__':
    ip_addresses = ['yandex.ru', 'google.ru', '8.8.8.8', '192.168.1.1']
    host_ping(ip_addresses)
