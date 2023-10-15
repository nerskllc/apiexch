import pyktok as pyk
import os
import csv

def get_video(item_url):
    downloader_msg = ""
    item_csv_name = item_url.split('/')[-3]
    item_vid_name = item_url.split('/')[-1].split('?')[0]
    try:        
        # Download the TikTok video to the `deliveries` directory.
        #pyk.save_tiktok(item_url, True, os.path.join('deliveries', f'{item_vid_name}.mp4'))

        # Download the TikTok CSV file to the `deliveries` directory.
        #pyk.save_tiktok(item_url, True, os.path.join('deliveries', f'{item_csv_name}.csv'))
        
        downloader_msg = f'Sucessful Download'
    except Exception as e:
        downloader_msg = str(e)
    
    video_data = []
    
    with open(os.path.join('deliveries', f'{item_csv_name}.csv'), 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            video_data.append(dict(row))
                
    return {
                'status': downloader_msg,
                 'video_path': os.path.join('deliveries', f'{item_vid_name}.mp4'),
                 'video_data': video_data,
            }
    
    
    
# # Usage example:
# if __name__ == '__main__':
#      video_url = 'https://www.tiktok.com/@tiktok/video/7106594312292453675?is_copy_url=1&is_from_webapp=v1'
#      msg = get_video(video_url)
#      print(msg)
