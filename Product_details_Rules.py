#Product Schema File 
#Defines the Pricing Rules and the Prices of each product.
#The product's price can be changed here manually

product_dict={'nsh':109.50,
              'stv':549.99,
              'cac':1399.99,
              'mch':30.00}#Price for each product

#Defining class for Discount rules
class Prod_rules:
    def __init__(self,cnt):
        self.invoice_dict=cnt
        
    def handle_key_error(self):
        #The funttion is to handle the error faced dur to Key eror while 
        #applying the rules to the total price..this enables us to enter the keys in any order
        
        #Alternatve way to avoid key error would be to update the 
        #Keys for dictionary Manually through for loop instead of Collections.counter
        main_keys=product_dict.keys()
        tmp={}
        
        for i in main_keys:
            tmp[i]=0
        
        for i in tmp.keys():
            if i in self.invoice_dict.keys():
                tmp[i]=self.invoice_dict[i]
        
        self.invoice_dict=tmp.copy()
        
                
        
    def product_rules(self,total_price):
    #Accepting total_price before discounts as paramenter
        
        try: 
            
            if self.invoice_dict['stv']>0 and self.invoice_dict['mch']>0:

                
                if self.invoice_dict['mch']>self.invoice_dict['stv']:
                    total_price=total_price-(self.invoice_dict['stv']*product_dict['mch'])
                if self.invoice_dict['mch']<=self.invoice_dict['stv']:
                    total_price=total_price-(self.invoice_dict['mch']*product_dict['mch'])
        
            
                
                
                
                
            if self.invoice_dict['nsh']>=3:
                total_price=total_price-((self.invoice_dict['nsh']/3)*product_dict['nsh'])
               
            
               

        
            if self.invoice_dict['stv']>4:
                total_price=total_price-(self.invoice_dict['stv']*50)
                
            
        
        except Exception as e:
            print(e)  
                    
        return total_price #returning total Price after discounts