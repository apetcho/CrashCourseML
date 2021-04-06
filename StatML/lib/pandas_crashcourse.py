#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

section = lambda title, n: print(f"\n{'*'*n}\n{title}\n{'*'*n}\n")

# Create DataFrame
title = "Create DataFrame"
section(title, len(title))

columns = ['name', 'age', 'gender', 'job']
user1 = pd.DataFrame([['alice', 19, 'F', 'student'],
                      ['john', 26, 'M', 'student']], columns=columns)
user2 = pd.DataFrame([['eric', 22, 'M', 'student'],
                     ['paul', 58, 'F', 'manager']], columns=columns)
user3 = pd.DataFrame(dict(name=['peter', 'julie'],
                          age=[33, 44],
                          gender=['M', 'F'],
                          job=['engineer', 'scientist']))
print(f"\nuser1:\n{user1}")
print(f"\nuser2:\n{user2}")
print(f"\nuser3:\n{user3}")

## Combining DataFrames
title = "Combining DataFrame"
section(title, len(title))

## -- Concatenate DataFrames
title = "Concatenate DataFrames"
section(title, len(title))

users = user1.append(user1)
print(f"users = user1.append(user2):\n\n{users}\n")

users = pd.concat([user1, user2, user3])
print(f"users = pd.concat([user1, user2, user3]):\n\n{users}\n")

## -- Join DataFrames
title = "Join DataFrames"
section(title, len(title))

user4 = pd.DataFrame(dict(name=['alice', 'john', 'eric', 'julie'],
                          height=[165, 180, 175, 171]))
print(f"user4:\n\n{user4}\n")

merge_inter = pd.merge(users, user4, on='name')
print(f"\nmerge_inter = pd.merge(users, user4, on='name'):\n{merge_inter}\n")

users = pd.merge(users, user4, on='name', how='outer')
print(f"\nusers = pd.merge(users, user4, on='name', how='outer')\n{users}\n")

## -- Reshaping by pivoting
title = "Reshaping by pivoting"
section(title, len(title))
staked = pd.melt(users, id_vars='name', var_name='variable', value_name='value')
print(f"\nstaked = pd.melt(users, id_vars='name', var_name='variable', value_name='value')\n{staked}\n")

print(f"staked.pivot(index='name', columns='variable', values='value')\n"
      f"{staked.pivot(index='name', columns='variable', values='value')}\n")

## Summarizing
title = "Summarizing"
section(title, len(title))
print(f"users:\n{users}\n\n")
print(f"type(users)\n{users}\n\n")
print(f"users.head()\n{users.head()}\n\n")
print(f"users.tail()\n{users.tail()}\n\n")
print(f"users.index\n{users.index}\n\n")
print(f"users.columns\n{users.columns}\n\n")
print(f"users.dtypes\n{users.dtypes}\n\n")
print(f"users.shape\n{users.shape}\n\n")
print(f"users.values\n{users.values}\n\n")
print(f"users.info()\n\n{users.info()}\n\n")

## Columns selection
title = "Columns selection"
section(title, len(title))
print(f"users['gender']\n{users['gender']}\n\n")
print(f"type(users['gender'])\n{type(users['gender'])}\n\n")
print(f"users.gender\n{users.gender}\n\n")
print(f"users[['age', 'gender']]\n{users[['age', 'gender']]}\n\n")
my_cols = ['age', 'gender']
print(f"my_cols = ['age'. 'gender']\ntype(users[my_cols])\n{type(users[my_cols])}\n\n")

## Rows selection (basic)
title = "Basic rows selection"
section(title, len(title))

df = users.copy()
print(f"df = users.copy()\n{df}\n\n")
print(f"df.iloc[0]\n{df.iloc[0]}\n\n")
print(f"df.iloc[0, 0]\n{df.iloc[0, 0]}\n\n")
df.iloc[0, 0] = 55
print(f"df.iloc[0, 0] = 55\n{df}\n\n")
for i in range(users.shape[0]):
    row = df.iloc[i]
    row.age *= 10
    
print("After looping over rows")
print(f"df\n{df}\n\n")

## Rows selection (filtering)
title = "Rows selection (filtering)"
section(title, len(title))

print(f"users[users.age < 20]\n{users[users.age < 20]}\n\n")
young_bool = users.age < 20
young = users[young_bool]
young_job = young.job
print(f"young_bool = users.age < 20\n{young_bool}\n")
print(f"young = users[young_bool]\n{young}\n\n")
print(f"young_job = young.job\n{young_job}\n\n")

## Sorting
title = "Sorting"
section(title, len(title))

df = users.copy()
print(f"df = users.copy()\n{df}\n\n")
print(f"df.age.sort_values()\n{df.age.sort_values()}\n\n")
print(f"df.sort_values(by='age')\n{df.sort_values(by='age')}\n\n")
print(f"df.sort_values(by='age', ascending=False)\n{df.sort_values(by='age', ascending=False)}\n\n")
df.sort_values(by=['job', 'age'], inplace=True)
print(f"df.sort_values(by=['job', 'age'], inplace=True)\n{df}\n\n")


## Descriptive statistics
title = "Descriptive statistics"
section(title, len(title))
print(f"df.describe()\n{df.describe()}\n\n")
print(f"df.describe(include='all')\n{df.describe(include='all')}\n\n")
print(f"df.describe(include=['object'])\n{df.describe(include=['object'])}\n\n")
print(f"df.groupby('job').mean()\n{df.groupby('job').mean()}\n\n")
print(f"df.groupby('job')['age'].mean()\n{df.groupby('job')['age'].mean()}\n\n")
print(f"df.groupby('job').describe(include='all')\n{df.groupby('job').describe(include='all')}\n\n")
print("\nGouby in a loop\n\n")
for grp, data in df.groupby('job'):
    print(grp, data)


## Quality check
title = "Quality check"
section(title, len(title))
##-- Remove duplicate data
title = "--- Remove duplicate data ---"
section(title, len(title))
df = users.append(df.iloc[0], ignore_index=True)
print(f"df = users.append(df.iloc[0], ignore_index=True)\n{df}\n\n")
print(f"df.duplicated()\n{df.duplicated()}\n\n")
print(f"df.duplicated().sum()\n{df.duplicated().sum()}\n\n")
print(f"df[df.duplicated()]\n{df[df.duplicated()]}\n\n")
print(f"df.age.duplicated()\n{df.age.duplicated()}\n\n")
print(f"df.duplicated(['age', 'gender']).sum()\n{df.duplicated(['age', 'gender']).sum()}\n\n")
df = df.drop_duplicates()
print(f"df = df.drop_duplicates()\n{df}\n\n")

##-- Missing data
title = "--- Missing data ---"
section(title, len(title))

print(f"df = users.copy()\n{df}\n\n")
print(f"df.describe(include='all')\n{df.describe(include='all')}")
print(f"df.height.isnull()\n{df.height.isnull()}\n\n")
print(f"df.height.notnull()\n{df.height.notnull()}\n\n")
print(f"df[df.height.notnull()]\n{df[df.height.notnull()]}\n\n")
print(f"df.height.isnull().sum()\n{df.height.isnull().sum()}\n\n")

print(f"df.isnull()\n{df.isnull()}\n\n")
print(f"df.isnull().sum()\n{df.isnull().sum()}\n\n")
print(f"df.dropna()\n{df.dropna()}\n\n")
print(f"df.dropna(how='all')\n{df.dropna(how='all')}\n\n")
print(f"df.height.mean()\n{df.height.mean()}\n\n")

##-- Rename values
title = "--- Rename values ---"
section(title, len(title))

df = users.copy()
print(f"df\n{df}\n\n")
print(f"df.columns\n{df.columns}\n\n")
df.columns = ['age', 'genre', 'travail', 'nom', 'taille']
df.travail = df.travail.map({'student': 'étudiant',
                             'manager': 'manager',
                             'engineer': 'ingénieur',
                             'scientist': 'scientific'})
#assert df.travail.isnull().sum() == 0
print(f"df['travail'].str.contains('étu|ingé')\n{df['travail'].str.contains('étu|ingé')}\n\n")
print(f"df:\n{df}\n\n")


## -- Dealing with outliers
title = "--- Dealing with outliers ---"
section(title, len(title))

size = pd.Series(np.random.normal(loc=175, size=20, scale=10))
print(f"size = pd.Series(np.random.normal(loc=175, size=20, scale=10))\n{size}\n\n")
# corrupt the first 3 measures
size[:3] = 500
print(f"size[:3] = 500\n{size}\n\n")

### Based on parametric statistic; use the mean
title = "--- Based on parametric statistics: use the mean ---"
section(title, len(title))

size_outlr_mean = size.copy()
print(f"size_outlr_mean = size.copy()\n{size_outlr_mean}\n\n")
size_outlr_mean[((size - size.mean()).abs() > 3 * size.std())] = size.mean()
print(f"size_outlr_mean[((size - size.mean()).abs() > 3 * size.std())] = size.mean()\n")
print(f"{size_outlr_mean}\n\n")
print(f"size_outlr_mean.mean()\n{size_outlr_mean.mean()}\n\n")

## -- Based on non-parametric statistics; use the median
title = "--- Based on non-parametric statistics: use the median ---"
section(title, len(title))

mad = 1.482 * np.median(np.abs(size - size.median()))   # Median absolute deviation
size_outlr_mad = size.copy()
print(f"size_outlr_mad\n{size_outlr_mad}\n\n")
size_outlr_mad[((size - size.median()).abs() > 3 * mad)] = size.median()
print("size_outlr_mad.mean(), size_outlr_mad.median(): ", end=' ')
print(size_outlr_mad.mean(), size_outlr_mad.median(), "\n")

## FILE I/O
title = "File I/O"
section(title, len(title))

import tempfile
import os.path

## -- csv
title = "--- csv ---"
section(title, len(title))
tmpdir = tempfile.gettempdir()
csv_filename = os.path.join(tmpdir, "users.csv")
users.to_csv(csv_filename, index=False)
other = pd.read_csv(csv_filename)

print(f"other\n{other}\n\n")

## -- Read csv from url
title = "--- Read csv from url ---"
section(title, len(title))
url = 'https://raw.github.com/neurospin/pystatsml/master/datasets/salary_table.csv'
salary = pd.read_csv(url)
print(f"salary = pd.read_csv(url)\n{salary}\n\n")

## Excel
title = "--- Excel ---"
section(title, len(title))
xls_filename = os.path.join(tmpdir, "users.xlsx")
users.to_excel(xls_filename, sheet_name='users', index=False)
xlsdata = pd.read_excel(xls_filename, sheet_name="users")
print(f"xsldata\n{xlsdata}\n\n")

# Multiple sheets
with pd.ExcelWriter(xls_filename) as writer:
    users.to_excel(writer, sheet_name='users', index=False)
    df.to_excel(writer, sheet_name='salary', index=False)
    
usersdata = pd.read_excel(xls_filename, sheet_name='users')
salarydata = pd.read_excel(xls_filename, sheet_name='salary')
print(f"userdata\n{usersdata}\n\nsalarydata\n{salarydata}\n\n")

## SQL (SQLite)
#title = "--- SQL (SQLite) ---"
#section(title, len(title))
#import sqlite3


#db_filename = os.path.join(tmpdir, "users.db")
#conn = sqlite3.connect(db_filename)
#salary = pd.read_csv(url)
#salary.to_sql('salary', conn, if_exists='replace')

#cur = conn.cursor()
#values = (100, 14000, 5, 'Bachelor', 'N')
#cur.execute("INSERT INTO salary VALUES(?, ?, ?, ?, ?)", values)
#conn.commit()

#salary_sql = pd.read_sql_query("SELECT * FROM salary;", conn)
#print(f"salary_sql.header()\n{salary_sql.header()}\n\n")

#salary_sql = pd.read_sql_query("SELECT * FROM salary;", conn)
#print(f"\n{salary_sql.tail()}\n\n")
#print('pd.read_sql_query("SELECT * FROM salary WHERE salary>25000;", conn)'
#      f'\n{pd.read_sql_query("SELECT * FROM salary WHERE salary>25000;", conn)}\n\n')
#print('pd.read_sql_query("SELECT * FROM salary WHERE experience=16;", conn)'
#      f'\n{pd.read_sql_query("SELECT * FROM salary WHERE experience=16;", conn)}\n\n')
#print(r"""pd.read_sql_query('SELECT * FROM salary WHERE education="Master";', conn)""",
#      '\n',
#      pd.read_sql_query('SELECT * FROM salary WHERE education="Master";', conn),
#      '\n\n')
#cur.close()
#conn.close()
