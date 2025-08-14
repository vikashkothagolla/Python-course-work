
#Base class - instagram story
class instagram:
    def __init__(self,user):
        self.user=user
        self.story_content = ""
    def post_story(self,content):
        self.story_content=content
        return (f"{self.user} posted a story:{content}")   
    