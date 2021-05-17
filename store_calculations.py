# -*- coding: utf-8 -*-

from collections import Counter
from Product_details_Rules import Prod_rules
from Product_details_Rules import product_dict

#Defining class for Store Calculations and inputs
class Store:
    def __init__(self,product_dict):
        self.product_dict=product_dict #product_dict if the dictionary for 
                                        #product_id and product's price
        self.prod_list=[]  #Defining an empty list for the products that are scanned
        total_price=0 #initializing total price for payment as 0
        
        
        # function for updating price through GUI
    """def update_price(self,product_id):
        #self.product_dict=product_dict
        #self.product_id=product_id
        
        try :
            print("Enter the Product ID to modify it's Price")
            input(id_prod)
            print("Enter the new Price of the product")
            input(price) 
            self.product_dict[is_prod]=price
            
            return self.product_dict
        except Exception as e:
            print(e)"""
            
        #Function to scan producs and update the list of products that are being scanned in the main.py file
    def scan_product_price(self,product_id):
        #self.product_dict=product_dict
        #self.product_id=product_id
        
        
        self.prod_list.append(product_id)
        
        return self.prod_list
        
    #Function to calculate the count of each product and calculation of Price before and after discount
    def calculate_total_bill(self):
        #self.prod_list=prod_list
        #self.product_dict=product_dict
        total_price=0
        
        
        cnt=Counter(self.prod_list) #Counter function to calculate the count of each product scanned
        cnt=dict(cnt)  #Converting Counter Object to Dictionary
        
        print("Items scanned...Please verify {}".format(cnt))
        
        
        for i in cnt.keys():
            total_price=total_price+self.product_dict[i]*cnt[i]#Calculating before discount price
        
        print("Total Price before Discounts {}".format(total_price))
        rule_application=Prod_rules(cnt)  #Object of Class Prod_rules from Project_details_Rules
        
        rule_application.handle_key_error()
        total_price=rule_application.product_rules(total_price)  # Subtracting discounts from the Total price as per the rules defined in Prod_rules class
        return total_price #Final Price after discount
        