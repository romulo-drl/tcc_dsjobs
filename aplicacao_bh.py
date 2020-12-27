# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 20:34:30 2020

@author: romul
"""

import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/romul/Desktop/tcc_dsjobs/chromedriver"

df = gs.get_jobs('analista de dados', 15, False, path, 15)
