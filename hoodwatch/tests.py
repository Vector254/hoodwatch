from django.test import TestCase
from .models import *

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(id=1, username='test', password='test123')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()


class HoodTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='test')
        self.hood = NeighbourHood.objects.create(id=1, name='test',location='Nairobi', description='This is a test hood',
                        admin=self.user )

    def test_instance(self):
        self.assertTrue(isinstance(self.hood, NeighbourHood))

    def test_save_hood(self):
        self.hood.save_hood()
        hood = NeighbourHood.objects.all()
        self.assertTrue(len(hood) > 0)

    def test_get_hoods(self):
        self.hood.save()
        hoods = NeighbourHood.objects.all()
        self.assertTrue(len(hoods) > 0)

    def test_delete_hood(self):
        self.hood.delete_hood()
        hood = NeighbourHood.search_hood('test')
        self.assertTrue(len(hood) < 1)


class BusinessTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='test')
        self.hood = NeighbourHood.objects.create(id=1, name='test',location='Nairobi', description='This is a test hood',
                        admin=self.user )
        self.profile = Profile.objects.create(user=self.user,name='test', email='test@gmail.com',bio='my bio', profile_picture='media/default.png', 
                        location='Test_location', hood=self.hood )
        self.biz = Business.objects.create(id=1, name='test', email='test@gmail.com', description='This is a test post',
                                        user=self.user, hood=self.hood)

    def test_instance(self):
        self.assertTrue(isinstance(self.biz, Business))

    def test_save_biz(self):
        self.biz.save_biz()
        biz = Business.objects.all()
        self.assertTrue(len(biz) > 0)

    def test_get_bizs(self):
        self.biz.save()
        bizs = Business.objects.all()
        self.assertTrue(len(bizs) > 0)

    def test_search_biz(self):
        self.biz.save()
        biz = Business.search_biz('test')
        self.assertTrue(len(biz) > 0)

    

class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='test')
        self.hood = NeighbourHood.objects.create(id=1, name='test',location='Nairobi', description='This is a test hood',
                        admin=self.user )
        self.profile = Profile.objects.create(user=self.user,name='test', email='test@gmail.com',bio='my bio', profile_picture='media/default.png', location='Test_location', hood=self.hood )
        self.post = Posts.objects.create(id=1, title='test post', post='This is a test post',hood=self.hood,
                                        author=self.profile)

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Posts))

    def test_save_post(self):
        self.post.save_post()
        post = Posts.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts = Posts.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Posts.search_post('test')
        self.assertTrue(len(post) < 1)




    
