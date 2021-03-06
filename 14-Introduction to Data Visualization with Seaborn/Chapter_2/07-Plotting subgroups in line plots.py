#part1
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
# Create line plot of model year vs. horsepower
sns.relplot(x="model_year",y="horsepower",data=mpg,kind="line",ci=None)
# Show plot
plt.show()


#part2
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
# Change to create subgroups for country of origin
sns.relplot(x="model_year", y="horsepower",
            data=mpg, kind="line",
            ci=None,style="origin",hue="origin")
# Show plot
plt.show()


#part3
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower",
            data=mpg, kind="line",
            ci=None, style="origin",
            hue="origin",markers=True,dashes=False)

# Show plot
plt.show()