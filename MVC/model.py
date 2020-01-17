import json
import requests

class Currency(object):
   def __init__(self, currency_name = None, currency_value = None):
      self.currency_name = currency_name
      self.currency_value = currency_value

   def data(self):
      return ("%s : %s" % (self.currency_name,self.currency_value))
		
   @classmethod
   #Collect currency live price from API and return it to controller
   def getCurrencyData(self,query_value):
      result = []
      if query_value.lower() == 'all':
      	url = 'http://apilayer.net/api/live?access_key=ab6ff40974c8c5147720c67a4c42db90&currencies=INR,EUR,CAD,AUD,JPY'
      else:
      	url = 'http://apilayer.net/api/live?access_key=ab6ff40974c8c5147720c67a4c42db90&currencies='+query_value

      try:
        reply_from_api = requests.get(url)
        json_list = json.loads(reply_from_api.text)
        for key,value in json_list['quotes'].items():
           currency = Currency(key, value)
           result.append(currency)
      except:
           currency = Currency(query_value,'Invalid currency name')
           result.append(currency)
           return result
           
      return result