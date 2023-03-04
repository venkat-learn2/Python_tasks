stock_data=[
{
"id":1,
"name":"mango",
"qty":20,
"price":10
},
{
"id":2,
"name":"orange",
"qty":20,
"price":10
},
{
"id":3,
"name":"grapes",
"qty":20,
"price":15
},
{
"id":4,
"name":"apple",
"qty":20,
"price":20
}
]
currency_format=[1,2,5,10,20,50,100]
print("1-mango,2-orange,3-grapes,4-apple")
flavour=int(input("Enter your Flavour Number:"))
qty=int(input("Enter the quantity:"))
amt=int(input("Enter your Amount:"))
def process_calculation(flavour,qty,amt,stock_data,currency_format):
    if qty>20:
        print("Only 20 Qty available.please enter 20 or below!")
        return
    else:
        get_flavour_price=[x['price'] for x in stock_data if x['id']==int(flavour)]
        total_purchased_price=qty*get_flavour_price[0]
        remaining_amt=amt-total_purchased_price
        # print("remaining_amt:",remaining_amt)
        if remaining_amt>0:
            currency_format.sort()
            currency_format=currency_format[::-1]
            get_change_amount=get_change(currency_format,remaining_amt)
        else:
            print("given Amount is insufficient!")

def get_change(currency_format,remaining_amt):
	return_arr=[]
	for i in currency_format:
		if remaining_amt in currency_format:
			data={"amount":remaining_amt,"currency_qty":1}
			return_arr.append(data)
			break
		if (remaining_amt>i):
			if (remaining_amt%i)==0:
				currency_qty=(remaining_amt//i)
				return_amt=i
				data={"amount":return_amt,"currency_qty":currency_qty}
				return_arr.append(data)
				break
			else:
				return_amt=i
				currency_qty=(remaining_amt//i)
				get_rem=(remaining_amt%i)
				data={"amount":return_amt,"currency_qty":currency_qty}
				# print("data:",data)
				return_arr.append(data)
				remaining_amt=get_rem
	print("return:",return_arr)

call_func=process_calculation(flavour,qty,amt,stock_data,currency_format)

print("added")