import tracemalloc


class MemoryMonitor:

    def start(self):
        tracemalloc.start()

    def stop(self):
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        return peak / 1024 / 1024