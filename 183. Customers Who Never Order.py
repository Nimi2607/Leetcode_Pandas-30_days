import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customer_not_ordering = customers[~customers['id'].isin(orders['customerId'])]
    customer_not_ordering = customer_not_ordering[['name']].rename(columns = {'name': 'Customers'})
    return customer_not_ordering
    
