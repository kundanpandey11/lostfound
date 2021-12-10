from django.forms import ModelForm
from .models import LostItem, FoundItem
import datetime


class lostform(ModelForm):
    class Meta:
        model = LostItem
        fields = ('itemname',  'owneremail', 'itemdescription', 'iteamlostlocation', 'itemimage', )

        # def save(self, *args, **kwargs):
        #     super().save(self, *args, **kwargs)
        #     self.fields['date'] = 



class foundform(ModelForm):
    class Meta:
        model = FoundItem
        fields = ('itemname',  'founderemail', 'itemdescription', 'iteamfoundlocation', 'itemimage', )