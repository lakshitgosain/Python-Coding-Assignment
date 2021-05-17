from store_calculations import Store
from Product_details_Rules import product_dict



stre=Store(product_dict) #oject of Store class with product dictionary(product prices as class name)

while True:
    
    try:
        prd_id=input("Enter Product ID(Enter Exit to calculate Total): ")
        prd_id=prd_id.lower()
        if prd_id=='nsh' or prd_id=='stv' or prd_id=='mch' or prd_id=='cac':
            lst=stre.scan_product_price(prd_id)
            
        else:
            
            if prd_id=='exit':
                break
            print('Enter a valid Code')
        
            
    
    except Exception as e:
        print(e)
    
    
total_payment=stre.calculate_total_bill()
print("Total price after discount(if applicable) {}".format(round(total_payment,4)))
        
        
        
            
        
        