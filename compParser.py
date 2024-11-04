import polars as pl 
import pandas as pd 
import numpy as np 
import emoji
import ftfy
import stopwords
import re
from colorama import Fore, Style
import dill 

class compParser():
      def __init__(self) -> None:
            """
            Initializes the compParser object.
            """
            pass 

      def PrintColor(self, text: str = '', color=Fore.RED) -> None:
            """
            Prints the given text in the specified color.

            Parameters:
            text (str): The text to print.
            color: The color to use for printing from colorama.Fore. Default is Fore.RED.
            """
            print(color + text + Style.RESET_ALL)   

      def pickleDump(self, obj, path: str) -> None:
            """
            Serializes an object and saves it to a file using dill.

            Parameters:
            obj: The object to serialize.
            path (str): The file path to save the serialized object.
            """
            with open(path, mode='wb') as f:
                  dill.dump(obj, f, protocol=4)

      def pickleLoad(self, path: str):
            """
            Loads a serialized object from a file using dill.

            Parameters:
            path (str): The file path from which to load the object.

            Returns:
            The deserialized object.
            """
            with open(path, mode='rb') as f:
                  return dill.load(f)

      def reduce_mem_usage(self, df: pd.DataFrame, float16_as32: bool = True) -> pd.DataFrame:
            """
            Reduces memory usage of a pandas DataFrame by downcasting numerical columns.

            Parameters:
            df (pd.DataFrame): The DataFrame to optimize.
            float16_as32 (bool): If True, converts float16 to float32 to avoid potential issues. Default is True.

            Returns:
            pd.DataFrame: The optimized DataFrame with reduced memory usage.
            """
            start_mem = df.memory_usage().sum() / 1024**2
            print('Memory usage of dataframe is {:.2f} MB'.format(start_mem))
            for col in df.columns:
                  col_type = df[col].dtype
                  if col_type != object and str(col_type) != 'category':
                        c_min, c_max = df[col].min(), df[col].max()
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
            end_mem = df.memory_usage().sum() / 1024**2
            print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
            print('Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))
            return df
      
      def clean_text(self,
                     text:str='',
                     language:str='english')->str:
            text = emoji.demojize(text, delimiters=(" ", " "))
            text = ftfy.fix_text(text) # unicode issues
            text = text.lower() 
            html = re.compile(r'<.*?>')
            text = html.sub(r'', text)
            #remove url '\w+':(word character,[a-zA-Z0-9_])
            text=re.sub("http\w+",'',text)
            #remove @  person_name 
            text=re.sub("@\w+",'',text)
            #drop single character,they are meaningless. 'space a space'
            text=re.sub("\s[a-z]\s",'',text)
            #remove number
            text=re.sub("\d+",'',text)
            #drop english stopwords,they are meaningless.
            language_stopwords = stopwords.words(language)
            text_list=text.split(" ")
            text_list=[t for t in text_list if t not in language_stopwords]
            text=" ".join(text_list)
            #drop space front and end.
            text=text.strip()
            return text            
            return text