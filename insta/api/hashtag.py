from insta.api.base import BaseAPI


class HashTag(BaseAPI):
    def __init__(self, hashtag):
        super(HashTag, self).__init__("GET")
        uri = "tags/search"
        json = self.request(uri, {"q": hashtag})
        self.data = json

class TagInfo(BaseAPI):
    def __init__(self, hashtag):
        super(TagInfo, self).__init__("GET")
        uri = "tags/%s" % hashtag
        json = self.request(uri, {})
        self.data = json


class RecentTagPosts(BaseAPI):
    def __init__(self, hashtag):
        super(RecentTagPosts, self).__init__("GET")
        uri = "tags/%s/media/recent" % hashtag
        json = self.request(uri, {})
        self.data = json