from concurrent.futures import Executor, ThreadPoolExecutor
import logging
import time


class Interval:
    tobe_continue=True
    cnt=0
    executor=None
    future=None

    def __init__(self):
        logging.basicConfig(format='[%(threadName)s] %(levelname)s:%(message)s', level=logging.DEBUG)
        logging.debug('INTERVAL init')

    def __del__(self):
        self.executor.shutdown()
        logging.debug('INTERVAL delete')    

    def interval_thread(self):
        logging.debug('run')
        try:
            with ThreadPoolExecutor(max_workers=1) as self.executor:
                self.future = self.executor.submit(self.ping)
            while not self.future.done() :
                time.sleep(1)
        except KeyboardInterrupt:
            logging.debug('get cancel')


    def ping(self):
        logging.debug('start ping')
        while(self.tobe_continue):
            try: 
                logging.debug(self.cnt)
                self.cnt+=1         
                time.sleep(1)
            except(KeyboardInterrupt):
                logging.debug('interval canceled')
                self.tobe_continue=False
                self.future.cancel()
                break
            except Exception as e:
                logging.debug(e)
                break
        logging.debug('end of ping')


if __name__ == '__main__':
    print('run from console')
    try:
        interval =Interval()
        interval.interval_thread()
    except KeyboardInterrupt:
        print('cancel from console')
        interval.tobe_continue=False
        interval.future.cancel()

        
