import requests

import actions
import tokens

def main():
    url = "https://api.artifactsmmo.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)

    print(response.json())

    
    actions.moveFrani(-1, 0)



if __name__ == "__main__":
    main()