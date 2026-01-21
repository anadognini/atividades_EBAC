#!/usr/bin/env python
# coding: utf-8

# In[9]:


import psycopg2 as pg2
import pandas as pd


# ### Calcule a média por nome e sobrenome do ator da seguintes variáveis:
# - rental_duration
# - rental_rate
# - length
# - replacement_cost

# In[10]:


conn = pg2.connect(host='localhost', port=5432, dbname='dvdrental',
                  user='postgres', password='senha')
cur = conn.cursor()


# In[11]:


cur.execute('''SELECT 
first_name,
last_name,
AVG(rental_duration) AS avg_rental_duration,
AVG(rental_rate) AS avg_rental_rate,
AVG(length) AS avg_length,
AVG(replacement_cost) AS avg_replacement_cost
FROM 
(SELECT * FROM actor AS x
LEFT JOIN film_actor AS y
ON x.actor_id = y.actor_id
LEFT JOIN film AS z
ON y.film_id = z.film_id
) AS sub
GROUP BY 
first_name,
last_name
ORDER BY 
avg_replacement_cost;
''')


# In[12]:


conn.commit()
data = cur.fetchall()
colnames = [desc.name for desc in cur.description]


# In[13]:


df = pd.DataFrame(data, columns=colnames)
df.head()


# ### Calcule a soma de amount (preço total do aluguel) por nome, sobrenome e email do cliente (customer) e indique os 10 clientes que mais gastaram e os 10 que menos gastaram.

# In[14]:


cur.execute('''SELECT
x.first_name,
x.last_name,
x.email,
SUM(y.amount) AS total_spent
FROM customer AS x
LEFT JOIN payment AS y
ON x.customer_id = y.customer_id
GROUP BY
x.first_name,
x.last_name,
x.email
ORDER BY
total_spent DESC
LIMIT 10;
''')


# In[15]:


conn.commit()
mais_gataram = cur.fetchall()
colnames = [desc.name for desc in cur.description]


# In[16]:


df = pd.DataFrame(mais_gataram, columns=colnames)
df.head()


# In[17]:


cur.execute('''SELECT
x.first_name,
x.last_name,
x.email,
SUM(y.amount) AS total_spent
FROM customer AS x
LEFT JOIN payment AS y
ON x.customer_id = y.customer_id
GROUP BY
x.first_name,
x.last_name,
x.email
ORDER BY
total_spent ASC
LIMIT 10;
''')


# In[18]:


conn.commit()
menos_gataram = cur.fetchall()
colnames = [desc.name for desc in cur.description]


# In[19]:


df = pd.DataFrame(menos_gataram, columns=colnames)
df.head()


# In[20]:


cur.close()
conn.close()

