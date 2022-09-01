# signals:
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete
from django.core.exceptions import PermissionDenied
# models:
from books import models

@receiver(pre_delete, sender = models.Category)
def category_deleter(sender, instance, *args, **kwargs):
    # print(instance)
    if instance == sender.objects.get(name = 'No Category'):
        raise PermissionDenied

# strings
import string
alphabet = list(string.ascii_uppercase)

@receiver(pre_save, sender = models.Category)
def category_pre_setter(sender, instance, *args, **kwargs):
    try:
        if instance.num is None or instance.sign is None:    
            number = 1
            alp_index = 0
            found = False
            while not found:
                if number > 20 or alp_index > len(alphabet)-1 :
                    instance.sign = 'Z'
                    instance.num = '19'
                    found = True
                
                if number == 20 and alphabet[alp_index] == 'Z':
                    instance.sign = 'Z'
                    instance.num = '19'
                    found = True
                
                # _NOTE: Z 20 is belongs to 'NO CATEGORY' and shoudn't be assigned
                
                if len(models.Category.objects.filter(sign = alphabet[alp_index])) == 0:

                    if len(models.Category.objects.filter(sign = alphabet[alp_index], num = number)) == 0:
                        instance.sign = alphabet[alp_index]
                        instance.num = number
                        found = True
                    else:
                        number += 1

                else:
                    alp_index += 1

            
            
            print(instance.sign ,instance.num )
    except:
        pass

@receiver(post_save, sender = models.BookCopy)
def bookCopy_setter(sender, instance, created, *args, **kwargs):

    if created:
        try:
            if not instance.shelf_code :
                instance.shelf_code = f'{instance.book.language[:2]}{instance.book.category.get_signiture()} {instance.book.id}\{instance.id}'
                instance.save()
        except:
            pass

@receiver(post_save, sender = models.Book)
def book_setter(sender, instance, created, *args, **kwargs):

    if created:
        try:
            pass
        except:
            pass