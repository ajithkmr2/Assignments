from model import Currency
import view

def showPrice(query_value):
   #gets list of all Currency objects
   currency_price = Currency.getCurrencyData(query_value)
   #calls view
   return view.showData(currency_price)

def start():
   view.startView()
   input_option = input('Enter [INR / EUR / CAD / AUD / JPY / ALL] :')
   return showPrice(input_option)

if __name__ == "__main__":
   #calls controller function
   start()