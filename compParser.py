import polars as pl 
import pandas as pd 
import numpy as np 
from colorama import Fore, Style
import dill 

class compParser():
      def __init__(self)-> None:
            pass 
      def PrintColor(self,
                     text:str='',
                     color = Fore.RED
                     ) -> None:
            print(color + text + Style.RESET_ALL)   
      def pickleDump(self, obj, path:str)-> None:
            with open(path, mode='wb') as f:
                  dill.dump(obj, f, protocol=4)
      def pickleLoad(self, path:str)-> None:
            with open(path, mode='rb') as f:
                  return dill.load(f)
      def reduce_mem_usage(self, 
                  df:pd.DataFrame,
                  float16_as32:bool=True)->pd.DataFrame:
            start_mem = df.memory_usage().sum() / 1024**2
            print('Memory usage of dataframe is {:.2f} MB'.format(start_mem))
            for col in df.columns:
                  col_type = df[col].dtype
                  if col_type != object and str(col_type)!='category':
                        c_min,c_max = df[col].min(),df[col].max() #
                        if str(col_type)[:3] == 'int':
                        
                              if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                                    df[col] = df[col].astype(np.int8)
                              elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                                    df[col] = df[col].astype(np.int16)
                              elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                                    df[col] = df[col].astype(np.int32)
                              elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                                    df[col] = df[col].astype(np.int64)  
                        else:
                              if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                                    if float16_as32:
                                          df[col] = df[col].astype(np.float32)
                                    else:
                                          df[col] = df[col].astype(np.float16)
                              elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                                    df[col] = df[col].astype(np.float32)
                              else:
                                    df[col] = df[col].astype(np.float64)
            #calculate memory after optimization
            end_mem = df.memory_usage().sum() / 1024**2
            print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
            print('Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))
            return df