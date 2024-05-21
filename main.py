import logging
import os

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    from instagram_bot import initialize
    initialize()
