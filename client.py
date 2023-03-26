
def upload_video_to_server(guest_name, phone_number):
    import requests
    import os
    # use post method to upload video to server
    current_dir = os.path.dirname(os.path.abspath(__file__))
    #open server.server file to get server ip
    with open(os.path.join(current_dir, 'server.server'), 'r') as f:
        server_ip = f.read()
        url = 'http://' + server_ip + '/upload_video.php'
        files = {'video': open(os.path.join(current_dir, 'test.mov'), 'rb')}
        #offer guest_name and phone_number
        data = {'guest_name': guest_name, 'phone_number': phone_number}
        r = requests.post(url, data=data, files=files)
        print(r.text)


if __name__ == '__main__':
    upload_video_to_server('진상혁', '010-7714-5470')
