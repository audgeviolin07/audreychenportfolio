import unittest
from peewee import *
from flask import json
from app import app, TimelinePost

MODELS = [TimelinePost]

# use in-memory SQLite for tests
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Blind model classes to test db. Have complete list of all models,
        # so no need to recursively bind dependencies
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Not strictly necessary b/c SQLite in-memory db only live for duration
        # of connection, but good practice
        test_db.drop_tables(MODELS)

        test_db.close()

    def test_timeline_post(self):
        # Test Post 1
        first_post = TimelinePost.create(name="Sam Lee", email="sl@gmail.com", content="Hello!")
        assert first_post.id == 1

        # Test Post 2
        second_post = TimelinePost.create(name="Kanmani M", email="km@gmail.com", content="Hello Number 2!")
        assert second_post.id == 2

        client = app.test_client()
        response = client.get('/api/timeline_post')
        data = json.loads(response.data)

        # Check that 'timeline_posts' key exists
        self.assertIn('timeline_posts', data)

        # Check we have 2 posts
        self.assertEqual(len(data['timeline_posts']), 2)

        # Check contents of post
        self.assertEqual(data['timeline_posts'][0]['id'], second_post.id)
        self.assertEqual(data['timeline_posts'][0]['name'], "Kanmani M")
        self.assertEqual(data['timeline_posts'][0]['email'], "km@gmail.com")
        self.assertEqual(data['timeline_posts'][0]['content'], "Hello Number 2!")

        self.assertEqual(data['timeline_posts'][1]['id'], first_post.id)
        self.assertEqual(data['timeline_posts'][1]['name'], "Sam Lee")
        self.assertEqual(data['timeline_posts'][1]['email'], "sl@gmail.com")
        self.assertEqual(data['timeline_posts'][1]['content'], "Hello!")


