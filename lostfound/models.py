from django.db import models


class LostItem(models.Model):
    itemname = models.CharField(max_length=100, verbose_name = "Item Name", null=True, blank=True)

    itemimage = models.ImageField(upload_to='media/', verbose_name = "ITEM IMAGE", blank=True, null=True)
    itemdescription = models.CharField(max_length=2000,verbose_name = "Item Description", null=True, blank=True)
    iteamlostlocation = models.CharField(max_length=200, verbose_name = "Location Lost",null=True, blank=True,)
    owneremail = models.EmailField(max_length=200,verbose_name = "Owner's Email", null=False)
    timecreated = models.DateTimeField(auto_now=True, verbose_name = "Time Created",)
    date = models.DateField(auto_now_add=True,verbose_name = "Date", blank=True, null=True)

    

    def __str__(self):
        return self.itemname

    class Meta:
        ordering = ('-timecreated',)











class FoundItem(models.Model):
    itemname = models.CharField(max_length=100, verbose_name = "Item Name", )
    itemimage = models.ImageField(upload_to='media',verbose_name = "ITEM IMAGE", null=True, blank=True)
    itemdescription = models.CharField(max_length=2000,verbose_name = "Item Description", null=True, blank=True)
    iteamfoundlocation = models.CharField(max_length=200, verbose_name = "Location Found",null=True, blank=True,)
    founderemail = models.EmailField(max_length=200,verbose_name = "Founder's Email", null=False)
    timecreated = models.DateTimeField(auto_now=True, verbose_name = "Time Created",)
    date = models.DateField(auto_now_add=True,verbose_name = "Date", blank=True, null=True)


    def __str__(self):
        return self.itemname

    @property
    def image_url(self):
        if self.itemimage and hasattr(self.itemimage, 'url'):
            return self.itemimage.url

    class Meta:
        ordering = ('-timecreated',)
