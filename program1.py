from flask import Flask
import requests
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.FileHandler("demologfile.log")

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)

logger.addHandler(ch)

app = Flask(__name__)


@app.route('/<macadd>')
def mac(macadd):
  try:
    MAC_URL = 'https://api.macaddress.io/v1?apiKey=at_oXN3OWKwhQXAooP0Jwc6UobnrGTCa&output=json&search=%s'
    r = requests.get(MAC_URL % macadd)
    logger.info('Requested the website')
    a = r.json()
    logger.info('Data Fetched')
    if len(a['vendorDetails']['companyName']) != 0:
      logger.info('MAC Address is valid')
      return  a['vendorDetails']['companyName']
    else:
      logger.info('User MAC adress not Correct')
      return 'The MAC address does not belong to any registered block.'
  except KeyError as e:
    logger.exception('User Inputed MAC formate was Incorrect')
    return 'Invalid MAC Address'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)



