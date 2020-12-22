# Асинхронный пинг

import asyncio

from sys import exit, platform
from ipaddress import ip_address, IPv4Address, IPv6Address
from tabulate import tabulate
from itertools import repeat


class AsyncPingHosts:
    # Инициализация
    def __init__(self, addresses):
        """
        Инициализация кросс-платформенной асинхронной пинг-машины
        :param addresses:
        """

        # пингуемые адреса
        self.addresses = addresses
        # доступные из них
        self.reachable = list()
        # недоступные
        self.unreachable = list()

        self._set_addresses_type()

    def _set_addresses_type(self):
        """
        Установить тип адресов в значение ipaddress.IPv4Address или ipaddress.IPv6Address,
        если в качестве аргумента адресов указан список.
        sys.exit(1) - выход, если перехвачено исключение ValueError
        :return:
        """
        try:
            if self._is_addresses_is_list():
                self.addresses = [self._set_address_type(address) for address in self.addresses]
        except ValueError as error:
            print(error)
            exit(1)

    def _is_addresses_is_list(self):
        """
        Валидация объекта - список адресов. True, если переданный объект является списком, иначе вывести ValueError
        :return:
        """
        if type(self.addresses) is list:
            return True
        raise ValueError(f'Passed addresses must be a list type. {type(self.addresses)} given.')

    @staticmethod
    def _set_address_type(address):
        """
        Установите типа адреса ipaddress.IPv4Address или ipaddress.IPv6Address
        :param address:
        :return:
        """
        if not type(address) in (IPv4Address, IPv6Address):
            try:
                address = ip_address(address)
            except ValueError as error:
                print(error)
                exit(1)
        return address

    def ping_hosts(self):
        """
        Межплатформенный асинхронный пинг хоста
        :return:
        """
        print(f'Пожалуйста, подождите, пока не закончится пинг. Нужно около 5 сек если все адреса доступны.'
              f'Около 20 сек или более в противном случае. В зависимости от количества переданных адресов.')

        if platform == 'win32':
            loop = asyncio.ProactorEventLoop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self._async_ping())
            loop.close()
        else:
            asyncio.run(self._async_ping())

    async def _async_ping(self):
        # Получить задачи и запускать их одновременно
        task = (self._ping_host(str(address)) for address in self.addresses)
        await asyncio.gather(*task)

    async def _ping_host(self, address):
        # Проверить связь с хостом и добавить его в список доступных или недоступных на основе кода возврата
        ping_key = self._get_ping_key()
        proc = await asyncio.create_subprocess_shell(
            f'ping {ping_key} 4 {address}', stdout=asyncio.subprocess.DEVNULL
        )
        await proc.communicate()
        if proc.returncode == 0:
            self.reachable.append(address)
        else:
            self.unreachable.append(address)

    @staticmethod
    def _get_ping_key():
        # Получить ключ для команды ping, которая устанавливает количество отправляемых пакетов
        key = '-c'
        if platform == 'win32':
            key = '/n'
        return key

    def get_ping_status_table(self):
        # Получить таблицу с адресами и их статусами
        headers = ['Address', 'Status']
        reachable = list(zip(self.reachable, repeat('reachable')))
        unreachable = list(zip(self.unreachable, repeat('unreachable')))
        return tabulate(reachable + unreachable, headers, tablefmt='github')


if __name__ == '__main__':
    FROM_ADDR = ip_address('192.168.1.1')
    TO_ADDR = ip_address('192.168.1.2')

    ADDRESSES = [FROM_ADDR + i for i in range(int(TO_ADDR) - int(FROM_ADDR) + 1)]

    ping = AsyncPingHosts(ADDRESSES)
    ping.ping_hosts()
    print(ping.get_ping_status_table())
