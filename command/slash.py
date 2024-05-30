import json
import urlextract


text = "https://id.io.net/auth/v1/token?grant_type=refresh_token"

detect_link = urlextract.URLExtract()
def detect(text):
    part = text.split(" ")
    with open("filter/filetWords.json", "r") as f:
        data = json.load(f)
        for word in data["words"]:
            if word in part:
                return "detected"

    





if __name__ == "__main__":
    print(detect("сука"))