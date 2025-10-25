# Conditional Multiple Plots


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt   # import libraries
iris_df = sns.load_dataset('iris')
grid = sns.FacetGrid(iris_df, col='species')  # facet grid intialization
grid.savefig('output/graph.png')  # save the figure



grid = sns.FacetGrid(iris_df, col='species')
grid.map(sns.kdeplot, "petal_width")
grid.savefig('output/graph.png')  # save the figure


grid = sns.FacetGrid(mpg_df, col='origin',hue="cylinders")
grid.map(sns.scatterplot, "displacement","horsepower")
plt.legend()   # add legend
grid.savefig('output/graph.png')  # save the figure



grid = sns.FacetGrid(iris_df, col='species')
grid.map(sns.kdeplot, "petal_width", fill='True', lw=2)# specify styling parameters
grid.savefig('output/graph.png')  # save the figure




grid = sns.FacetGrid(tips_df, col_wrap=3, col="size", hue="sex")   # col_wrap
grid.map(sns.scatterplot, "total_bill", "tip")
grid.add_legend()
grid.savefig('output/graph.png')  # save the figure




grid = sns.FacetGrid(mpg_df, col="origin", height=4, aspect=.5)
grid.map(sns.barplot, "cylinders", "horsepower", order=[8,6,4])
grid.savefig('output/graph.png')  # save the figure



grid = sns.FacetGrid(titanic_df,hue='who', col="pclass",
             margin_titles=True, height=4.5)  # facet intialization
grid.map(sns.scatterplot, "age", "fare",s=50)      # specify plot
grid.set_axis_labels("Age", "Fare (US $)")  #set x-axis and y-axis label
grid.fig.suptitle('Fare distribution with age and passenger class') # set title
grid.tight_layout()  # to fit figure within the area
# save the figure
grid.savefig('output/graph.png')





# Using Custom Functions in Multi-plot Grids



import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('darkgrid')
# custom function
def double_tips(x,**kwargs):    # simple function that doubles the tip amount
     x_sq = x**2
     plt.scatter(x,x_sq,**kwargs)  
     plt.ylabel("tip$^2$") 
# import data
tips_df = sns.load_dataset('tips')
g = sns.FacetGrid(tips_df, col="sex",hue='smoker', height=4)
g.map(double_tips, "tip")
g.savefig('output/graph.png')




from scipy import stats
def quantiles_func(x,y,**kwargs):
     xq = stats.probplot(x, fit=False)
     yq = stats.probplot(y, fit=False)
     plt.scatter(xq, yq, **kwargs)
# intialize facet grid
g = sns.FacetGrid(tips_df, col="sex", hue='smoker', height=4,aspect=2)
g.map(quantiles_func, "total_bill", "tip")
g.savefig('output/graph.png')



def plot_mean_line(var,**kwargs):    
     ax = plt.gca()  # get current axis
     mean = np.mean(var)     # get data mean
     ax.axvline(mean, ls='--', lw=2, color='red')
     ax.text(0.8,0.8, f'mean={mean:.2f}', fontweight='bold', color='red',
     ha='center', transform=ax.transAxes, fontsize=12)
# facet grid initialization
g = sns.FacetGrid(peng_df, col="species", height=5)
g.map(sns.kdeplot, "body_mass_g", fill=True)
g.map(plot_mean_line, "body_mass_g")
g.savefig('output/graph.png')




# Plotting Multiple Pairwise Relations


import seaborn as sns
import matplotlib.pyplot as plt
# import data
peng_df = sns.load_dataset("penguins")
pg = sns.PairGrid(peng_df)
pg.map(sns.scatterplot)
# saving figure
pg.savefig('output/graph.png')



pg = sns.PairGrid(peng_df) #intialize
pg.map_offdiag(sns.scatterplot)    # non diagonals
pg.map_diag(sns.kdeplot)   # main diagonal (univariate)
pg.savefig('output/graph.png')   # saving figure




pg = sns.PairGrid(peng_df , hue ='species')
pg.map_offdiag(sns.scatterplot)    # non diagonals
pg.map_diag(sns.kdeplot)   # main diagonal (univariate)
pg.add_legend()
pg.savefig('output/graph.png')




pg = sns.PairGrid(peng_df , palette='Set2', hue ='species')
pg.map_upper(sns.kdeplot)
pg.map_lower(sns.scatterplot)
pg.map_diag(sns.histplot, kde=True)
pg.add_legend()
pg.savefig('output/graph.png')




pg = sns.PairGrid(peng_df, y_vars=["body_mass_g"],
                 x_vars=["bill_length_mm","bill_depth_mm"], 
                 hue ='species',palette='Set1', height=4)
pg.map(sns.scatterplot, marker = 'D')
pg.add_legend()
pg.savefig('output/graph.png')





# Multi-Plot Grids with Different Styles



import matplotlib.pyplot as plt
import seaborn as sns
fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(8,8),  constrained_layout=True)
plt.savefig('output/graph.png') # to save figure



f, axs = plt.subplots(2, 2, figsize=(8, 8), constrained_layout=True)
sns.scatterplot(data=peng_df, x="flipper_length_mm",
                y="bill_length_mm", hue="species", ax=axs[0,0],legend=False)
plt.savefig('output/graph.png')                



f, axs = plt.subplots(2, 2, figsize=(8, 8), constrained_layout=True)
# define plots
sns.scatterplot(data=peng_df, x="flipper_length_mm",
               y="bill_length_mm", hue="species", ax=axs[0,0],legend=False)
sns.histplot(data=peng_df, x="species", 
             hue="species", shrink=.8, alpha=.8, legend=False, ax=axs[1,1])
plt.savefig('output/graph.png') 




f, axs = plt.subplots(2, 2, figsize=(8, 8), constrained_layout=True)
# define plots
sns.scatterplot(data=peng_df, x="flipper_length_mm", 
            y="bill_length_mm", hue="species", ax=axs[0,0],legend=False)
sns.histplot(data=peng_df, x="species", hue="species", 
             shrink=.8, alpha=.8, legend=False, ax=axs[1,1])
sns.kdeplot(data=peng_df, x="body_mass_g", 
           hue="species", fill=True, lw =2, ax=axs[0,1])
sns.violinplot(data=peng_df, x="body_mass_g",  ax=axs[1,0])
plt.savefig('output/graph.png')