# Pricing rules

products.csv`: Input file containing product catalog data.
sales.csv`: Input file with sales data from the last 30 days.

Pricing Rules 
1. **Low Stock & High Demand**  
   - Condition: `stock < 20` and `quantity_sold > 30`  
   - Action: Increase price by **15%**

2. **Dead Stock**  
   - Condition: `stock > 200` and `quantity_sold == 0`  
   - Action: Decrease price by **30%**

3. **Overstocked Inventory**  
   - Condition: `stock > 100` and `quantity_sold < 20`  
   - Action: Decrease price by **10%**

4. **Minimum Profit Rule (Always Applied)**  
   - Ensure new price ≥ `cost_price * 1.2`  
   - If not, reset it to `cost_price * 1.2`  
   - All final prices rounded to **2 decimal places**
  
   - **Merge**
   -   sku    name  current_price  cost_price  stock  quantity_sold
0  A123  Item A         649.99         500    150             10
1  B456  Item B         699.00         550     15             35
2  C789  Item C         999.00         500    250              0


**final output**
 sku   old_price   new_price
0  A123  649.99 INR   600.0 INR
1  B456   699.0 INR  803.85 INR
2  C789   999.0 INR   699.3 INR


