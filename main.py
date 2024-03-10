def load_data():
    pass
def list_all_videos(videos):
    pass

def add_video(video):
    pass

def update_video(video):
    pass

def delete_video(video):
    pass

def main():
    videos=load_data()
    while True:
        print("Yt Manager")
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