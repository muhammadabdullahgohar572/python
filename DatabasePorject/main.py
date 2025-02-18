import sqlite3

conn = sqlite3.connect("youTube_Videos.db")
cursor = conn.cursor()
cursor.execute(
    """ 
               CREATE TABLE IF NOT EXISTS videos(
                   id INTEGER PRIMARY KEY ,
                   name TEXT NOT NULL,
                   time TEXT NOT NULL
               )
               """
)


def List_video():
    coursor = cursor.execute("SELECT * FROM videos")
    for row in coursor.fetchall():
        print(row)


def Add_video(name, time):
    cursor.execute("INSERT INTO videos  (name,time) VALUES( ?,?)", (name, time,))
    conn.commit()


def Update_video(video_id, new_name, new_time):
    cursor.execute(
        "UPDATE videos SET name=? , time=? WHERE id = ?", (video_id,new_name, new_time)
    )
    conn.commit()


def Delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()


def main():
    while True:
        print("Welcome to the YouTube Video Database")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Delete a video")
        print("4. Update a video")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            List_video()
        elif choice == 2:
            name = input("Enter the name of the video: ")
            time = input("Enter the time of the video: ")
            Add_video(name, time)
        elif choice == 3:
            id = int(input("Enter the id of the video: "))
            Delete_video(id)
        elif choice == 4:
            id = int(input("Enter the id of the video: "))
            name = input("Enter the name of the video: ")
            time = input("Enter the time of the video: ")
            Update_video(id, name, time)

        elif choice == 5:
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()

conn.close()