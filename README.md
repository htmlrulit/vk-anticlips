# НАДСТРОЙКИ
    new_title = f"Название видео"  # название для видео
    video_info = vk.video.save(name=new_title, group_id=group_id, is_private=0)  # (0 - публичное, 1 - приватное)
    vk_session = vk_api.VkApi(token='') # токен VK Admin https://vkhost.github.io
    folder_path = '' # папка с видео
    group_id = '' # id группы (положительное)
    output_file = 'uploaded_videos.json'  # файл с ссылками на видео
    
