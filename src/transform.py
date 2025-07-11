def parse_weather(json_data):

    return{
        "ciudad": json_data["name"],
        "temperatura": json_data["main"]["temp"],
        "humedad": json_data["main"]["humidity"],
        "presion": json_data["main"]["pressure"],
        "clima": json_data["weather"][0]["description"],
        "viento": json_data["wind"]["speed"],
        "timestamp": json_data["dt"]
    }