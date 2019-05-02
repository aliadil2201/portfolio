from django.db import models


class Personal(models.Model):
    myself = models.CharField(max_length=250)
    Name = models.CharField(max_length=250)
    detail = models.CharField(max_length=500)
    discover = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.Name


class About(models.Model):
    image = models.ImageField(upload_to='images/')
    tell_about = models.CharField(max_length=250)
    detail_heading = models.CharField(max_length=250)
    personal_detail = models.CharField(max_length=1000)
    view = models.CharField(max_length=250)
    description = models.CharField(max_length=4000)


class ToolExpertness(models.Model):
    tool_expert_percentage = models.CharField(max_length=250)
    width = models.CharField(max_length=200)


class Qualification(models.Model):
    degree_name = models.CharField(max_length=250)
    session = models.CharField(max_length=250)
    result = models.CharField(max_length=250)

    def __str__(self):
        return self.degree_name


class Designation(models.Model):
    image = models.ImageField(upload_to='images/')
    post = models.CharField(max_length=250)
    date = models.CharField(max_length=250)

    def __str__(self):
        return self.post


class LatestProjectFeatures(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    previous_img = models.ImageField(upload_to='images/')
    category = models.TextField()

    def __str__(self):
        return self.title


class MyOfferedServices(models.Model):
    service_tag = models.CharField(max_length=250)
    Name = models.CharField(max_length=250)
    Description = models.TextField()

    def __str__(self):
        return self.Name


class ServicesComplete(models.Model):
    number_of_services = models.IntegerField()
    services_title = models.CharField(max_length=250)

    def __str__(self):
        return self.services_title


# class Heading(models.Model):
#     service_heading = models.CharField(max_length=500)
#     service_detail = models.CharField(max_length=500)
#     feature_heading = models.CharField(max_length=500)
#     feature_detail = models.CharField(max_length=500)
#     clientfeedback_heading = models.CharField(max_length=500)
#     clientfeedback_detail = models.CharField(max_length=500)
#     plan_heading = models.CharField(max_length=500)
#     plan_detail = models.CharField(max_length=500)
#     blog_heading = models.CharField(max_length=500)
#     blog_detail = models.CharField(max_length=500)
#     qualification_heading = models.CharField(max_length=250)
#     qualification_detail = models.CharField(max_length=250)
#     asked_question_heading = models.CharField(max_length=250)
#     asked_question_detail = models.CharField(max_length=500)
#     popular_post_heading = models.CharField(max_length=250)
#     post_category_heading = models.CharField(max_length=250)
#     blog_comment_heading = models.CharField(max_length=250)
#     blog_single_tag_heading = models.CharField(max_length=250)
#     page_sample_heading = models.CharField(max_length=250)


class Blog(models.Model):
    latest_Image = models.ImageField(upload_to='images/')
    user_image = models.ImageField(upload_to='images/')
    user_name = models.CharField(max_length=250)
    date = models.CharField(max_length=40)
    heart_tag = models.CharField(max_length=250)
    bubble_tag = models.CharField(max_length=250)
    image_title = models.CharField(max_length=250)
    image_description = models.CharField(max_length=1000)

    def __str__(self):
        return self.user_name


class ClientFeedbackAboutMe(models.Model):
    Image = models.ImageField(upload_to='images/')
    feedback = models.CharField(max_length=500)
    client_name = models.CharField(max_length=250)
    client_post = models.CharField(max_length=250)

    def __str__(self):
        return self.client_name


class ChosePlan(models.Model):
    package_number = models.IntegerField()
    package_name = models.CharField(max_length=250)
    package_title = models.CharField(max_length=250)
    packages = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    buy = models.CharField(max_length=250)

    def __str__(self):
        return self.package_name


class ImageLabel(models.Model):
    label = models.ImageField(upload_to='images/')


class QuestionAnswer(models.Model):
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=1000)

    def __str__(self):
        return self.question


class BlogHomeBanner(models.Model):
    bg_image = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    view_button = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class BlogHomeCategoryWidget(models.Model):
    category_image = models.ImageField(upload_to='images/')
    category_title = models.CharField(max_length=250)
    category_description = models.CharField(max_length=500)

    def __str__(self):
        return self.category_title


class BlogHomeContent(models.Model):
    tag = models.CharField(max_length=1000)
    Name = models.CharField(max_length=250)
    date = models.CharField(max_length=250)
    views = models.CharField(max_length=250)
    comments = models.CharField(max_length=250)
    blog_image = models.ImageField(upload_to='images/')
    blog_title = models.CharField(max_length=250)
    blog_description = models.CharField(max_length=10000)
    blog_view_button = models.CharField(max_length=500)
    quotes = models.CharField(max_length=10000)
    sample_image = models.ImageField(upload_to='images/')
    sample_image2 = models.ImageField(upload_to='images/')

    # def summary(self):
    #     return self.blog_description[:200]

    def __str__(self):
        return self.blog_title


class BlogHomeSearchPost(models.Model):
    placeholder = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=250)
    post = models.CharField(max_length=250)
    description = models.CharField(max_length=10000)

    def __str__(self):
        return self.name


class BlogHomePopularPost(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=250)
    post_time = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class BlogHomeCategory(models.Model):
    category_name = models.CharField(max_length=250)
    number_of_product = models.IntegerField()

    def __str__(self):
        return self.category_name


class BlogHomeNewsLetter(models.Model):
    heading = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    email = models.CharField(max_length=250)
    subcribe = models.CharField(max_length=250)
    subcribe_description = models.CharField(max_length=250)


class BlogSinglePost(models.Model):
    image = models.ImageField(upload_to='images/')
    direction = models.CharField(max_length=250)
    post = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.description


class BlogSingleComment(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=250)
    date = models.CharField(max_length=250)
    comment = models.CharField(max_length=250)
    reply = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class BlogSingleLeaveComment(models.Model):
    comment_heading = models.CharField(max_length=250)
    enter_name = models.CharField(max_length=250)
    enter_mail = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    messege = models.CharField(max_length=1000)
    post_comment = models.CharField(max_length=250)

    def __str__(self):
        return self.enter_name


class BlogSingleTagsCloud(models.Model):
    technology = models.CharField(max_length=250)
    fashion = models.CharField(max_length=250)
    Architecture = models.CharField(max_length=250)
    Food = models.CharField(max_length=250)
    Lifestyle = models.CharField(max_length=250)
    Art = models.CharField(max_length=250)
    Adventure = models.CharField(max_length=250)


class NewsSubscription(models.Model):
    news_email = models.EmailField(max_length=120)

    def __str__(self):
        return self.news_email


class ContentFormAddressInfo(models.Model):
    state_address = models.CharField(max_length=250)
    simple_address = models.CharField(max_length=250)
    mobile_number = models.CharField(max_length=250)
    time = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.state_address


class ContactForm(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
