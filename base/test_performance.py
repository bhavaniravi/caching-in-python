import random
import requests
URL = "http://127.0.0.1:5000/user/user00{i}"

URLs = [URL.format(i=i) for i in range(0, 4)]


def get_response_elapsed_time():
    num = random.randint(0, 3)
    res = requests.get(URLs[num])
    return res.elapsed.total_seconds()


etime = [get_response_elapsed_time() for i in range(1000)]
print (sum(etime)/1000)


# Without DB

# LRU caching - 0.0037427440000000023
# Redis - 0.004498315000000001
# Memcached - 0.003989093000000003

# With DB

# without caching - 0.006189506999999994
# LRU - 0.0032120939999999974
# Redis - 0.003976993000000001
# memcached - 0.004795536000000001



