from django.db import models

# Create your models here.

#           A model is the single, definitive source of information 
#       about your data. They contain the essential fields and 
#       behaviors of the data you’re storing. In general, each model maps 
#       to a single database table.

class Profile(models.Model):
    '''
    Data definition for the Profile model.
    
    models
        :username: = models.TextField(max_length=20, unique=True)
        :name: = models.TextField(blank=True)
        :pfp_file: = models.FileField(blank=True, null=True)
        :bio: = models.TextField(blank=True)
        :pfp_file: = models.ImageField(blank=True, null=True, default="defaultpfp.jpg")
        :created: = models.DateTimeField(auto_now_add=True, blank=True)


    '''
    # user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    username = models.TextField(max_length=20, unique=True)
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    pfp_file = models.ImageField(blank=True, null=True)
    bio = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.username}'


class Post(models.Model):
    '''
    Data definition for the Post model.

    models
        :profile: = models.ForeignKey(Profile, on_delete=models.CASCADE)
        :caption: = models.TextField(max_length=100, blank=True)
        :created: = models.DateTimeField(auto_now_add=True, blank=True)

    '''

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    caption = models.TextField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    # The max date a post can apear on the public feed, 14 days
    # after a post's first cosign
    max_feed_date = models.DateField(blank=True) 


class Image(models.Model):
    '''Data definition for the Image model.

    models
        :post: = models.ForeignKey(Post, on_delete=models.CASCADE)
        :image: = models.FileField(blank=True, null=True)
        :created: = models.DateTimeField(auto_now_add=True, blank=True)


    '''

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.FileField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)


class CoSign(models.Model):
    '''
    Data definition for the CoSign model. 

    models
        :post: = models.ForeignKey(Post, on_delete=models.CASCADE)
        :profile: = models.ForeignKey(Profile, on_delete=models.CASCADE)
        :created: = models.DateTimeField(auto_now_add=True, blank=True)

    functions
        :def can_go_to_feed(self): returns True if post can go to public feed
    '''

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def can_go_to_feed(self):
        '''
        Docstring for can_go_to_feed
        
        :param self: The CoSign Object calling the function

        :return True: If the date is before the maximum date the
            post is allowed to be on the public feed 
        '''

        if self.date > self.post.max_feed_date:
            return False
        else:
            return True



class Like(models.Model):
    '''
    Data definition for the Like model. 

    post = models.ForeignKey(Post, on_delete=models.CASCADE) \n
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE) \n
    
    created = models.DateTimeField(auto_now_add=True, blank=True)
    
    '''

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, blank=True)



class Comment(models.Model):
    '''
    Data definition for the Comment model. 

    post = models.ForeignKey(Post, on_delete=models.CASCADE) \n
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE) \n
    comment = models.TextField(max_length=100) \n
    
    created = models.DateTimeField(auto_now_add=True, blank=True)
    
    '''

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment = models.TextField(max_length=100)

    created = models.DateTimeField(auto_now_add=True, blank=True)