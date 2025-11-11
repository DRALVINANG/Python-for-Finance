import pandas as pd

df = pd.read_csv('https://gist.githubusercontent.com/DRALVINANG/5821855d6bcce977fc7f7638bb7ea9a3/raw/9d5bf33a581bf81a8319baf9d677eef309a2d7e9/TSLA%2520Stock%2520Price%2520(2020).csv')
print(df)
#-------------------------------------------------------------------------------------------

#SCATTER PLOT
import matplotlib.pyplot as plt

plt.scatter(df.Date,
            df.Close,
            color = 'blue',
            alpha = 0.7)

plt.show()

#--------------------------------------------------------------------------

#LINE PLOT
plt.plot(df.Date, df.Close)
plt.plot(df.Date, df.High)


#COSMETICS
plt.xticks(rotation=90)
plt.title('TITLE', fontsize = 14)
plt.xlabel('X_LABEL', fontsize = 12)
plt.ylabel('Y_LABEL', fontsize = 12)
plt.grid(True)
plt.show()

#--------------------------------------------------------------------------


