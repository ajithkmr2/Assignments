from model import Currency

def showData(currency_data):
   print('Currency live exchange price based on USD:')
   for item in currency_data:
      print(item.data())

def startView():
   print('--Welcome to Currency App--')
   print('Enter currency name to get live exchange price based on USD:')
