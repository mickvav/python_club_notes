## pinger service

write a program, that takes a file with networks, e.g.:

```
10.0.0.0/24
192.168.0.0/16
```

_randomly_ pings ip addresses from them and saves result summaries in another file, so it looks like

```
pinger input.txt output.txt
```



```
10.0.0.10 1 14.2
192.168.1.3 0 0
192.168.20.30 1 33.4
```

"1" means pingable
"0" means unreachable
14.2 means 14.2 ms
33.4 means 33.4 ms of _average_ ping rtt.
