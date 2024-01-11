from pyalgotrading.algobulls import AlgoBullsConnection
from pyalgotrading.strategy import *

from datetime import datetime

class StrategyEMARegularOrder(StrategyBase):
    name = 'EMA Regular Order Strategy'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.timeperiod1 = self.strategy_parameters['TIMEPERIOD1']
        self.timeperiod2 = self.strategy_parameters['TIMEPERIOD2']

        self.main_order_map = None


if __name__ == '__main__':
    dt1 = datetime.now()
    print(f'Approach #1: {dt1}')
    print(f'Year: {dt1.year}')
    print(f'Month: {dt1.month}')
    print(f'Day: {dt1.day}')
    print(f'Hours: {dt1.hour}')
    print(f'Minutes: {dt1.minute}')
    print(f'Seconds: {dt1.second}')
    print(f'Microseconds: {dt1.microsecond}')
    print(f'Timezone: {dt1.tzinfo}')
    print(f"Date: {dt1.date()}")
    print(f"Type: {type(dt1.date())}")
    print(f"Time: {dt1.time()}")
    print(f"Type: {type(dt1.time())}")

    dt2 = datetime(year=2021, month=1, day=1)
    print(f'Approach #2: {dt2}')
    print(f'Year: {dt2.year}')
    print(f"Date: {dt2.date()}") 
    print(f"Type: {type(dt2.date())}")
    print(f"Time: {dt2.time()}")
    print(f"Type: {type(dt2.time())}")
