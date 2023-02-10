#定義model的class類別之前都需要先import models
#每個class類別都代表一個資料表
from django.db import models



#當你的資料表定義包含自定義的function的時候，就必須import reverse
from django.urls import reverse
from import_export.resources import ModelDeclarativeMetaclass 
#Used to generate URLs by reversing the URL patterns






class Buydb(models.Model):
    """
    Model representing buydbR12.xlsx
    """
    #欄位名稱:name
    #CharField:大概是varchar, nvarchar之類的
    #max_length:此欄位最大長度
    #help_text:此欄位的註解，實務上在公司還真的很少人寫註解在資料表
    Title = models.CharField(max_length=200, help_text="Enter buydb title(id)")
    MrtCode = models.CharField(max_length=200, help_text="Enter Mrt Station Code, ex: R12 = 雙連捷運站")
    #BuydbMrtName = models.ForeignKey(WhichMrtName, on_delete=models.SET_NULL, null=True) 
    MrtName = models.CharField(max_length=200, help_text="Enter Mrt Station Name, ex: R12 = 雙連捷運站")
    Address = models.CharField(max_length=200, help_text="Enter Address")

    # FloorType_Choices = (
    #     ('flat', '整層住家'),('room', '套房')
    # )
    FloorType = models.CharField(max_length=200, help_text="Enter 整層住家 or 套房")

    RoomNum = models.IntegerField(help_text="Enter Room Number, ex: 4 = 4房")
    Price = models.IntegerField(help_text="Enter buying prices per month, 單位 = 新台幣")
    Size = models.DecimalField(max_digits=20,decimal_places=2, help_text="Enter housing size, 單位 = 坪")
    Floor = models.CharField(max_length=200, help_text="Enter floor")
    Parking = models.CharField(max_length=200, help_text="Enter parking detail")
    Link = models.CharField(max_length=500, help_text="Enter 591 urls")
 


    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.Title
    

    # get_absolute_url:這是自定義的函數，當你使用get_absolute_url的時候
    # 會透過book-detail這個url mapping的這個網址mapping規則去導向網頁
    # 當然最後會導向的網頁會顯示這個Book物件的詳細細節
    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('buydb-detail', args=[str(self.id)])   









class WhichMrtName(models.Model):
    Title = models.ForeignKey(Buydb, on_delete=models.SET_NULL, null=True) 
    MrtCode = models.CharField(max_length=200, help_text="Enter Mrt Station Code, ex: R12 = 雙連捷運站")
    MrtName = models.CharField(max_length=200, help_text="Enter Mrt Station Name, ex: R12 = 雙連捷運站")
    
    #FordingKey表示多個Buydb對應到一個WhichMrtName

    def __str__(self):
        """String for representing the Model object."""
        return self.MrtName











class Rentdb(models.Model):
    """
    Model representing RentdbR12.xlsx
    """
    #欄位名稱:name
    #CharField:大概是varchar, nvarchar之類的
    #max_length:此欄位最大長度
    #help_text:此欄位的註解，實務上在公司還真的很少人寫註解在資料表
    Title = models.CharField(max_length=200, help_text="Enter buydb title(id)")
    MrtCode = models.CharField(max_length=200, help_text="Enter Mrt Station Code, ex: R12 = 雙連捷運站")
    MrtName = models.CharField(max_length=200, help_text="Enter Mrt Station Name, ex: R12 = 雙連捷運站")
    Address = models.CharField(max_length=200, help_text="Enter Address")

    # FloorType_Choices = (
    #     ('flat', '整層住家'),('room', '套房')
    # )
    FloorType = models.CharField(max_length=200, help_text="Enter 整層住家 or 套房")
    
    RoomNum = models.IntegerField(help_text="Enter Room Number, ex: 4 = 4房")
    Price = models.IntegerField(help_text="Enter buying prices per month, 單位 = 新台幣")
    Size = models.DecimalField(max_digits=20,decimal_places=2, help_text="Enter housing size, 單位 = 坪")
    Floor = models.CharField(max_length=200, help_text="Enter floor")
    Parking = models.CharField(max_length=200, help_text="Enter parking detail")
    Link = models.CharField(max_length=500, help_text="Enter 591 urls")
 


    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.Title
    

    # get_absolute_url:這是自定義的函數，當你使用get_absolute_url的時候
    # 會透過book-detail這個url mapping的這個網址mapping規則去導向網頁
    # 當然最後會導向的網頁會顯示這個Book物件的詳細細節
    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('rentdb-detail', args=[str(self.id)])   

