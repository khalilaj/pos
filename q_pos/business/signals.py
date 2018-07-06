# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from
#
# def create_business(sender, weak=False, **kwargs):
#     if kwargs['created']:
#         user_type = kwargs['instance'].user_type
#         if user_type == 'EMP':
#             employee = Business.objects.create(merchant=kwargs['instance'], name=kwargs['instance'].firstname,
#                                                email=kwargs['instance'].email)
#
#
# post_save.connect(save_profile, sender=User)