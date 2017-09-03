from insta.api.base import BaseAPI


class HashTag(BaseAPI):
    def __init__(self, hashtag):
        super(HashTag, self).__init__("GET")
        uri = "tags/search"
        json = self.request(uri, {"q": hashtag})
        print(json)
