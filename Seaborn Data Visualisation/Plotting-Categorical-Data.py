# Visualization with Count Plots



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme()
tips_df = sns.load_dataset('tips')
print(tips_df.head())




cplot = sns.countplot( data = tips_df , x ='sex')   #returns bar container
plt.bar_label(cplot.containers[0])
plt.savefig('output/graph.png')    # save figure




cplot = sns.countplot( data = tips_df , x ='sex', color ='green')
plt.bar_label(cplot.containers[0], padding=2, color='red',
               fontsize=15, label_type= 'edge')    # customise bar labels
plt.ylim(top = 180)         # customise axis range     
plt.savefig('output/graph.png')




c_plot = sns.countplot( data = tips_df , x ='sex', hue='smoker')  
plt.bar_label(c_plot.containers[0], padding=1, color='red',
               fontsize=15, label_type= 'edge')     # first group
plt.bar_label(c_plot.containers[1], padding=1, color='black',
               fontsize=15, label_type= 'center')  # second group
plt.ylim(top = 120)
plt.savefig('output/graph.png')





sns.set(font_scale = 0.9)
c_plot = sns.countplot(y='species', data = penguins_df)
plt.bar_label(c_plot.containers[0], padding=1, color='black',
               fontsize=12, label_type= 'edge')
plt.xlim(right=170)     # set xlim for horizontal plot
plt.savefig('output/graph.png')



print(penguins_df.species.value_counts())




c_plot = sns.countplot(x='species', data = penguins_df,
         order = ['Adelie','Gentoo','Chinstrap'])
plt.bar_label(c_plot.containers[0], padding=1, color='red',
               fontsize=15, label_type= 'edge')   
plt.ylim(top = 170)              
plt.savefig('output/graph.png')






c_plot = sns.countplot(x='species', data = penguins_df,
              hue = 'island', hue_order=['Torgersen','Dream'])
plt.bar_label(c_plot.containers[0], padding=1, color='black',
               fontsize=15, label_type= 'edge')  # first group
plt.bar_label(c_plot.containers[1], padding=1, color='black',
               fontsize=15, label_type= 'edge')  # second group
plt.ylim(top=100)
plt.savefig('output/graph.png')





print(penguins_df.groupby('species').island.value_counts())





c_plot = sns.countplot(data=tips_df , x='sex', hue = 'time', saturation = 0.4)
plt.bar_label(c_plot.containers[0], padding=1, color='black',
               fontsize=15, label_type= 'edge')  # first group
plt.bar_label(c_plot.containers[1], padding=1, color='red',
               fontsize=15, label_type= 'edge')  # second group
plt.ylim(top = 140) # set y-axis limit
plt.savefig('output/graph.png')





c_plot = sns.countplot(data=tips_df , x='sex', hue = 'time', saturation = 3.0)
plt.bar_label(c_plot.containers[0], padding=1, color='black',
               fontsize=15, label_type= 'edge')  # first group
plt.bar_label(c_plot.containers[1], padding=1, color='red',
               fontsize=15, label_type= 'edge')  # second group
plt.ylim(top = 140) 
plt.savefig('output/graph.png')




# Visualization with Bar Plots


c_plot = sns.barplot(data=titanic_df , x='pclass', y='age') # categorized on pclass
plt.bar_label(c_plot.containers[0], padding=13, color='red',
               fontsize=14, fmt= "%.2f" , label_type= 'edge')
plt.ylim(top = 50)              
plt.savefig('output/graph.png')

print(titanic_df.groupby('pclass').age.mean()) 


c_plot = sns.barplot(data=titanic_df , x='pclass', y='age', order=[3,2,1])
plt.bar_label(c_plot.containers[0], color='black',
               fontsize=15, fmt= "%.2f" , label_type= 'center')
plt.savefig('output/graph.png') 


c_plot = sns.barplot(data=titanic_df , x='pclass', y='age', ci =50)
plt.bar_label(c_plot.containers[0], padding=4, color='black',
               fontsize=15, fmt= "%.2f" , label_type= 'center')
plt.savefig('output/graph.png')



c_plot = sns.barplot(data=titanic_df , x='pclass', y='age', ci =95, n_boot=500)
plt.bar_label(c_plot.containers[0], padding=12, color='red',
               fontsize=15, fmt= "%.2f" , label_type= 'edge')
plt.ylim(top = 50)               
plt.savefig('output/graph.png')



c_plot = sns.barplot(data=titanic_df , x='pclass', y='age', hue='who')  # add hue 
# first hue group
plt.bar_label(c_plot.containers[0], padding=18, color='red',
               fontsize=10, fmt= "%.2f" , label_type= 'edge')  
# second hue group              
plt.bar_label(c_plot.containers[1], padding=18, color='black',
               fontsize=10, fmt= "%.2f" , label_type= 'edge')  
# third hue group
plt.bar_label(c_plot.containers[2], padding=18, color='green',
               fontsize=10, fmt= "%.2f" , label_type= 'edge')   
plt.ylim(top = 60)
plt.savefig('output/graph.png')



c_plot = sns.barplot(data=titanic_df , x='pclass', y='age',
              hue='who', hue_order=['child','woman','man']) 
# first hue group
plt.bar_label(c_plot.containers[0], padding=18, color='red',
               fontsize=10, fmt= "%.2f" , label_type= 'edge')  
 # second hue group
plt.bar_label(c_plot.containers[1], padding=18, color='black',
               fontsize=10, fmt= "%.2f" , label_type= 'edge')  
 # third hue group
plt.bar_label(c_plot.containers[2], padding=18, color='green',
               fontsize=10, fmt= "%.2f" , label_type= 'edge')  
plt.ylim(top = 60)
plt.savefig('output/graph.png')



c_plot = sns.barplot(data=titanic_df , x='age', y='pclass', orient ='h')
plt.bar_label(c_plot.containers[0], color='black',
               fontsize=15, fmt= "%.2f" , label_type= 'center')  # first hue group
plt.savefig('output/graph.png')



c_plot = sns.barplot(data=titanic_df , x='pclass', y='age', 
             hue='who', errcolor='red',errwidth=5.0) 
# first hue group             
plt.bar_label(c_plot.containers[0], padding=13, color='black',
               fontsize=10, fmt= "%.2f" , label_type= 'edge') 
# second hue group
plt.bar_label(c_plot.containers[1], padding=13, color='black',
               fontsize=10, fmt= "%.2f" , label_type= 'edge') 
 # third hue group
plt.bar_label(c_plot.containers[2], padding=13, color='black',
               fontsize=10, fmt= "%.2f" , label_type= 'edge')
plt.ylim(top = 60)
plt.savefig('output/graph.png')

c_plot = sns.barplot(data=titanic_df ,x='pclass', y='age',
             capsize=0.2,errcolor='red',errwidth=5.0) 
plt.bar_label(c_plot.containers[0], color='black',
               fontsize=15, fmt= "%.2f" , label_type= 'center')
plt.ylim(top = 50)
plt.savefig('output/graph.png')




# Visualization with Point Plots


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt   
sns.set_theme()
diamonds_df = sns.load_dataset('diamonds')
print(diamonds_df.head())

sns.pointplot(x='cut', y = 'depth', data= diamonds_df)  
plt.savefig('output/graph.png')

print(diamonds_df.groupby('cut').depth.mean())

sns.pointplot(x='cut', y = 'depth', data= diamonds_df, order = ['Ideal','Fair']) 
plt.savefig('output/graph.png')

sns.pointplot( x='cut', y = 'depth', 
              data= diamonds_df,estimator= np.std)   # change estimator
plt.savefig('output/graph.png')

sns.pointplot( x='cut', y = 'depth', data= diamonds_df, ci = 65)  # change ci
plt.savefig('output/graph.png')

sns.pointplot( x ='cut', y = 'depth', 
               data= diamonds_df, n_boot = 400)   # change bootstrap samples
plt.savefig('output/graph.png')

sns.pointplot( x ='cut', y = 'price', data= diamonds_df, hue='color') 
plt.savefig('output/graph.png')

sns.pointplot( x='cut', y = 'price',hue='color', 
              hue_order=['A','B','C','D','E'], 
              data= diamonds_df) 
plt.savefig('output/graph.png')


sns.pointplot( x ='cut', y = 'price', hue='color',
               hue_order=['D','E','F'], 
               data= diamonds_df, dodge=True)
plt.savefig('output/graph.png')


sns.pointplot( x ='cut', y = 'price',
               hue='color', hue_order=['D','E','F'], 
               data= diamonds_df, join =False) 
plt.savefig('output/graph.png')


sns.set(font_scale = 0.6)
sns.pointplot(x='price', y = 'cut',
              hue='color', hue_order=['D','E','F'], 
              data= diamonds_df, join=False)           # horizontal
plt.savefig('output/graph.png')



sns.pointplot(x ='cut', y ='depth',hue='color', hue_order=['D','E'],  
              data= diamonds_df, markers=["o", '*'], dodge =True)
plt.savefig('output/graph.png')



sns.pointplot(x='cut', y = 'depth',hue ='clarity', 
                data= diamonds_df, errwidth=3, capsize=.3, join=False) 
plt.savefig('output/graph.png')




# Visualization with Box Plots


sns.boxplot(x='age', data = titanic_df)   
plt.savefig('output/graph.png')



print(titanic_df['age'].describe())


sns.boxplot(y='age',x='who', data = titanic_df) #categorize on who 
plt.savefig('output/graph.png')



print(titanic_df.groupby('who').age.describe())



sns.boxplot(y='age',x='class', data = titanic_df)   
plt.savefig('output/graph.png')


sns.boxplot(y='age',x='class', data = titanic_df, hue='who') #add hue
plt.savefig('output/graph.png')


sns.boxplot( y='age',x='class', data = titanic_df, 
              hue='who', hue_order = ['woman','child'])  
plt.savefig('output/graph.png')



sns.boxplot( y='age',x='class', data = titanic_df, 
             hue='who', fliersize=8) 
plt.savefig('output/graph.png')



sns.boxplot( y='age',x='class', data = titanic_df,
                 hue='who', fliersize=8, linewidth=3)   
plt.savefig('output/graph.png')



sns.boxplot( y='age',x='class', data = titanic_df,
             width=1, order = ['First','Second'])
plt.savefig('output/graph.png')



sns.boxplot( y='age',x='class', data = titanic_df, hue='who', whis =np.inf)   
plt.savefig('output/graph.png')



sns.boxplot( x='age',y='class', data = titanic_df, whis= np.inf, hue='who',dodge=False)
plt.savefig('output/graph.png')


# Visualization with Violin Plots


import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
sns.set_theme()
mpg_df = sns.load_dataset('mpg')
print(mpg_df.head())


sns.violinplot(data = mpg_df , x ='weight')     
plt.savefig('output/graph.png')


sns.violinplot(data =mpg_df , x='cylinders', y ='weight') 
plt.savefig('output/graph.png')


sns.violinplot(data =mpg_df , x='cylinders', 
                 y ='weight', order=[4,5,6])    # add order
plt.savefig('output/graph.png')


sns.violinplot(data =mpg_df , x='cylinders',
                y ='weight', hue='origin')    # add hue
plt.savefig('output/graph.png')



sns.violinplot(data =mpg_df , x='cylinders', 
                y ='weight', hue='origin',hue_order=['usa'])        # add hue order
plt.savefig('output/graph.png')


sns.violinplot(data =mpg_df , x='cylinders', 
                y ='weight', hue='origin' ,    
                dodge = False) 
plt.savefig('output/graph.png')



sns.violinplot(data =mpg_df , x='cylinders',
                y ='weight', hue='origin',scale="count")
plt.savefig('output/graph.png')



sns.violinplot(data =mpg_df , x='cylinders', y ='weight', hue='origin',
                hue_order = ['japan','europe'] ,split=True)    
plt.savefig('output/graph.png')



sns.violinplot(data =mpg_df , x='cylinders', y ='weight', hue='origin', 
                hue_order = ['japan','europe'] , linewidth=3.0) 
plt.savefig('output/graph.png')



sns.violinplot( data =mpg_df , x='cylinders', y ='weight', hue='origin',
               hue_order = ['japan','europe'] , inner ='quartile' , split=True)
plt.savefig('output/graph.png')



sns.violinplot(data =mpg_df , x='cylinders', y ='weight', hue='origin',
               hue_order = ['europe'] , cut =True)
plt.savefig('output/graph.png')






# Visualization with Swarm Plots


sns.swarmplot(x='body_mass_g', data = penguins_df)
plt.savefig('output/graph.png')



sns.swarmplot(x='body_mass_g',y='sex', data = penguins_df) # group on categoricals
plt.savefig('output/graph.png')



sns.swarmplot(x='body_mass_g',y='sex', data = penguins_df,
              order=['Female','Male'])    # change categoricals order
plt.savefig('output/graph.png')



sns.swarmplot(y='body_mass_g', data = penguins_df)  # display vertical
plt.savefig('output/graph.png')



sns.swarmplot(x='sex',y='body_mass_g', hue= 'species', data = penguins_df)  # add hue 
plt.savefig('output/graph.png')



sns.swarmplot(x='sex',y='body_mass_g', hue= 'species', dodge= True,data = penguins_df)   
plt.savefig('output/graph.png')



sns.swarmplot(x='sex',y='body_mass_g', 
              hue='island',linewidth=0.7,
              data = penguins_df.query("body_mass_g>4000"))
plt.savefig('output/graph.png')



sns.swarmplot(y='sex',x='body_mass_g', data = penguins_df,
             linewidth=1.0, edgecolor='red')  
plt.savefig('output/graph.png')



sns.violinplot(x='sex',y='body_mass_g', 
            data = penguins_df, inner =None)    # remove boxplot in background
sns.swarmplot(x='sex',y='body_mass_g', 
         data = penguins_df, color='black', size=3.0)  
plt.savefig('output/graph.png')




sns.boxplot(x='sex',y='body_mass_g',
             data = penguins_df)
sns.swarmplot(x='sex',y='body_mass_g', 
             data = penguins_df, color='black')       
plt.savefig('output/graph.png')





# Visualization with Strip Plots


sns.stripplot(data = penguins_df,x='sex', y='body_mass_g')  # categorize on gender
plt.savefig('output/graph.png')


sns.stripplot(data = penguins_df,y='sex', x= 'body_mass_g', hue='species') # add hue
plt.savefig('output/graph.png')



sns.stripplot(data = penguins_df,x='sex',y='body_mass_g', hue='species',dodge=True)
plt.savefig('output/graph.png')



sns.stripplot(data = penguins_df, x='sex', y='body_mass_g', hue='species',
              dodge=True, jitter= False) 
plt.savefig('output/graph.png') 



sns.stripplot(data = penguins_df, x='sex', y='body_mass_g', hue='species',
              dodge=True, jitter =0.03)
plt.savefig('output/graph.png')




sns.stripplot(data = penguins_df,x='body_mass_g',y='sex', hue='species',alpha=0.4) 
plt.savefig('output/graph.png')



sns.stripplot(data = penguins_df,x='body_mass_g', y='sex', hue='species',size=7) 
plt.savefig('output/graph.png')



sns.boxplot(data = penguins_df,x='body_mass_g',
              y='island', whis=np.inf)                                                        
sns.stripplot(data = penguins_df,x='body_mass_g',
              y='island',color='black', alpha=0.3) 
plt.savefig('output/graph.png')




sns.violinplot(data = penguins_df,x='body_mass_g', 
               y='island', inner=None)                  
sns.stripplot(data = penguins_df,x='body_mass_g',
              y='island',color='black', alpha=0.3) 
plt.savefig('output/graph.png')





# Visualization with Cat Plots



sns.catplot(x ='age', data = titanic_df)       # default strip plot
plt.savefig('output/graph.png')


sns.catplot(x ='age', data = titanic_df, kind = 'violin') 
plt.savefig('output/graph.png')



titanic_df['survived'] = np.where(titanic_df['survived']==1,'Yes','No')
sns.catplot(y ='age', x='class', hue='survived', kind='box', data=titanic_df) 
plt.savefig('output/graph.png')



g= sns.catplot(x ='class', y='age', kind ='bar',col ='embark_town' , data=titanic_df)
g.set_xlabels("Class", fontsize = 16, labelpad=12)  
plt.savefig('output/graph.png')



g= sns.catplot(x ='class', y='age', kind ='bar',data=titanic_df,
            col ='embark_town',row ='survived')
g.set_xlabels("Class", fontsize = 16, labelpad=12) 
plt.savefig('output/graph.png')



print(titanic_df['deck'].nunique())



g= sns.catplot(x ='class', y='age', kind ='bar', data=titanic_df,col ='embark_town',
            row ='deck',row_order=['A','B','C'])
g.set_xlabels("Class", fontsize = 16, labelpad=12) 
plt.savefig('output/graph.png')



g= sns.catplot(x ='class',y='age',hue= 'survived', kind ='bar',
            data=titanic_df,col ='deck',col_wrap=3)
g.set_xlabels("Class", fontsize = 16, labelpad=12) 
plt.savefig('output/graph.png')





g= sns.catplot(x ='class',y='age', hue= 'survived',kind ='bar', data=titanic_df,
            col ='embark_town',height = 5, aspect=1)
g.set_xlabels("Class", fontsize = 16, labelpad=12) 
plt.savefig('output/graph.png')




g= sns.catplot(x ='class',y='age',hue= 'survived',kind ='bar',data=titanic_df,
            col ='embark_town',legend_out= False)
g.set_xlabels("Class", fontsize = 16, labelpad=12) 
plt.savefig('output/graph.png')