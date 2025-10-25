# Seaborn's Built-in Themes


sns.set_style('darkgrid')   # set theme
cplot = sns.countplot(x='sex', width = 0.6, data=tips_df)
plt.bar_label(cplot.containers[0])   # bar label
plt.ylim(top = 170)   # axis range
plt.savefig('output/graph.png')



sns.set_style('darkgrid')   # set theme
sns.boxplot(x='pclass', y='age', data=titanic_df)
plt.savefig('output/graph.png')



sns.set_style('whitegrid')
sns.histplot( x ='total_bill',hue='smoker', multiple='dodge', shrink=.7, data=tips_df)
plt.ylabel('frequency')
plt.savefig('output/graph.png')



sns.set_style('whitegrid')
sns.boxplot( x ='total_bill', y= 'sex', hue='smoker', dodge=False, data=tips_df)
plt.savefig('output/graph.png')


sns.set_style('dark')
sns.lineplot(x='timepoint', y='signal', hue='event', data=fmri_df)
plt.savefig('output/graph.png')



sns.set_style('white')
sns.kdeplot(x='total_bill',fill=True, data=tips_df, lw=2)
plt.savefig('output/graph.png')



sns.set_style('white')
sns.regplot( x='displacement', y = 'mpg', data= mpg_df, marker='+',
           scatter_kws = {'color': 'purple', 'alpha': 0.3},
           line_kws = {'color': 'red', 'alpha': 0.5, 'lw':2})
plt.savefig('output/graph.png')



sns.set_style('ticks')
j_plt = sns.jointplot(x= 'horsepower', y= 'mpg', data = mpg_df, 
             height= 7, ratio = 3, marker = "+", marginal_ticks= True)
j_plt.plot_joint(sns.kdeplot, color="r",levels=6)
plt.savefig('output/graph.png')




# Figure Scaling and Styling


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
tips_df = sns.load_dataset('tips')
sns.pairplot(hue = 'sex' , data = tips_df)
plt.savefig('output/graph.png')



import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set_context('paper')
tips_df = sns.load_dataset('tips')
sns.pairplot(hue = 'sex' , data = tips_df)
plt.savefig('output/graph.png')



import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set_context('talk')
tips_df = sns.load_dataset('tips')
sns.pairplot(hue = 'sex' , data = tips_df)
plt.savefig('output/graph.png')




import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set_context('poster')
tips_df = sns.load_dataset('tips')
sns.pairplot(hue = 'sex' , data = tips_df)
plt.savefig('output/graph.png')




f = plt.figure(figsize=(6, 6)) # set figure
gs = f.add_gridspec(2, 2)   # make 2x2 grid
 # random values
x1 = np.arange(1, 10, 0.1)     
y1 = np.sin(x1)   # sinx
y2 = np.cos(x1)   # cosx   
# first axis style
with sns.axes_style("darkgrid"):   
    ax = f.add_subplot(gs[0, 0])
    plt.plot(x1,y1, ls ='dashed')  #sinx
    plt.plot(x1,y2, ls='dashed') #cos x
# second axis style
with sns.axes_style("ticks"):
    ax = f.add_subplot(gs[1, 0])   
    plt.plot(x1,y1, linewidth = 3)  
    plt.plot(x1,y2, linewidth = 3)  
# third axis style
with sns.axes_style("white"):     
    ax = f.add_subplot(gs[0, 1])
    plt.plot(x1,y1, c='green')
    plt.plot(x1,y2, c='red')
# fourth axis style
with sns.axes_style("whitegrid"):   
    ax = f.add_subplot(gs[1, 1])
    plt.plot(x1,y1) 
    plt.plot(x1,y2)
f.tight_layout()   # fit the plot within area
# save the figure
f.savefig('output/graph.png')




# Seaborn Axis Spines


sns.set(font_scale=1.2, style = 'ticks')  # set theme
var1 = [1,3,5,7,9,10,11,12,13,15,16,17,19,21,22,23,24,27,28,31,33,35,36] # dummy data
var2 = [2,4,6,8,10,5,12,13,14,16,19,18,20,22,24,25,10,28,30,32,34,36,15]
# reg plot
sns.regplot(x= var1, y=var2, color='red',
scatter_kws={"color":"green","s":40, "ec":'red'})
sns.despine()      # remove top and right axes spines
plt.title("Linear relationship")
plt.xlabel("x")
plt.ylabel("y")
# save the figure
plt.savefig('output/graph.png')



sns.lineplot(x='timepoint', y='signal', hue='event', data= fmri_df)
plt.title('Signal variation over time')
sns.despine(left=True, bottom=True)  # remove all axes spines
# save the figure
plt.savefig('output/graph.png')



import matplotlib.pyplot as plt
# classifier performance data
clsf = ['DT', 'RF', 'XGBoost', 'CatBoost', 'LSTM']
acccuracy = [0.65,0.80,0.95,0.92,0.89]
# get current figure axis
fig, ax = plt.subplots()  
sns.barplot(x=clsf, y =acccuracy, palette = 'hls') # plot data
plt.title('Classifiers comparison')
plt.ylim(top=1.0)
plt.ylabel('Accuracy')
sns.despine()      # remove top and right spines
ax.spines['left'].set_color('red')   # change left spine color
ax.spines['left'].set_linewidth(2)    # customize line width
ax.spines['bottom'].set_alpha(0.3)    # decrease transparency of bottom spines
plt.tight_layout()
plt.savefig('output/graph.png')




fig, ax = plt.subplots()
x1 = np.arange(-2, 2, 0.1)   # x values
y1 = np.sin(x1)
plt.plot(x1, y1, linewidth =3, ls ='dashed')   # sinx
y2 = np.cos(x1)   
plt.plot(x1,y2, linewidth = 3, ls='dashed')  # cosx
sns.despine()
ax.spines['left'].set_position(('data', 0))  # set coordinates according to axis
ax.spines['left'].set_color('red')
ax.spines['left'].set_linewidth(3)
ax.spines['left'].set_linestyle('dashed')
# add legend
plt.legend(['sin(x)', 'cos(x)'], loc =2)
plt.savefig('output/graph.png')





# Seaborn Color Palettes



import seaborn as sns
print(sns.palettes.SEABORN_PALETTES.keys())




import seaborn as sns
import matplotlib.pyplot as plt
sns.palplot(sns.color_palette(palette = 'deep', n_colors = 8))
plt.show()
 # save the figure
plt.savefig('output/graph.png')




import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set_theme()
mpg_df = sns.load_dataset('mpg')
sns.scatterplot(x='displacement', y='horsepower', hue='cylinders', data = mpg_df)
# save the figure
plt.savefig('output/graph.png')




mpg_df = sns.load_dataset('mpg')
sns.scatterplot(x='displacement', y='horsepower', hue='cylinders', 
                palette = 'bright', data = mpg_df)
# save the figure
plt.savefig('output/graph.png')




import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set_theme()
sns.set(font_scale = 0.7)
# import data
mpg_df = sns.load_dataset('mpg')
sns.heatmap(mpg_df.corr() ,  xticklabels = False, cmap= 'rocket')
# save figure
plt.savefig('output/graph.png')



import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set_theme()
# import data
penguins_df = sns.load_dataset('penguins') 
penguins_df_specie = penguins_df.groupby('species').island.value_counts().unstack().fillna(0) 
# heatmap
sns.heatmap(penguins_df_specie,lw= 2, annot=True, fmt= ".0f", cmap = 'Spectral') 
plt.savefig('output/graph.png') 