import json

categories = ['images', 'web']
paging = True

def request(query, params):
    params['url'] = 'https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&limit=20&tags=' + query + '&pid=' + str(params['pageno'] - 1)

    return params


def response(resp):
    results = []
    data = json.loads(resp.text)

    for post in data['post']:
        results.append({
            'template': 'images.html',
            'url': "https://gelbooru.com/index.php?page=post&s=view&id=" + str(post['id']), 
            'thumbnail_src': post['preview_url'], 
            'img_src': post['file_url'], 
            'title': post['tags'], 
            'content': post['tags']
        })

    return results