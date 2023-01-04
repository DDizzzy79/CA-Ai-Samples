import cv2
pic_num = 0

for i in range(1,5):
    print(f"!!!!!!!!!!starting video {i}!!!!!!!!!!")
    video = cv2.VideoCapture(f'sample{i}.mp4')
    # Get the total number of frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    start_frame = 0
    end_frame = total_frames

    frame_counter = start_frame
    while video.isOpened():
        success, frame = video.read()
        if frame_counter > end_frame:
            break
        if frame_counter % 30 == 0:
            pic_num += 1
            cv2.imwrite(f's{i}/frame{frame_counter}.jpg', frame)
            print(f"frame {frame_counter}, picture index {pic_num} written!")
            
        frame_counter += 1
        
    print(f"[*] Process finished, totally {i} file was created")

    video.release()
