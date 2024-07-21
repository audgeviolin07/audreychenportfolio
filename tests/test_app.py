import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert "<title>MLH Fellow: Audrey Chen</title>" in html

        # Test meta tags
        assert '<meta property="og:title" content="Personal Portfolio">' in html
        assert '<meta property="og:description" content="My Personal Portfolio">' in html

        # Test navigation
        assert '<header class="nav-bar">' in html
        assert '<img src="./static/img/logo.svg" />' in html

        # Test nav buttons
        assert '<a href="/education" class="btn"><div class="div-3">Education</div></a>' in html
        assert '<a href="/workexperience" class="btn"><div class="div-4">Work Experience</div></a>' in html
        assert '<a href="/hobbies" class="btn"><div class="div-5">Hobbies</div></a>' in html
        assert '<a href="/travelmap" class="btn"><div class="div-5">Travel Map</div></a>' in html

        # Test images exist
        assert '<img src="./static/img/logo.svg" />' in html
        assert '<img src="./static/img/audrey.jpg">' in html
        assert '<img loading="lazy" src="./static/img/abt.png" class="img" />' in html

    def test_timeline(self):
        # Initial Empty Timeline
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        # Adding Two Posts to Timeline
        posts = [
            {"name": "Bob", "email": "bob1@gmail.com", "content": "Bob says hi"},
            {"name": "Joe", "email": "joe1@gmail.com", "content": "Joe says hi"}
        ]

        for post in posts:
            self.client.post("/api/timeline_post", data=post)

        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 2

        assert json["timeline_posts"][0]["content"] == "Joe says hi"
        assert json["timeline_posts"][1]["content"] == "Bob says hi"


    # def test_malformed_timeline_post(self):
    #     # POST request missing name
    #     response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
    #     assert response.status_code == 400
    #     html = response.get_data(as_text = True)
    #     assert "Invalid name" in html
    #
    #     # POST request with empty content
    #     response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
    #     assert response.status_code == 400
    #     html = response.get_data(as_text = True)
    #     assert "Invalid content" in html
    #
    #     # POST request with malformed email
    #     response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
    #     assert response.status_code == 400
    #     html = response.get_data(as_text = True)
    #     assert "Invalid email" in html
