from ipaddress import ip_address
from task1 import host_ping


def host_range_ping():
    while True:
        start_ip = input('Введите адрес: ')
        try:
            las_oct = int(start_ip.split('.')[3])
            break
        except Exception as e:
            print(e)
    while True:
        end_ip = input('Сколько адресов проверить: ')
        if not end_ip.isnumeric():
            print('Нобходимо ввести число')
        else:
            if (las_oct + int(end_ip)) > 254:
                print(
                    f'Можем менять только последний октет, т.е. максимальное число хостов для проверки {254 - las_oct}')
            else:
                break

    host_list = []

    [host_list.append(str(ip_address(start_ip) + x)) for x in range(int(end_ip))]
    return host_ping(host_list)


if __name__ == "__main__":
    host_range_ping()
