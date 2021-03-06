import time
class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)

c = CountdownTask()

from threading import Thread
t = Thread(target=c.run, args=(10,))
t.start()
c.terminate() # Signal termination 信號終止
t.join()      # Wait for actual termination (if needed) 實際停止