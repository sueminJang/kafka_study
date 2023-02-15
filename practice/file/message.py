class Message:
    def __init__(self):
        self.latest_version = None

    def get(self):
        past_version = open("practice/file/past_ver.txt", "r").readlines()
        self.latest_version = open("practice/file/message.txt", "r").readlines()
        diff_ = len(self.latest_version) - len(past_version)
        if diff_:
            return "\n".join(self.latest_version[len(self.latest_version) - diff_:])

    def save_past_version(self):
        with open(
                "practice/file/past_ver.txt", "w") as output:
            output.write("".join(self.latest_version))
            output.close()
