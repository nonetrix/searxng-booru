import json

categories = ['images', 'web']
paging = True

def request(query, params):
    params['url'] = 'https://e621.net/posts.json?tags=' + query + '&limit=20&page=' + str(params['pageno'])

    return params


def response(resp):
    results = []
    tags = ""
    data = json.loads(resp.text)


    for post in data['posts']:

        if post['file']['url'] != None:
            for tag in post['tags']['general']:
                tags += tag + " "
                results.append({
                    'template': 'images.html',
                    'url': 'https://e621.net/posts/' + str(post['id']),
                    'thumbnail_src': post['preview']['url'],
                    'img_src': post['file']['url'],
                    'title': tags,
                    'content': tags
                })

    return results