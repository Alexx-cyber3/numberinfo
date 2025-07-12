import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def phone_info(number: str, region: str = None):
    # Parse the phone number
    phone_number = phonenumbers.parse(number, region)
    
    # Get country/region
    country = geocoder.description_for_number(phone_number, 'en')
    # Get carrier
    sim_carrier = carrier.name_for_number(phone_number, 'en')
    # Get timezone
    time_zones = timezone.time_zones_for_number(phone_number)
    # Is valid
    is_valid = phonenumbers.is_valid_number(phone_number)
    
    return {
        'number': number,
        'country': country,
        'carrier': sim_carrier,
        'timezones': list(time_zones),
        'is_valid': is_valid
    }

if __name__ == "__main__":
    num = input("Enter phone number (with country code): ")
    region = input("Enter region code (or leave blank): ")
    info = phone_info(num, region if region else None)
    print(info)