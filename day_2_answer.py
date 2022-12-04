'''
Paste the stratey guide into an input.txt file

Bash:
pbpaste > input.txt
echo -e "Opponent Me\n$(cat input.txt)" > input.txt
sed 'y/ /,/' input.txt > input2.txt
mv input2.txt input2.csv
'''

Python
import pandas as pd
df = pd.read_csv('input2.csv')
df.loc[df['Me'] ==  'X', 'my_letter_score'] = 1
df.loc[df['Me'] ==  'Y', 'my_letter_score'] = 2
df.loc[df['Me'] ==  'Z', 'my_letter_score'] = 3
df.loc[df['Opponent'] ==  'A', 'opp_letter_score'] = 1
df.loc[df['Opponent'] ==  'B', 'opp_letter_score'] = 2
df.loc[df['Opponent'] ==  'C', 'opp_letter_score'] = 3

'''
I win = 6
Draw 3
I lose 0
'''


df.loc[(df['Opponent'] ==  'A') & (df['Me'] == 'X'), 'me round score'] = 3
df.loc[(df['Opponent'] ==  'A') & (df['Me'] == 'X'), 'opp round score'] = 3
df.loc[(df['Opponent'] ==  'A') & (df['Me'] == 'Y'), 'opp round score'] = 0
df.loc[(df['Opponent'] ==  'A') & (df['Me'] == 'Y'), 'me round score'] = 6
df.loc[(df['Opponent'] ==  'A') & (df['Me'] == 'Z'), 'opp round score'] = 6
df.loc[(df['Opponent'] ==  'A') & (df['Me'] == 'Z'), 'me round score'] = 0
df.loc[(df['Opponent'] ==  'B') & (df['Me'] == 'X'), 'opp round score'] = 6
df.loc[(df['Opponent'] ==  'B') & (df['Me'] == 'X'), 'me round score'] = 0
df.loc[(df['Opponent'] ==  'B') & (df['Me'] == 'Y'), 'opp round score'] = 3
df.loc[(df['Opponent'] ==  'B') & (df['Me'] == 'Y'), 'me round score'] = 3
df.loc[(df['Opponent'] ==  'B') & (df['Me'] == 'Z'), 'opp round score'] = 0
df.loc[(df['Opponent'] ==  'B') & (df['Me'] == 'Z'), 'me round score'] = 6
df.loc[(df['Opponent'] ==  'C') & (df['Me'] == 'X'), 'opp round score'] = 0
df.loc[(df['Opponent'] ==  'C') & (df['Me'] == 'X'), 'me round score'] = 6
df.loc[(df['Opponent'] ==  'C') & (df['Me'] == 'Y'), 'opp round score'] = 6
df.loc[(df['Opponent'] ==  'C') & (df['Me'] == 'Y'), 'me round score'] = 0
df.loc[(df['Opponent'] ==  'C') & (df['Me'] == 'Z'), 'opp round score'] = 3
df.loc[(df['Opponent'] ==  'C') & (df['Me'] == 'Z'), 'me round score'] = 3


df['my_letter_score'].sum() + df['me round score'].sum()

'''
---
Part 2
---
'''


df2 = df 
df2['outcome'] = df['Me']
df2.drop(columns='Me', inplace=True)
df2 = df2[['Opponent', 'outcome', 'opp_letter_score']]

'''
X = lost
Y = Draw 
Z = Win
1 for Rock, 2 for Paper, and 3 for Scissors
'''


df2.loc[df2['outcome'] ==  'X', 'outcome_score'] = 0
df2.loc[df2['outcome'] ==  'Y', 'outcome_score'] = 3
df2.loc[df2['outcome'] ==  'Z', 'outcome_score'] = 6


df2.loc[(df2['Opponent'] ==  'A') & (df2['outcome'] == 'X'), 'Me_score'] = 3
df2.loc[(df2['Opponent'] ==  'A') & (df2['outcome'] == 'Y'), 'Me_score'] = 1
df2.loc[(df2['Opponent'] ==  'A') & (df2['outcome'] == 'Z'), 'Me_score'] = 2
df2.loc[(df2['Opponent'] ==  'B') & (df2['outcome'] == 'X'), 'Me_score'] = 1
df2.loc[(df2['Opponent'] ==  'B') & (df2['outcome'] == 'Y'), 'Me_score'] = 2
df2.loc[(df2['Opponent'] ==  'B') & (df2['outcome'] == 'Z'), 'Me_score'] = 3
df2.loc[(df2['Opponent'] ==  'C') & (df2['outcome'] == 'X'), 'Me_score'] = 2
df2.loc[(df2['Opponent'] ==  'C') & (df2['outcome'] == 'Y'), 'Me_score'] = 3
df2.loc[(df2['Opponent'] ==  'C') & (df2['outcome'] == 'Z'), 'Me_score'] = 1

df2['Me_score'].sum() + df2['outcome_score'].sum()

