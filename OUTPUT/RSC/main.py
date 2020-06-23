import pandas as pd
import matplotlib
import sys
import os
import DataAnalysis
import Parser
import plotly.express as px


def main():
 args = Parser.parser()
 data = DataAnalysis.user_request(args.sp, args.info)
 print(data)
    
      
if __name__ == '__main__':
  main()