from pytube import YouTube
while True:
    url = input("Please enter the url of the video : ")

    my_video = YouTube(url)



    print("*******************video title******************")

    print(my_video.title)

    print("****************Thumbnail Image*****************")

    print(my_video.thumbnail_url)


    print("***************Download video*******************")

    my_video = my_video.streams.get_highest_resolution()


    my_video.download()


    print("hello world")
