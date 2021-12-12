## Apache build guide

```
./buildconf

mkdir -p ../workspace/http-2.4.51/datadir

./configure --prefix=`realpath ../workspace/http-2.4.51` --datadir=`realpath ../workspace/http-2.4.51/datadir`

make -j

make install
```

Edit conf, replace "listen 80" into "listen 10080". Thus we don't need root access to run.
Set ServerName to localhost:10080

## Benchmark guide

Apache benchmark client is called ab, which is placed in  `realpath ../workspace/http-2.4.51`

```
/usr/bin/time -a ./bin/ab -n 1000000 -c 500 http://localhost:10080/
```

(Don't forget trailing / in url)

Trick: You can install ab with system package manager to save the hassle of using compiled ab.

### How to test time

Test ab rather than httpd itself. We could use /usr/bin/time ab ... to calculate time.

```
Server Software:        Apache/2.5.1-dev
Server Hostname:        localhost
Server Port:            10080

Document Path:          /
Document Length:        191 bytes

Concurrency Level:      500
Time taken for tests:   37.248 seconds
Complete requests:      1000000
Failed requests:        0
Total transferred:      439000000 bytes
HTML transferred:       191000000 bytes
Requests per second:    26847.01 [#/sec] (mean)
Time per request:       18.624 [ms] (mean)
Time per request:       0.037 [ms] (mean, across all concurrent requests)
Transfer rate:          11509.61 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    9   1.0      9      17
Processing:     2   10   1.8     10     105
Waiting:        1    8   1.8      7     101
Total:         12   19   2.0     18     106

Percentage of the requests served within a certain time (ms)
  50%     18
  66%     19
  75%     19
  80%     20
  90%     20
  95%     21
  98%     22
  99%     23
 100%    106 (longest request)
```

## How to test memory overhead

httpd server won't auto exit after running. Use the following to 
cat /proc/self/status|grep VmSize


## How to safely kill httpd

```
./httpd -k stop
```

## How to run http with single process

Run with `http -X` to enable single process mode.

## Reference

https://httpd.apache.org/docs/current/install.html
