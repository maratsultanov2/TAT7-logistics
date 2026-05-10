import logging

log = logging.getLogger("tat7_logistics")
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)
log.setLevel(logging.INFO)
