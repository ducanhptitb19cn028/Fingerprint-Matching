import cv2
import requests
import time
import shutil
import json

headers = {'Authorization': 'f134382194a844c8bb589af58ef283e9'}
file_list = ['input/test.png', 'input/test.png', 'input/test.png']
params = {
    'lang': 'en',
    'convert_to': 'image-backgroundremover'
}

api_url = 'https://api.backgroundremover.app/v1/convert/'
results_url = 'https://api.backgroundremover.app/v1/results/'


def download_file(url, local_filename):
    with requests.get("https://api.backgroundremover.app/%s" % url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return local_filename


def convert_files(api_url, params, headers):
    files = [eval(f'("files", open("{file}", "rb"))') for file in file_list]
    print(files)
    r = requests.post(
        url=api_url,
        files=files,
        data=params,
        headers=headers
    )
    return r.json()


def get_results(params):
    if params.get('error'):
        return params.get('error')
    r = requests.post(
        url=results_url,
        data=params
    )
    data = r.json()
    finished = data.get('finished')
    while not finished:
        if int(data.get('queue_count')) > 0:
            print('queue: %s' % data.get('queue_count'))
        time.sleep(5)
        results = get_results(params)
        print(results)
        results = json.dumps(results)
        if results:
            break
    if finished:
        print(data.get('files'))
        for f in data.get('files'):
            print(f.get('url'))
            download_file("%s" % f.get('url'), "%s" % f.get('filename'))
        return {"finished": "files downloaded"}
    return r.json()


get_results(convert_files(api_url, params, headers))

