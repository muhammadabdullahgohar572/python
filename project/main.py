import json


def load_data():
    try:
        with open("youtube.txt", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("YouTube data file not found.")
        return []


def save_Data_here(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)


def list_youtube_videos(videos):
         print("\n")
         print("*" * 50)
         for index, video in enumerate(videos, start=1):
           print(f"{index} - {video['name']} - Duration is  {video['time']}")
         print("\n")
         print("*" * 50)


def Add_a_youtube_video(videos):
    name = input("Enter the name of the video: ")
    time = input("Enter the time of the video: ")
    videos.append({"name": name, "time": time})
    save_Data_here(videos)


def Update_a_youtube_video_Details(videos):
    list_youtube_videos(videos)
    index=int(input("Enter The video number you want to update: "))
    if 1<=index <=len(videos):
        name = input("Enter the name of the video: ")
        time = input("Enter the time of the video: ")
        videos[index-1]={"name":name,"time":time}
        save_Data_here(videos)
    else:
        print("Invalid video number")

def Delete_a_youtube_video(videos):
   list_youtube_videos(videos)
   index=int(input("Enter The video number you want to delete: "))
   if 1<=index<=len(videos):
         del videos[index-1]
         save_Data_here(videos)
   else:
    print("Invalid video number")


def main():
    videos = load_data()
    while True:
        print("\n Choose an option:")
        print("1. List all Youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video Details")
        print("4. Delete a youtube video")
        print("5. Exit")
        choice = input("Enter your choice: ")
      

        match choice:
            case "1":
                list_youtube_videos(videos)
            case "2":
                Add_a_youtube_video(videos)
            case "3":
                Update_a_youtube_video_Details(videos)
            case "4":
                Delete_a_youtube_video(videos)
            case "5":
                print("Exiting")
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
