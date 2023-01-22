import geopy

def get_geolocation():
    try:
        # Create the GeoLocator object
        locator = geopy.geocoders.Nominatim(user_agent="geoapiExercises")
        
        # Get the current location
        location = locator.geocode("")
        
        # Extract latitude and longitude
        latitude = location.latitude
        longitude = location.longitude
        
        return latitude, longitude
    
    except:
        print("No coordinates found")

latitude, longitude = get_geolocation()
print(f"Latitude: {latitude}, Longitude: {longitude}")
