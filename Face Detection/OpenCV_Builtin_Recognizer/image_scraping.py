import requests
from bs4 import BeautifulSoup
import urllib.request
from PIL import Image
import os
sachin_url = 'https://www.google.com/search?q=sachin+tendulkar&tbm=isch&ved=2ahUKEwji5-yyqJH3AhUu_TgGHaPMBK8Q2-cCegQIABAA&oq=sachin+t&gs_lcp=CgNpbWcQARgAMgcIABCxAxBDMgsIABCABBCxAxCDATIICAAQgAQQsQMyCwgAEIAEELEDEIMBMggIABCABBCxAzIECAAQQzIFCAAQgAQyCwgAEIAEELEDEIMBMgUIABCABDIFCAAQgAQ6CggAELEDEIMBEENQighYmxNgjiBoAHAAeACAAX2IAYsHkgEDNi4zmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=AedWYqLjEK764-EPo5mT-Ao&bih=754&biw=1536'

def get_images(url,folder_name):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    images_tags = soup.find_all('img')
    links = [image_tag['src'] for image_tag in images_tags]

    count = 0
    for image_tag in images_tags:
        count += 1
        if image_tag['src'].split('.')[-1] != 'gif':
            urllib.request.urlretrieve(image_tag['src'],folder_name+'/image_'+str(count)+'.png')
        if count == 60:
            break

url_name_list = [['Sachin','https://www.google.com/search?q=sachin+tendulkar&tbm=isch&ved=2ahUKEwji5-yyqJH3AhUu_TgGHaPMBK8Q2-cCegQIABAA&oq=sachin+t&gs_lcp=CgNpbWcQARgAMgcIABCxAxBDMgsIABCABBCxAxCDATIICAAQgAQQsQMyCwgAEIAEELEDEIMBMggIABCABBCxAzIECAAQQzIFCAAQgAQyCwgAEIAEELEDEIMBMgUIABCABDIFCAAQgAQ6CggAELEDEIMBEENQighYmxNgjiBoAHAAeACAAX2IAYsHkgEDNi4zmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=AedWYqLjEK764-EPo5mT-Ao&bih=754&biw=1536'],
['Dhoni','https://www.google.com/search?q=dhoni&tbm=isch&ved=2ahUKEwiX0tG5qJH3AhUQgWMGHW3oA4IQ2-cCegQIABAA&oq=dhoni&gs_lcp=CgNpbWcQAzIHCAAQsQMQQzIKCAAQsQMQgwEQQzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyBAgAEEMyBwgAELEDEEMyBAgAEEMyBAgAEEM6CAgAEIAEELEDOgUIABCABDoICAAQsQMQgwFQ6QZYpA1gtRJoAHAAeACAAV-IAZoEkgEBNpgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=D-dWYteOH5CCjuMP7dCPkAg&bih=754&biw=1536'],
['Yuvraj','https://www.google.com/search?q=yuvraj&tbm=isch&ved=2ahUKEwiIgteGq5H3AhW0rmMGHe1cCosQ2-cCegQIABAA&oq=yuvraj&gs_lcp=CgNpbWcQAzIKCAAQsQMQgwEQQzIICAAQgAQQsQMyBwgAELEDEEMyBAgAEEMyBQgAEIAEMgUIABCABDIECAAQQzIFCAAQgAQyBQgAEIAEMgQIABBDOgsIABCABBCxAxCDAToGCAAQChAYUI8IWOMeYPUgaAFwAHgAgAFaiAGtBZIBATiYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=yelWYsj5ObTdjuMP7bmp2Ag&bih=754&biw=1536'],
['Raina','https://www.google.com/search?q=raina&tbm=isch&ved=2ahUKEwiTu72kq5H3AhWT_jgGHWqJDVcQ2-cCegQIABAA&oq=raina&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyBAgAEEMyBAgAEEMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgcIABCxAxBDOgsIABCABBCxAxCDAToICAAQsQMQgwE6CggAELEDEIMBEEM6BAgAEANQ_gdY7yNg8SxoBHAAeAKAAbsBiAHyCZIBAzguNJgBAKABAaoBC2d3cy13aXotaW1nsAEAwAEB&sclient=img&ei=COpWYpOXG5P94-EP6pK2uAU&bih=754&biw=1536'],
['Dravid','https://www.google.com/search?q=dravid&tbm=isch&ved=2ahUKEwi8pb-vq5H3AhVw_jgGHbdZDRIQ2-cCegQIABAA&oq=dravid&gs_lcp=CgNpbWcQAzIFCAAQgAQyCAgAEIAEELEDMgUIABCABDIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAELEDEEM6BAgAEEM6CAgAELEDEIMBOgsIABCABBCxAxCDAVCuBlisG2DOHGgAcAB4AIABYogB6gSSAQE3mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=H-pWYvyZIfD84-EPt7O1kAE&bih=754&biw=1536']]

for index in range(len(url_name_list)):
    folder_name = 'images/'+url_name_list[index][0]
    print(url_name_list[index][0])
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    get_images(url_name_list[index][1],folder_name)
