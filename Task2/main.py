from ya_disk import YandexDisk


if __name__ == '__main__':
    path = ['mem.jpg', 'test.txt']
    token = ''
    ya = YandexDisk(token=token)
    ya.upload_list_files_to_disk(path)