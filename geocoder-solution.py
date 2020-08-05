import geocoder

spots = [
  'Space Needle',
  'Crater Lake',
  'Golden Gate Bridge',
  'Yosemite National Park',
  'Las Vegas, Nevada',
  'Grand Canyon National Park',
  'Aspen, Colorado',
  'Mount Rushmore',
  'Yellowstone National Park',
  'Sandpoint, Idaho',
  'Banff National Park',
  'Capilano Suspension Bridge'
]

# g = geocoder.arcgis(spots)

locationList = []

for location in spots:
  print("{} is in: {}".format(location, geocoder.arcgis(location).latlng))
  # print(geocoder.arcgis(location).latlng)


