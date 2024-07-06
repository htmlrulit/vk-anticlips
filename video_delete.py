import vk_api
import json
import re

def extract_video_ids(video_urls):
    video_ids = []
    for url in video_urls:
        match = re.search(r'video(-?\d+_\d+)', url)
        if match:
            video_ids.append(match.group(1))
    return video_ids

def delete_videos_from_vk(vk_session, video_ids):
    vk = vk_session.get_api()

    for video_id in video_ids:
        try:
            owner_id, video_id = video_id.split('_')
            vk.video.delete(owner_id=owner_id, video_id=video_id)
            print(f'Successfully deleted video {owner_id}_{video_id}')
        except Exception as e:
            print(f'Failed to delete video {video_id}: {e}')

if __name__ == "__main__":
    vk_session = vk_api.VkApi(token='')  # Укажите ваш токен доступа
    video_links_file = 'video_del.json'  # Укажите путь к файлу с ссылками на видео

    with open(video_links_file, 'r') as f:
        video_urls = json.load(f)

    video_ids = extract_video_ids(video_urls)
    delete_videos_from_vk(vk_session, video_ids)
