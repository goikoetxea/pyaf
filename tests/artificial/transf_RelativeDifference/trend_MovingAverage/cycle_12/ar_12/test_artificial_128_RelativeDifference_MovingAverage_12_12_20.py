import pyaf.Bench.TS_datasets as tsds
import pyaf.tests.artificial.process_artificial_dataset as art




art.process_dataset(N = 128 , FREQ = 'D', seed = 0, trendtype = "MovingAverage", cycle_length = 12, transform = "RelativeDifference", sigma = 0.0, exog_count = 20, ar_order = 12);