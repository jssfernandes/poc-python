from builtins import print
from multiprocessing.dummy import Pool
import requests
import json
import time

# Creates a pool with ten threads; more threads = more concurrency.
# "pool" is a module attribute; you can be sure there will only
# be one of them in your application
# as modules are cached after initialization.
pool = Pool(10)
start_time = time.time()

if __name__ == '__main__':
    futures = []
    for x in range(1, 152):
        futures.append(pool.apply_async(requests.get, [f'https://pokeapi.co/api/v2/pokemon/{x}']))
    # futures is now a list of 10 futures.
    for future in futures:
        # For each future, wait until the request is
        # finished and then print the response object.
        # print(future.get())
        pokemon = json.loads(future.get().text)
        print(pokemon['name'])
    # print(futures[0].get().text)
print("--- %s seconds ---" % (time.time() - start_time))