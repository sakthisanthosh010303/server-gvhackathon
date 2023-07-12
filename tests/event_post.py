# Author: Sakthi Santhosh
# Created on: 14/01/2023
def main() -> int:
    from base64 import b64encode
    from json import dumps
    from requests import post
    from requests.exceptions import ConnectionError
    from uuid import uuid4

    from constants import BASE_URL

    try:
        DATA = {
            "animal_class": "leopard",
            "device_id": "4b7cf20e-b73a-4d89-8210-773eab7dc702",
            "image": b64encode(open("./tests/test.jpg", "rb").read()).decode("utf-8")
        }

        request_handle = post(
            url=BASE_URL + "add_event",
            data=dumps(DATA),
            headers={"Content-Type": "application/json"}
        )

        print("Response:", request_handle.status_code)
        request_handle.close()
    except FileNotFoundError:
        print("Error: Image file not found.")
        return 1
    except ConnectionError:
        print("Error: Failed to establish a new connection to \"%s\"."%(BASE_URL))
        return 1
    except:
        print("Error: Something went wrong.")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())
