student_age = 22           # variable creation and declaration
student_name = "Sara"      # type of variable is determined based on the value assigned 
print("Data type of variable student_age: ",type(student_age))
print("Data type of variable student_name:",type(student_name))




student_name = "John"           # a string variable
student_weight = 50.20          # a floating variable representing weight in kilo-grams(Kg)
student_age = 25                # an integer variable
interview_passed = True         # a boolean variable






# scatter plots



import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme()             # set default theme
# dummy data
gym_data = {'time_spent': [10,15,20,30,40,50,60,80,90] ,
          'calories_burned': [80,88,100,138,200,300,400,600,710]}  
gym_df = pd.DataFrame(gym_data)  # data frame
sns.scatterplot(data=gym_df , x = 'time_spent' , y = 'calories_burned')
# saving figure
plt.savefig('output/graph.png')




# customising plot
sns.scatterplot(data=gym_df , x = 'time_spent' , y = 'calories_burned')
plt.title('Time spent on treadmill vs calories burned')
plt.xlabel("Time spent", fontsize= 10)
plt.ylabel("Calories burned", fontsize= 10)
# saving figure
plt.savefig('output/graph.png')






student_data = {'time_spent_playing': [15,16,20,30,35,45,50,55,70,80,90] ,
                 'exam_score': [90,89,85,70,62,55,50,42,30,25,10]}  
student_df = pd.DataFrame(student_data)
sns.scatterplot(data =student_data , x = 'time_spent_playing',y = 'exam_score')     
plt.title('Time spent on video games vs exam score')
plt.xlabel("Time spent", fontsize= 10)
plt.ylabel("Exam score", fontsize= 10)
# saving figure
plt.savefig('output/graph.png')





tips_df = sns.load_dataset('tips')
print(tips_df.head())
print("\nCount of null values\n")
print(tips_df.isnull().sum())






sns.scatterplot(data =tips_df , x = 'total_bill' , y = 'tip')    
plt.title('Tips w.r.t total bills')
plt.xlabel("Total bill", fontsize= 10)
plt.ylabel("Tips", fontsize= 10)
# saving figure
plt.savefig('output/graph.png')






emp_df = pd.read_csv('ShoeSizeandAverageSalary.csv')   # import data
print(emp_df.head())
print("\n Count of null values \n")
print(emp_df.isnull().sum())






sns.scatterplot(data= emp_df , x= 'Shoe_size' , y = 'Average_salary') 
plt.title('Relationship between average salary and shoe size')
plt.xlabel("Shoe size", fontsize= 10)
plt.ylabel("Average salary", fontsize= 10)
# saving figure
plt.savefig('output/graph.png')






# Pair Plots

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme()    # set default theme
tips_df = sns.load_dataset('tips')
print(tips_df.head())
sns.pairplot(data = tips_df, dropna = True)
plt.savefig('output/graph.png')  # save figure

sns.pairplot(data=tips_df , diag_kind="kde")
plt.savefig('output/graph.png')


sns.pairplot(data=tips_df , diag_kind="kde", height=2)
plt.savefig('output/graph.png')

sns.pairplot(data=tips_df , diag_kind="kde",aspect=2)
plt.savefig('output/graph.png')

sns.pairplot(data=tips_df , kind="reg", aspect=1)
plt.savefig('output/graph.png')

sns.pairplot( tips_df, x_vars=["total_bill", "tip" ],y_vars=["total_bill", "tip"])
plt.savefig('output/graph.png')


sns.pairplot(tips_df, x_vars=["total_bill", "tip","size" ],
             y_vars=["total_bill", "tip"])
plt.savefig('output/graph.png')




sns.pairplot(data = tips_df , corner=True)
plt.savefig('output/graph.png')




sns.pairplot(data = tips_df , diag_kws= {'color':'gray'})
plt.savefig('output/graph.png')




sns.pairplot(data = tips_df ,kind="kde", plot_kws= {'color':'xkcd:salmon'})
plt.savefig('output/graph.png')





# Adding the hue Parameter for Color Encoding


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme()
iris_df = sns.load_dataset('iris')
print(iris_df.head())
print("\n")                       #add new line
print(iris_df.dtypes)


sns.scatterplot(data = iris_df , x= 'sepal_length',y= 'petal_width' , hue='species')
plt.savefig('output/graph.png')        # save figure                 





import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme()
iris_df = sns.load_dataset('iris')
print(iris_df.head())
print("\n")                       #add new line
print(iris_df.dtypes)


peng_df = sns.load_dataset('penguins')
print("Data types\n",peng_df.dtypes)
print("\n")
print("Unique Species\n",peng_df['species'].unique())



sns.scatterplot( data = tips_df , x='tip' , y = 'size', hue = 'day')
plt.savefig('output/graph.png')

sns.scatterplot(data = tips_df , x = 'total_bill', y='tip', hue='sex')
plt.savefig('output/graph.png')   # save figure

colors = {"Adelie":"Red",
         "Chinstrap":"Black",
         "Gentoo": "Green"}     # custom colors for hue    
sns.pairplot(peng_df ,hue='species' ,palette=colors, height=2)
plt.savefig('output/graph.png')  # save figure






# Data Visualization with Line Plots



import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set_theme()
fmri_df = sns.load_dataset('fmri')
print(fmri_df.head())



sns.lineplot(data= fmri_df, x='timepoint', y='signal')
plt.title("Change in signal over time", fontsize= 10)
plt.xlabel("Time point", fontsize= 10)
plt.ylabel("Signal", fontsize= 10)
plt.savefig('output/graph.png')  # save figure 




sns.lineplot(data = fmri_df, x='timepoint', y='signal', hue='event', 
             err_style='bars')   # add error bars and hue
plt.title("Change in signal over time", fontsize= 10)
plt.xlabel("Time point", fontsize= 10)
plt.ylabel("Signal", fontsize= 10)                     
plt.savefig('output/graph.png')    # save figure




sales_df = pd.read_csv('IrishWhiskeySales.csv')
print(sales_df.head())
print("\n Data shape")
print(sales_df.shape)
print("\n Null values")
print(sales_df.isnull().sum())




updated_sales_df = sales_df.dropna()
print("Null values count\n",updated_sales_df.isnull().sum())
print("\n Data types")
print(updated_sales_df.dtypes)


print(updated_sales_df['Quality'].unique())



sns.lineplot( data = updated_sales_df, x = 'Year', y='Cases', hue ='Quality')      
plt.title("Whiskey sales per year w.r.t to quality", fontsize= 10)
plt.xlabel("Year", fontsize= 10)
plt.ylabel("Cases", fontsize= 10)                 
plt.savefig('output/graph.png')   #save fig





plot = sns.lineplot( data = updated_sales_df, x = 'Year', y='Cases', hue ='Country')    
plt.title("Whiskey sales per year w.r.t to quality", fontsize= 10)
plt.xlabel("Year", fontsize= 10)
plt.ylabel("Cases", fontsize= 10)                 
plt.savefig('output/graph.png')   #save fig





print(updated_sales_df['Country'].nunique())





sns.lineplot( data = updated_sales_df, x = 'Year', y='Cases', hue ='Country',
              hue_order = sales_df.Country.value_counts().iloc[:8].index)
plt.title("Whiskey sales per year w.r.t to quality", fontsize= 10)
plt.xlabel("Year", fontsize= 10)
plt.ylabel("Cases", fontsize= 10)  
plt.legend(loc ='upper left')               # customise legend location
plt.savefig('output/graph.png')   #save fig






# bootstrapping in seaborn



sns.lineplot( data = updated_sales_df, x = 'Year',
             y='Cases', estimator=sum) # estimator sum
plt.title("Whiskey sales per year with estimator sum", fontsize= 10)
plt.xlabel("Year", fontsize= 10)
plt.ylabel("Cases", fontsize= 10)              
plt.savefig('output/graph.png')




sns.lineplot( data = updated_sales_df, x = 'Year', y='Cases', 
                      estimator=None)  # show actual data points
plt.title("Whiskey sales per year with no estimator", fontsize= 10)
plt.xlabel("Year", fontsize= 10)
plt.ylabel("Cases", fontsize= 10)  
plt.savefig('output/graph.png')




sns.lineplot( data = updated_sales_df, x = 'Year', y='Cases', n_boot=20) 
plt.title("Whiskey sales per year", fontsize= 10)
plt.xlabel("Year", fontsize= 10)
plt.ylabel("Cases", fontsize= 10)  
plt.savefig('output/graph.png')




sns.lineplot( data = updated_sales_df, x = 'Year',
                      y='Cases', ci=None ) # no confidence interval
plt.title("Whiskey sales per year", fontsize= 10)
plt.xlabel("Year", fontsize= 10)
plt.ylabel("Cases", fontsize= 10)  
plt.savefig('output/graph.png')






# Relplots

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme()
titanic_df = sns.load_dataset('titanic')
print(titanic_df.head())




sns.relplot(data = titanic_df , x= 'age', y='fare', hue='class') 
plt.savefig('output/graph.png')  # save figure 




sns.relplot(data = titanic_df , x='age', y ='fare', hue='class',
            hue_order = ['Third','Second','First'])
plt.savefig('output/graph.png')  # save figure 




sns.relplot(data = titanic_df, hue='class', x= 'age', y='fare',col='embark_town')
plt.savefig('output/graph.png')  # save figure 



sns.relplot(data = titanic_df,hue='class', x= 'age', y='fare',row='who')
plt.savefig('output/graph.png')  # save figure 



fmri_df = sns.load_dataset('fmri')
print(fmri_df.head())



sns.relplot(data = fmri_df , x ='timepoint', y = 'signal', kind = 'line',
             col ='event', hue  ='region')
plt.savefig('output/graph.png')  # save figure




whiskey_df = pd.read_csv('IrishWhiskeySales.csv')       
print(whiskey_df.head())




sns.relplot( data = whiskey_df, x ='Year', 
            y ='Cases', kind = 'line',
            col='Quality',col_wrap = 2)
plt.savefig('output/graph.png')  





sns.relplot( data = fmri_df , x= 'timepoint',y = 'signal', kind = 'line',
              col ='event', hue='region',legend = False)
plt.savefig('output/graph.png')  # save figure





sns.relplot( data = fmri_df , x= 'timepoint',y = 'signal', kind = 'line',
             col ='event', hue='region',legend =False, aspect =2, height = 7)
plt.savefig('output/graph.png')  




# Visualization with Heatmaps




import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set_theme()
penguins_df = sns.load_dataset('penguins')
print(penguins_df.head())




sns.set(font_scale=0.7)
sns.heatmap(penguins_df.corr())
plt.savefig('output/graph.png')


print(penguins_df.groupby('species').island.value_counts())    # multilevel index


print(penguins_df.groupby('species').island.value_counts().unstack())  # unstack the data



penguins_df_specie = penguins_df.groupby('species').island.value_counts().unstack().fillna(0)   
print(penguins_df_specie.head())




sns.heatmap(penguins_df_species) 
plt.savefig('output/graph.png') 



sns.set(font_scale=0.7)
sns.heatmap(penguins_df.corr(), cmap="Greens")     
plt.savefig('output/graph.png')



x_label = ['BISCOE', 'DREAM','TORGERSEN']
y_label = ['ADELIE','CHINSTRAP','GENTOO']
sns.heatmap(penguins_df_specie,cmap="YlGnBu", xticklabels=x_label,yticklabels=y_label)
plt.savefig('output/graph.png')




sns.set(font_scale=0.7)
sns.heatmap(penguins_df_specie, cmap="YlGnBu",xticklabels= False)  
plt.savefig('output/graph.png')




sns.set(font_scale = 0.7)
sns.heatmap(penguins_df.corr(), cmap="PiYG", center = 0) 
plt.savefig('output/graph.png')




sns.set(font_scale = 0.7)
sns.heatmap(penguins_df.corr(), cmap="Greens", vmin=-0.5, vmax=1)  
plt.savefig('output/graph.png')




sns.heatmap(penguins_df_specie, cmap="YlGnBu",annot=True)
plt.savefig('output/graph.png')




sns.heatmap(penguins_df_specie, cmap="YlGnBu", annot=True, fmt= ".1f") 
plt.savefig('output/graph.png')




sns.heatmap(penguins_df_specie, cmap="YlGnBu", annot=True, fmt= ".0f",
            linewidths=5, linecolor='black') 
plt.savefig('output/graph.png') 





sns.heatmap(penguins_df_specie, cmap="YlGnBu", 
              annot=True,fmt= ".0f", linewidths=3, linecolor='white',
              annot_kws= { 'fontsize': 20,
                            'fontstyle' :"italic",
                             'linespacing' : 0.5,
                              'fontweight':'heavy'})      
plt.savefig('output/graph.png')