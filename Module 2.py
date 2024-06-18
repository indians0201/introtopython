## Die project I was using to learn for finance stuff
import pandas as pd
import numpy as np
intro = 'Sum of Dice is'
die = pd.DataFrame([1,2,3,4,5,6])

sod = die.sample(2,replace = True).sum().loc[0]


print('Sum of dice is', sod)
 print(intro, sod)
