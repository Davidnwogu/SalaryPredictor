#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 19:44:37 2021

@author: dav3
"""
import glassdoor_scraper as gs
import pandas as pd

path = "/Users/dav3/Dev/SalaryPredictor/chromedriver"

df = gs.get_jobs('data scientist', 1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv')