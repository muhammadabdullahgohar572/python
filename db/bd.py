# abdullah1234
from pymongo import MongoClient
from  bson import ObjectId

client = MongoClient(
    "mongodb+srv://abdullah1234:abdullah1234@cluster0.dnr3w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    tlsAllowInvalidCertificates=True
)
bd = client["videos"]
collection = bd["videos"]
print(collection)


def list_Allvideos():

    for getvideo in collection.find():
        print(
            f"This is video is {getvideo['_id']} abd This is a video name {getvideo['name']} and this is a time to complete watch an {getvideo['time']}"
        )


def add_Allvideos(name, time):
    collection.insert_one({"name": name, "time": time})


def Delete_Allvideos(video_id):
    collection.delete_one({"_id":ObjectId(video_id)})


def update_Allvideos(video_id,name,time):
    collection.update_one({"_id": ObjectId(video_id)}, {"$set": {"name": name, "time": time}})


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
            list_Allvideos()
        elif choice == 2:
            name = input("Please Enter a name: ")
            Time = input("Please a Time complete Video: ")
            add_Allvideos(name, Time)
        elif choice == 3:
            video_id = input("Enter a video Id to delete: ")
            Delete_Allvideos(video_id)
        elif choice == 4:
            
            video_id = input("Enter a video Id to update: ")
            name = input("Please Enter a new name: ")
            Time = input("Please a new Time complete Video: ")
            update_Allvideos(video_id, name, Time)
        elif choice == 5:
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
