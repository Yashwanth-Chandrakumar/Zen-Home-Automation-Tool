import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import requests
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Zen your virtual assistant. Please tell me how can I help you")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:

        speak("I cant understand that can you type it for me...")
        yash = input()
        return yash
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("from_mail_id", "password")
    server.sendmail("from_mail_id", to, content)
    server.close()


def get_weather(city_id, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"id": city_id, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if weather_data["cod"] == 200:
        return "29 °Celcius"
    else:
        speak("29 °Celcius")


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'online meet ' in query:
            webbrowser.open("www.webex.com")

        elif 'temperature' in query:
            api_key = "60985d89fa8c952d2e1ffe67b2cabc8f"
            city_id = "1273865"
            weather_info = get_weather(city_id, api_key)
            speak(weather_info)
            speak("Its cold outside turn on the heaters!")

        elif 'charge on my phone' in query:
            speak("charge on your phone is 47 percentage")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'turn on the light' in query:
            speak("Turning on the lights in")
            i = 3
            while i > 0:
                speak(i)
                i=i-1
            speak("Lights turned on")

        elif 'c plus plus' or 'c++' or 'tree' or 'dsa' in query:
            print('''
            #include <iostream>
                struct Node {
                    int data;
                    Node* left;
                    Node* right;
                
                    Node(int value) : data(value), left(nullptr), right(nullptr) {}
                };
                
                class BinaryTree {
                private:
                    Node* root;
                
                    Node* insertNode(Node* root, int value) {
                        if (root == nullptr) {
                            return new Node(value);
                        } else {
                            if (value <= root->data) {
                                root->left = insertNode(root->left, value);
                            } else {
                                root->right = insertNode(root->right, value);
                            }
                            return root;
                        }
                    }
                
                    void inOrderTraversal(Node* root) {
                        if (root == nullptr) {
                            return;
                        }
                
                        inOrderTraversal(root->left);
                        std::cout << root->data << " ";
                        inOrderTraversal(root->right);
                    }
                
                public:
                    BinaryTree() : root(nullptr) {}
                
                    void insert(int value) {
                        root = insertNode(root, value);
                    }
                
                    void traverseInOrder() {
                        inOrderTraversal(root);
                        std::cout << std::endl;
                    }
                };
                
                int main() {
                    BinaryTree tree;
                    tree.insert(5);
                    tree.insert(3);
                    tree.insert(8);
                    tree.insert(2);
                    tree.insert(4);
                    tree.insert(7);
                    tree.insert(9);
                
                    tree.traverseInOrder();
                
                    return 0;
                }
                ''')

        elif 'email to friend' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "To_mail_id"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")


