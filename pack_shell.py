import subprocess

VERSION_CODE = '1.0.0'


def run_flet_pack():
    command = [
        'flet', 'pack',
        '-v',
        # '-i', 'logo.ico',
        '-n', 'main_back',
        # '--add-data=./src:./src',
        '--product-name', 'WechatPartner',
        '--file-description', 'wechat partner',
        '--product-version', '1.0.0',
        '--file-version', '1.0.0',
        '--company-name', 'My Company',
        '--copyright', 'Copyright 2024',
        '--bundle-id', 'com.wechat.wechatpartner',
        'main.py'
    ]

    subprocess.run(command)


if __name__ == '__main__':
    run_flet_pack()
