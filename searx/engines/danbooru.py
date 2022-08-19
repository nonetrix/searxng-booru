import json

categories = ['images', 'web']
paging = True

def request(query, params):
    params['url'] = 'https://danbooru.donmai.us/posts.json?limit=20&tags=' + query + '&page=' + str(params['pageno'])

    return params


def response(resp):
    results = []
    data = json.loads(resp.text)

    for post in data:
        if "id" in post:
            results.append({
                'template': 'images.html',
                'url': "https://danbooru.donmai.us/posts/" + str(post['id']), 
                'thumbnail_src': post['preview_file_url'], 
                'img_src': post['file_url'], 
                'title': post['tag_string'], 
                'content': post['tag_string']
            })

    return results