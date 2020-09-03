# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of acceleration vs. mpg
sns.relplot(x="acceleration",y="mpg",data=mpg,size="origin",hue="origin",kind="scatter",style="origin")



# Show plot
plt.show()