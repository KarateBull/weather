#!/usr/bin/env python3

from typing import Tuple

import requests
import pgeocode

DEFAULT_ZIP_CODE = '04103'

def get_lat_long(zipcode) -> Tuple[str, str]:
    nomi = pgeocode.Nominatim('us')
    location_data = nomi.query_postal_code(zipcode)

    latitude = location_data.latitude
    longitude = location_data.longitude
    return latitude, longitude

def get_weather_by_zip_code(zip_code: str):
    latitude, longitude = get_lat_long(zip_code)
    response = requests.get(
        url=f'https://api.weather.gov/points/{latitude},{longitude}',
        headers = {'User-Agent': 'MyWeatherApp/1.0'}
    )
    response.raise_for_status()

    weather_data = response.json()
    weather_properties = weather_data['properties']
    pass

def get_zip_code():
    code = input(f"Enter your zip code [{DEFAULT_ZIP_CODE}]: ").strip()
    if not code:
        code = DEFAULT_ZIP_CODE
    return code

def main():
    area_code = get_zip_code()
    print(get_weather_by_zip_code(area_code))

if __name__ == '__main__':
    main()
