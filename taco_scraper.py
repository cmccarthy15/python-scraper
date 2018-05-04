import requests

class TacoBellScraper(object):

  def fetch_data(self, zip_code):
    url = 'https://www.tacobell.com/store-finder/findStores?q={}'.format(zip_code)
    zipcode_results = requests.get(url)
    return zipcode_results.json()['nearByStores']

  def parse_record(self, record):
    formatted_record = {
      'store_id': record['storeNumber'],
      'latitude': record['geoPoint']['latitude'],
      'longitude': record['geoPoint']['longitude'],
      'address': record['address']['formattedAddress']
    }
    return formatted_record

  # def uniquify_records(self, records):
  # nice-to-have later
  #   pass

  def process(self):
    zipcodes = [10003, 33477]
    all_results = []
    for zipcode in zipcodes:
      for record in self.fetch_data(zipcode):
        all_results.append(self.parse_record(record))
    return all_results
