import json
 
def load_data():
    try:
        with open("youtube.txt","r") as file:
            return json.load(file) 
    except FileNotFoundError : 
        return []
    
def save_data_helper(videos):
    with open ("youtube.txt",'w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print("\n ")
    print("*"*99)
    for index,video in enumerate(videos,start=1):
        print(f"{index},{video['name']},Duration:{video['duration']}")
    print("*"*99)

def add_video(videos):
    name=input("Enter name of video -> ")
    time=input("Enter duration of the video (in minutes) -> ")
    videos.append({"name":name, "duration":int(time)})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    id=int(input("Which Video you want to Update?->"))
    if (1 <= id <= len(videos)):
        name = input('Enter new Name -> ')
        time = input('Enter New Duration -> ')
        videos[id-1]['name'] = name
        videos[id-1]['duration'] = int(time)
        save_data_helper(videos)
    else:
        print("Invalid index.")

def delete_video(videos):
    list_all_videos(videos)
    id=int(input("Delete which video?->"))
    if (1<=id<=len(videos)):    
        videos.pop(id - 1 )
        save_data_helper(videos)
    else:
        print("Invalid index")    

# Driver code  

def main():
    videos=load_data()
    while True:
        print("\nYt Manager")
        print("1.List all the videos.")
        print("2.Add a video.")
        print("3.Update")
        print("4.Delete")
        print("4.Exit")
        choice=int(input("Enter your choice please --> "))
        match choice:
            case 1:
                list_all_videos(videos)
            case 2:
                add_video(videos)
            case 3:
                update_video(videos)
            case 4:
                delete_video(videos)
            case 4:
                break
            case _:
                print("Invalid Choice.\n")

if __name__=="__main__":
    main()