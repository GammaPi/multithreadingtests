## Memcached build guide

```
./autogen.sh
./configure
```
Note: The older version of memcached system autogen version may not support autogen in the system. Try to add system version to the supported list in autogen.sh


## Benchmark guide

### Building test client
We could use  memtier_benchmark to perform benchmark test.
```
git clone https://github.com/RedisLabs/memtier_benchmark.git
cd memtier_benchmark
autoreconf -ivf
./configure
make
make install
```

### Run test
```
./memtier_benchmark -p 11211 -P memcache_binary
```

### How to test time

Use /usr/bin/time on memtier_benchmark

## How to test memory overhead

memcached won't auto exit after running. Use the following to get memory overhead at exit
cat /proc/self/status|grep VmSize


## How to safely kill memcached

Add enable-shutdown [Ref](https://github.com/memcached/memcached/pull/740)
```
./memcached --enable-shutdown
```
To kill
```
echo "shutdown" | nc -q0 localhost 11211
```


## How to run memcached with single process

It is single process by default


## Reference

https://httpd.apache.org/docs/current/install.html
