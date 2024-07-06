import os
import requests
import vk_api
import json

def upload_videos_to_vk_folder(vk_session, folder_path, group_id, output_file):
    vk = vk_session.get_api()
    uploaded_videos = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".mp4"):
            file_path = os.path.join(folder_path, filename)
            new_title = f"Название видео"  # название для видео
            print(f'Uploading {filename} as {new_title}...')

            try:
                video_info = vk.video.save(name=new_title, group_id=group_id, is_private=0)  # (0 - публичное, 1 - приватное)
                with open(file_path, 'rb') as video_file:
                    files = {'video_file': video_file}
                    response = requests.post(video_info['upload_url'], files=files)
                
                if response.status_code == 200:
                    print(f'Successfully uploaded {filename}')
                    uploaded_videos.append({
                        'title': new_title,
                        'link': f"https://vk.com/video{video_info['owner_id']}_{video_info['video_id']}"
                    })
                else:
                    print(f'Failed to upload {filename}: HTTP {response.status_code}')
                
            except Exception as e:
                print(f'Failed to upload {filename}: {e}')

    # Сохраняем ссылки на загруженные видео в файл
    with open(output_file, 'w') as f:
        json.dump(uploaded_videos, f, indent=4)
    print(f'Links to uploaded videos have been saved to {output_file}')

if __name__ == "__main__":
    vk_session = vk_api.VkApi(token='') # токен VK Admin https://vkhost.github.io
    folder_path = '' # папка с видео
    group_id = '' # id группы (положительное)
    output_file = 'uploaded_videos.json'  # файл с ссылками на видео

    upload_videos_to_vk_folder(vk_session, folder_path, group_id, output_file)
