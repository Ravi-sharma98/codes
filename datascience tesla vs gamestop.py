#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install nbformat')


# In[3]:


get_ipython().system('pip install bs4')


# In[4]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[6]:


import warnings
warnings.filterwarnings('ignore', category=FutureWarning)


# In[7]:


def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()


# In[8]:


t1=yf.Ticker('TSLA')


# In[9]:


tesla_data=t1.history(period='max')


# In[10]:


tesla_data.reset_index(inplace=True)
tesla_data.head(5)


# In[13]:


url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data=requests.get(url).text
html_data


# In[14]:


beautiful_soup=BeautifulSoup(html_data,'html5lib')


# In[49]:


#tesla_revenue=pd.DataFrame(columns=['date','Revenue'])


# In[50]:


t1=pd.read_html(url)


# In[60]:


tesla_revenue=pd.DataFrame(t1[1])
tesla_revenue.head(5)


# In[63]:


tesla_revenue.rename(columns={"Tesla Quarterly Revenue(Millions of US $)":'Date',"Tesla Quarterly Revenue(Millions of US $).1":'Revenue'},inplace=True)
tesla_revenue.head(5)


# In[68]:


tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")
tesla_revenue.dropna(inplace=True)


# In[69]:


tesla_revenue.head(5)


# In[70]:


tesla_revenue.tail(5)


# ## Game stop

# In[71]:


g=yf.Ticker('GME')


# In[123]:


gme_data=g.history(period='max')


# In[73]:


type(game_data)


# In[126]:


gme_data.reset_index(inplace=True)
gme_data.head(5)


# In[75]:


url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"


# In[91]:


html_data=requests.get(url).text


# In[92]:


soup=BeautifulSoup(html_data, 'html5lib')


# In[93]:


gme_revenue=pd.DataFrame(columns=['Date','revenue'])


# In[105]:


for row in soup.find_all('tbody')[1].find_all('tr'):
    col= row.find_all('td')
    date=col[0].text
    revenue=col[1].text
    
    gme_revenue=gme_revenue.append({'Date':date,'Revenue':revenue},ignore_index=True)


# In[106]:


gme_revenue.head(5)


# In[107]:


gme_revenue.drop('revenue',axis=1)


# In[108]:


gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"")
gme_revenue


# In[109]:


gme_revenue.drop('revenue',axis=1)


# In[116]:


gme_revenue.dropna(subset=['Revenue'],inplace=True)
gme_revenue.dropna(subset=['Date'],inplace =True)


# In[119]:


gme_revenue.shape
del gme_revenue['revenue']


# gme_revenue.tail(5)

# In[120]:


gme_revenue.tail(5)


# In[121]:


make_graph(tesla_data, tesla_revenue, 'Tesla')


# In[127]:


make_graph(gme_data, gme_revenue, 'GameStop')


# In[ ]:




