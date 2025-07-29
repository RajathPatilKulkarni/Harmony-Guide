from chatbot.chatbot import recommend_song, load_model, load_data

if __name__ == "__main__":
    df = load_data()
    model = load_model()

    print("Welcome to the Music Recommendation Chatbot!")
    while True:
        user_input = input("Enter an artist name (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        print(f"Recommended Song: {recommend_song(user_input, model, df)}")
