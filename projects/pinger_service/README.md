# Pinger as web service

Read through https://realpython.com/api-integration-in-python/ and convert our pinger cli into a web service.

Ideally, as a user, I would like to be able to send http requests like

```
curl https://<host>:<port>/pinger/networks
```
And the service would give me current set of networks that it is configured to be able to ping. For example,
```JSON
["10.0.0.0/24","192.168.0.0/24"]
```
Or, say, 
```
curl https://<host>:<port>/pinger/networks \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '["10.0.0.0/24"]'
```
would replace list of networks.

To initiate actual execution of ping user would be expected to send request like

```
curl https://<host>:<port>/pinger/run \
  -x POST \
  -H 'Content-Type: application/json' \
  -d '{"hosts": 10, "timeout": 1, "repeats": 4}'
```
This will _start_ pinging process that pings 10 hosts, chosen from networks (controlled by /pinger/networks endpoint) randomly, and immediately returns it's identifier to the user:
```JSON
{"run": 1}
```

Nb: all the logic of selection of ip addresses from networks remains the same as in CLI version.

If the user wants to examine the progress of a particular run, they would
```
curl https://<host>:<port>/pinger/run/1
```
And will receive something like
```JSON
{
    "status": "running"
    "results": []
}
```
or 
```JSON
{
    "status": "finished",
    "results": [
        {"host": "10.0.1.2","pingable":true},
        {"host": "10.0.1.3","pingable":false},
        ...
    ]
}
```
If the user wants to see list of all runs, they would run:
```
curl https://<host>:<port>/pinger/run/
```
and receive
```JSON
[1, 2, 3, 4]
```

