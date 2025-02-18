import requests


def api_get_data():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    data=response.json()
    
    if data["success"] and "data" in data:
        useralldata=data["data"]
        username=useralldata["login"]["username"]
        usercountry=useralldata["location"]["country"]
        
        return username, usercountry
    
    else:
        raise Exception("Failed to fetch data from API")
    
    
def main():
      try:
          username, usercountry=api_get_data()
          print(f"Username: {username}")
          print(f"User Country: {usercountry}")
      except Exception as e:
          print(f"Error: {str(e)}")


if __name__ =="__main__":
    main()
              