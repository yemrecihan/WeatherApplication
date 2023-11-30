import requests

get_url = ('http://api.openweathermap.org/data/2.5/weather?')
appid = ('86807abef1a69bab4c6e4d80a7e3808b')
city = input('enter city name:')
def Change(x):
    return x - 273.15




get_response = requests.get(url=get_url,params=dict(q={city} ,APPID=appid))

if get_response.status_code ==200 :
    data = get_response.json()
    temp= data['main']['temp']
    desc = data ['weather'][0]['description']
    convert_kelvin_to_celsius= Change(temp)
    format_change= "{:.2f}".format(convert_kelvin_to_celsius)
    print(f'Temperature : {format_change} Celsius')
    print(f'Description : {desc}')
else:
    print('Error fetching weather data')



#print (get_response)
#print(get_response.json())



