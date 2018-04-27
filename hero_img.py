import requests
import urllib
import os
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}


# 下载皮肤
def get_herolist():
    # 英雄列表数据URL
    url = 'http://pvp.qq.com/web201605/js/herolist.json'
    # 构造皮肤下载的URL
    base_skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/%d/%d-bigskin-%d.jpg'
    # 构造头像下载的URL
    base_avatar_url = 'http://game.gtimg.cn/images/yxzj/img201606/heroimg/%d/%d.jpg'

    response = requests.get(url, headers)
    herolist_json = response.json()
    # 保存英雄皮肤的根路径
    base_skin_path = 'skin'
    # 保存英雄头像的根路径
    base_avatar_path = 'avatar'

    # 判断英雄皮肤根路径是否存在，如果不存在则创建
    path_exists(base_skin_path)
    # 判断英雄头像根路径是否存在，如果不存在则创建
    path_exists(base_avatar_path)

    for herolist in herolist_json:
        # 英雄名
        cname = herolist['cname']
        print(cname)
        # 英雄编号
        ename = herolist['ename']
        # 英雄皮肤名
        skin_names = herolist['skin_name'].split('|')
        for index, skin_name in enumerate(skin_names):
            # 构造好的皮肤地址
            skin_url = base_skin_url % (ename, ename, index + 1)
            # 构造好的头像地址
            avatar_url = base_avatar_url % (ename, ename)
            print('  >>> 头像地址：' + avatar_url)
            print('  >>> 皮肤名：' + skin_name + ' 皮肤地址：' + skin_url)

            # 保存的皮肤文件名：英雄名-皮肤名.jpg
            skin_file_name = cname + '-' + skin_name + '.jpg'
            # 下载皮肤
            download(skin_url, base_skin_path, skin_file_name)

            # 保存的头像文件名：英雄名.jpg
            avatar_file_name = cname + '.jpg'
            # 下载头像
            download(avatar_url, base_avatar_path, avatar_file_name)


# 下载英雄皮肤或者头像
def download(url, base_path, file_name):
    save_path = base_path + '/' + file_name
    # 如果皮肤文件不存在才下载
    if not os.path.exists(save_path):
        urllib.request.urlretrieve(url, save_path)
    # 防止下载过快
    time.sleep(0.1)


# 判断路径是否存在
def path_exists(path):
    # 如果保存文件的路径不存在就自动创建
    if not os.path.exists(path):
        os.mkdir(path)


if __name__ == '__main__':
    get_herolist()
