#!/usr/bin/python
purchase_amount_of_shares = 2000 * 40.00
sale_amount_of_shares = 2000 * 42.75
broker_comission_purchase = purchase_amount_of_shares * 0.03
broker_comission_sale = sale_amount_of_shares * 0.03
profit = (sale_amount_of_shares - purchase_amount_of_shares)- (broker_comission_sale + broker_comission_purchase)
print("Purchase amount of shares {}\nBroker comission of purchase {}\nSale amount of shares {}\nBroker comission of sale {}\nProfit {}".format(purchase_amount_of_shares, broker_comission_purchase, sale_amount_of_shares, broker_comission_sale, profit))