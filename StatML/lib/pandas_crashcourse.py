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
                          agen=[33, 44],
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

