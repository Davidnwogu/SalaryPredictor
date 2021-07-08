#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 21:13:09 2021

@author: dav3
"""
import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

#salary parsing
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided' in x.lower() else 0)

df = df[df['Salary Estimate'] != "-1"]
salary = df['Salary Estimate'].apply(lambda x:x.split('(')[0])
minus_kd = salary.apply(lambda x:x.replace('K','').replace('$',''))

min_hr = minus_kd.apply(lambda x:x.lower().replace('per hour', '').replace('employer provided salary:', ''))

df['min_salary'] = min_hr.apply(lambda x:int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x:int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary) / 2


#Company name text only
df['company_txt'] = df.apply(lambda x:x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis=1)

#state field

df['job_state'] = df['Location'].apply(lambda x:x[-2:])
df.job_state.value_counts()
df['same_state'] = df.apply(lambda x: 1 if x['Location'] == x['Headquarters'] else 0, axis=1 )

#age of company

df['age'] = df['Founded'].apply(lambda x: x if x < 1 else (2021 - x))

#Parsing Job Description
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['r_studio_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() else 0)
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df['sql_yn'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)


if (1 or 5) > 3:
    print("yes")