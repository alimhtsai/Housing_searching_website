from django.shortcuts import redirect, render
from .models import Buydb, Rentdb, WhichMrtName
from .filters import BuydbFilter, RentdbFilter
from django.views import generic

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects

    num_buydb=Buydb.objects.all().count()
    num_rentdb=Rentdb.objects.all().count()
    num_whichmrtname = WhichMrtName.objects.all().count()
    # num_whichmrtname=WhichMrtName.objects.all().count()
    # Available books (status = 'a')
    #num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    #num_authors=Author.objects.count()  # The 'all()' is implied by default.
    #num_book_title_icontain_how = Book.objects.filter(title__icontains = 'how').count()
    
    #Render the HTML template index.html with the data in the context variable
    #而rendor可以將我們要傳達的資料一併打包，再透過 HttpResponse 回傳到瀏覽器
    return render(
        request,
        #index()最後將會導向到下列這個.html檔案:index.html
        'index.html',
        #並且把剛剛從db取得的物件傳送到index.html
        # context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
        context={'Buydb Number': num_buydb, 'Rentdb Number': num_rentdb, 'Whichmrtname Number': num_whichmrtname}
    )












class BuydbListView(generic.ListView):
    model = Buydb
    #透過定義get_queryset()就可以自己定義想要的資料
    #沒有要自定義的話就註解掉get_queryset()
    def get_queryset(self):
        return Buydb.objects.filter(MrtName__icontains='捷運站') #取前20筆資料，buydbMrt包含關鍵字'捷運站'的
    
    #等等要去哪個路徑找.html檔案
    #不定義這個template_name的話，Django就會去預設的路徑尋找.html
    #預設的路徑是：/locallibrary/catalog/templates/catalog/book_list.html
    #不過目前暫時程式碼設定路徑的方式跟預設一樣就好    
    template_name = '/rentorbuyv2/catalog/templates/catalog/buydb_list.html'

    #get_context_data()是用來建立自訂的Server side variable的
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BuydbListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

    #這是分頁機制, 以下設定一頁的最多資料筆數 = 40
    paginate_by = 40





class BuydbDetailView(generic.DetailView):
    model = Buydb





def BuydbFloortypeFilter(request):
    buydb = Buydb.objects.all()
    buydbFilter = BuydbFilter(queryset = buydb)
    # 當第一次載入網頁時，由於請求方法為GET，
    # 所以在利用queryset關鍵字參數(Keyword Argument)來指定django-filter物件所要查詢資料集，
    # 需指定資料模型中的所有資料。
    

    if request.method == "POST":
        buydbFilter = BuydbFilter(request.POST, queryset = buydb)
    # 而當請求方法為POST，也就是使用者輸入查詢條件，按下查詢按鈕時，
    # django-filter物件將依據請求所傳入的查詢條件(request.POST)，來自動篩選資料集。


    return render(request, 'buydbfilter.html', context = {'BuydbFilter': buydbFilter})




def BuydbMetrocodeFilter(request):
    buydb = Buydb.objects.all()
    buydbFilter = BuydbFilter(queryset = buydb)
    # 當第一次載入網頁時，由於請求方法為GET，
    # 所以在利用queryset關鍵字參數(Keyword Argument)來指定django-filter物件所要查詢資料集，
    # 需指定資料模型中的所有資料。

    if request.method == "POST":
        buydbFilter = BuydbFilter(request.POST, queryset = buydb)
    # 而當請求方法為POST，也就是使用者輸入查詢條件，按下查詢按鈕時，
    # django-filter物件將依據請求所傳入的查詢條件(request.POST)，來自動篩選資料集。

    return render(request, 'buydbfilterMrtCode.html', context = {'BuydbFilter': buydbFilter})
    



def BuydbMetromapFilter(request):
    model = Buydb
    template_name = '/rentorbuyv2/catalog/templates/buydb_metromap.html'
    return render(request, 'buydb_metromap.html')














class RentdbListView(generic.ListView):
    model = Rentdb
    #透過定義get_queryset()就可以自己定義想要的資料
    #沒有要自定義的話就註解掉get_queryset()
    def get_queryset(self):
        return Rentdb.objects.filter(MrtName__icontains='捷運站') #取前20筆資料，buydbMrt包含關鍵字'捷運站'的
    
    #等等要去哪個路徑找.html檔案
    #不定義這個template_name的話，Django就會去預設的路徑尋找.html
    #預設的路徑是：/locallibrary/catalog/templates/catalog/book_list.html
    #不過目前暫時程式碼設定路徑的方式跟預設一樣就好    
    template_name = '/locallibrary/catalog/templates/catalog/rentdb_list.html'

    #get_context_data()是用來建立自訂的Server side variable的
    #跟.Net MVC也挺像的
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(RentdbListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

    #這是分頁機制, 以下設定一頁的最多資料筆數 = 40
    paginate_by = 40





class RentdbDetailView(generic.DetailView):
    model = Rentdb





def RentdbFloortypeFilter(request):
    rentdb = Rentdb.objects.all()
    rentdbFilter = RentdbFilter(queryset = rentdb)
    # 當第一次載入網頁時，由於請求方法為GET，
    # 所以在利用queryset關鍵字參數(Keyword Argument)來指定django-filter物件所要查詢資料集，
    # 需指定資料模型中的所有資料。

    if request.method == "POST":
        rentdbFilter = RentdbFilter(request.POST, queryset = rentdb)
    # 而當請求方法為POST，也就是使用者輸入查詢條件，按下查詢按鈕時，
    # django-filter物件將依據請求所傳入的查詢條件(request.POST)，來自動篩選資料集。

    return render(request, 'rentdbfilter.html', context = {'RentdbFilter': rentdbFilter})







def RentdbMetrocodeFilter(request):
    rentdb = Rentdb.objects.all()
    rentdbFilter = RentdbFilter(queryset = rentdb)
    # 當第一次載入網頁時，由於請求方法為GET，
    # 所以在利用queryset關鍵字參數(Keyword Argument)來指定django-filter物件所要查詢資料集，
    # 需指定資料模型中的所有資料。

    if request.method == "POST":
        rentdbFilter = RentdbFilter(request.POST, queryset = rentdb)
    # 而當請求方法為POST，也就是使用者輸入查詢條件，按下查詢按鈕時，
    # django-filter物件將依據請求所傳入的查詢條件(request.POST)，來自動篩選資料集。

    return render(request, 'rentdbfilterMrtCode.html', context = {'RentdbFilter': rentdbFilter})
    



def RentdbMetromapFilter(request):
    model = Rentdb
    template_name = '/rentorbuyv2/catalog/templates/rentdb_metromap.html'
    return render(request, 'rentdb_metromap.html')












class BuydbMrtCodeR12(generic.ListView):
    model = Buydb
    #透過定義get_queryset()就可以自己定義想要的資料
    #沒有要自定義的話就註解掉get_queryset()
    def get_queryset(self):
        return Buydb.objects.filter(MrtCode__icontains='R12') #MrtCode包含關鍵字'R12'的

    template_name = '/rentorbuyv2/catalog/templates/mrtcode/buydb/r12.html'
    #這是分頁機制, 以下設定一頁的最多資料筆數 = 40
    paginate_by = 40





def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects

    num_buydb=Buydb.objects.all().count()
    num_rentdb=Rentdb.objects.all().count()
    # Available books (status = 'a')
    #num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    #num_authors=Author.objects.count()  # The 'all()' is implied by default.
    #num_book_title_icontain_how = Book.objects.filter(title__icontains = 'how').count()
    
    #Render the HTML template index.html with the data in the context variable
    return render(
        request,
        #index()最後將會導向到下列這個.html檔案:index.html
        'index.html',
        #並且把剛剛從db取得的物件傳送到index.html
        # context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
        context={'num_buydb': num_buydb, 'num_rentdb': num_rentdb}
    )






class RentdbMrtCodeR12(generic.ListView):
    model = Rentdb
    #透過定義get_queryset()就可以自己定義想要的資料
    #沒有要自定義的話就註解掉get_queryset()
    def get_queryset(self):
        return Rentdb.objects.filter(MrtCode__icontains='R12') #MrtCode包含關鍵字'R12'的
    
    template_name = '/rentorbuyv2/catalog/templates/mrtcode/buydb/r12.html'
    #這是分頁機制, 以下設定一頁的最多資料筆數 = 40
    paginate_by = 40













# from django.contrib.auth.decorators import permission_required

# from django.shortcuts import get_object_or_404
# from django.http import HttpResponseRedirect
# from django.urls import reverse

# from .forms import RenewBuydbForm

# #加上適當的權限，限制此功能只有圖書館員可使用
# def renew_buydb(request):
# 	# 透過forms.py去驗證使用者提交的欄位value是否合法
#     # Create a form instance and populate it with data from the request (binding):
#     form = RenewBuydbForm(request.POST)

#     context = {
#         'form' : form
#     }

#     return render(request, 'renew_buydb.html', context)







from django.shortcuts import get_object_or_404
from .forms import BuydbForm 

def buydb_create_view(request):

    # buydb_inst=get_object_or_404(Buydb)

    form = BuydbForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = BuydbForm() # 清空 form

    context = {
        'form' : form
    }

    return render(request, "buydb_create.html", context)



# def buydb_create_view(request):
#     if request.method == 'POST': # If the form has been submitted...
#         form = BuydbForm(request.POST) # A form bound to the POST data

#         if form.is_valid():
#             form.save()    # saves a new 'Lala' object to the DB
        
#         context = {
#             'form' : form
#         }

#         return render(request, "buydb_create.html", context)