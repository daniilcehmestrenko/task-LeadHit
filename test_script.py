import json
import requests


def main():
    with open('test_request_data.json') as f:
        file = json.load(f)

        for form_data in file['forms']:
            request = requests.post(
                    'http://127.0.0.1:8000/get_form/',
                    json=form_data
                )
            print(request.text)

if __name__ == '__main__':
    main()
