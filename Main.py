# Start The Log
import logging
from datetime import datetime
from StartUp.Start_Up import first_run

log_name = datetime.now().strftime('Logs/%d_%m_%Y_%H_%M.log')

logging.basicConfig(filename=log_name, level=logging.DEBUG, format='%(asctime)s %(name)s ----%(message)s----',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
log = logging.getLogger(__name__)
log.info('Log Started')
# Run Start Up Script
log.info('First Run Called')
firstrun = first_run()
log.info('First Run Successfully Run')
if first_run() > 0:
    log.info('Shut Down Program')



