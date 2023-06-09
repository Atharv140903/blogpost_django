from django.utils.text import slugify
import string
import random
 
def generate_random_str(N):
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))
    return res



def generate_slug(text):
    from home.models import blogPostModel
    new_slug = slugify(text)
    if blogPostModel.objects.filter(slug = new_slug).exists():
        return generate_slug(text + generate_random_str(5))
    return new_slug