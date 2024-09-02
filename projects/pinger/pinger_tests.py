#!/usr/bin/env python3

import unittest
from pinger import parseping


class TestPinger(unittest.TestCase):
    def test_parseping(self):
        line = '''PING yandex.ru (5.255.255.77) 56(84) bytes of data.
64 bytes from yandex.ru (5.255.255.77): icmp_seq=1 ttl=237 time=78.9 ms
64 bytes from yandex.ru (5.255.255.77): icmp_seq=2 ttl=237 time=74.0 ms
64 bytes from yandex.ru (5.255.255.77): icmp_seq=3 ttl=237 time=80.6 ms
64 bytes from yandex.ru (5.255.255.77): icmp_seq=4 ttl=237 time=72.2 ms

--- yandex.ru ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 72.166/76.403/80.592/3.447 ms'''
        
        flag, rtt = parseping(line)
        self.assertEqual(flag, '1')
        self.assertEqual(rtt, '76.403')

    '''PING 10.10.10.1 (10.10.10.1) 56(84) bytes of data.

--- 10.10.10.1 ping statistics ---
4 packets transmitted, 0 received, 100% packet loss, time 3107ms'''
        
if __name__ == '__main__':
    unittest.main()