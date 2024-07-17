from memcache import Client
from typing import Optional
from core.config import MEMCACHED_ENDPOINT, MEMCACHED_PORT


DEFAULT_TTL = 1000
MEMCACHED_CLIENT = Client([f'{MEMCACHED_ENDPOINT}:{MEMCACHED_PORT}'])


class Memcache:
    class MemcachedKeyNoneError(Exception):
        pass

    def __init__(self, client: Client = MEMCACHED_CLIENT) -> None:
        self.client: Client = client

    def set_vars(self, key: str, value: str, time: int = DEFAULT_TTL) -> bool:
        try:
            return self.client.set(key, value, time=time)
        except Exception as e:
            raise Exception(f"Error setting key '{key}': {e}")

    def get_vars(self, key: str) -> Optional[str]:
        try:
            value = self.client.get(key)
            if value is None:
                raise self.MemcachedKeyNoneError(f"Key '{key}' not found in cache.")
            return value
        except self.MemcachedKeyNoneError:
            return None
        except Exception as e:
            raise Exception(f"Error getting key '{key}': {e}")

    def delete(self, key: str) -> bool:
        try:
            return self.client.delete(key)
        except Exception as e:
            raise Exception(f"Error deleting key '{key}': {e}")

    def flush(self) -> bool:
        try:
            return self.client.flush_all()
        except Exception as e:
            raise Exception(f"Error flushing cache: {e}")

    def close(self) -> None:
        try:
            self.client.disconnect_all()
        except Exception as e:
            raise Exception(f"Error disconnecting from Memcached servers: {e}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()