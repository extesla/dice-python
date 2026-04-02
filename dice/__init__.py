import logging

#: Initialize the root level logging...
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

#: Expose the core library functions here so that all someone needs to do is
#: "import dice" to get them.
from .roll import roll
