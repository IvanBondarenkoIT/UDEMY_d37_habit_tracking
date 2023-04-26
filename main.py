import requests
import datetime
import config


def main():
    pixela_endpoint = 'https://pixe.la/v1/users'
    user_params = {
        'token': config.TOKEN,
        'username': config.USERNAME,
        'agreeTermsOfService': 'yes',
        'notMinor': 'yes',
    }
    # response = requests.post(url=pixela_endpoint, json=user_params)
    # print(response.text)

    graph_endpoint = f'{pixela_endpoint}/{config.USERNAME}/graphs'

    graph_config = {
        'id': config.GRAPH_ID,
        'name': 'Blind Typing',
        'unit': 'Min',
        'type': 'int',
        'color': 'ajisai'
    }

    headers = {
        'X-USER-TOKEN': config.TOKEN,
    }

    # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    # print(response.text)

    pixel_endpoint = f'{pixela_endpoint}/{config.USERNAME}/graphs/{config.GRAPH_ID}'

    # pixel_date = datetime.datetime.now()
    pixel_date = datetime.datetime(year=2023, month=4, day=25)

    pixel_config = {
        'date': pixel_date.strftime('%Y%m%d'),
        'quantity': '10',
    }

    # response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
    # print(response.text)

    update_date = datetime.datetime(year=2023, month=4, day=25)
    update_pixel = f'{pixela_endpoint}/{config.USERNAME}/graphs/{config.GRAPH_ID}/{update_date.strftime("%Y%m%d")}'
    update_config = {
        'quantity': '4',
    }

    # response = requests.put(url=update_pixel, json=update_config, headers=headers)
    # print(response.text)

    delete_date = datetime.datetime(year=2023, month=4, day=25)
    delete_pixel = f'{pixela_endpoint}/{config.USERNAME}/graphs/{config.GRAPH_ID}/{delete_date.strftime("%Y%m%d")}'

    response = requests.delete(url=delete_pixel, headers=headers)
    print(response.text)


if __name__ == '__main__':
    main()


