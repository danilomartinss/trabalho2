
# coding: utf-8

# In[ ]:

# Import pandas as pd
import pandas as pd

# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Import output_notebook and show from bokeh.io
from bokeh.io import output_notebook, show

# Import the ColumnDataSource class from bokeh.plotting
from bokeh.plotting import ColumnDataSource

# Import HoverTool from bokeh.models
from bokeh.models import HoverTool

data = pd.read_csv("/home/danilo/Documentos/UFRN/2017.1/BigData/CO2_passenger_cars_v12.csv", low_memory=False, sep="\t")

data = data.fillna('')

source = ColumnDataSource(data)

f1 = figure(width=600, height=600, title = "Relação Potencia vs Emissão de CO2",x_axis_label='ep(KW)', y_axis_label='e(g/km)')

# Create a HoverTool object: hover
hover = HoverTool(tooltips=[('Comercial Name','@Cn'), ('Make', '@Mk')])

# Add the HoverTool object to figure p
f1.add_tools(hover)

f1.circle(x=data['ep (KW)'], y=data['e (g/km)'], size=5, alpha = 0.8, source = source)

# Print inline the figure
output_notebook()
show(f1)


# In[4]:

f2 = figure(width=600, height=600, title = "Relação Peso vs Emissão de CO2",x_axis_label='m (kg)', y_axis_label='e(g/km)')

# Create a HoverTool object: hover
hover = HoverTool(tooltips=[('Comercial Name','@Cn'), ('Make', '@Mk')])

# Add the HoverTool object to figure p
f2.add_tools(hover)

f2.circle(x=data['m (kg)'], y=data['e (g/km)'], size=5, alpha = 0.8, source = source)

# Print inline the figure
show(f2)


# In[8]:

registration_cars = data['r'].groupby(data['Man']).sum()

registration_cars = registration_cars[registration_cars.notnull()]

average_emisson = data['e (g/km)'].groupby(data['Man']).mean()

average_emisson = average_emisson[average_emisson.notnull()]

average_mass = data['m (kg)'].groupby(data['Man']).mean()

average_mass = average_mass[average_mass.notnull()]

f3 = figure(width=600, height=600, title = "Relação Média Peso vs Média Emissão de CO2",x_axis_label='mean m (kg)', y_axis_label='mean e(g/km)')

# Create a HoverTool object: hover
hover = HoverTool(tooltips=[('Comercial Name','@Cn'), ('Make', '@Mk')])

# Add the HoverTool object to figure p
f3.add_tools(hover)

f3.circle(x=average_mass, y=average_emisson, size=5, alpha = 0.8, source = source)

# Print inline the figure
show(f3)

