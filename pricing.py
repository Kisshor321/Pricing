import pandas as pd


products=pd.read_csv("C:\\Users\\uyyal\\products.csv")
sales=pd.read_csv("C:\\Users\\uyyal\\sales.csv")


merge=pd.merge(products,sales, on='sku', how='left')
merge['quantity_sold'] = merge['quantity_sold'].fillna(0)

merge['quantity_sold'] = merge['quantity_sold'].astype(int)


def apply_rules(row):
    current_price = float(row['current_price'])
    cost_price = float(row['cost_price'])
    stock = int(row['stock'])
    quantity_sold = int(row['quantity_sold'])
    new_price = current_price
    
    if stock<20 and quantity_sold>30:
        new_price=current_price*1.15
    
    elif stock >200 and quantity_sold==0:
        new_price=current_price*0.70
        
    elif stock>100 and quantity_sold<20:
        new_price=current_price*0.90
        
    min_price=cost_price*1.2
    if new_price < min_price:
        new_price=min_price
        
    return round(new_price,2)

merge["new_price"] = merge.apply(apply_rules, axis=1)

merge['old_price']=merge['current_price'].apply(lambda x:f'{round(x,2)} INR')
merge['new_price']=merge['new_price'].apply(lambda x:f'{round(x,2)} INR')

output=merge[['sku','old_price','new_price']]
output.to_csv("updated_prices.csv", index=False)

print(output)