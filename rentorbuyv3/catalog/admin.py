from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Buydb, Rentdb, WhichMrtName
from django.apps import apps
from django.utils.translation import gettext_lazy as _


# Register your models here.



class BuydbResource(resources.ModelResource):

    def get_export_fields(self):
        #fields:
        #用來基本客製化顯示的欄位的順序（編輯資料時）
        #預設的系統排列方式，是垂直的一個一個欄位顯示
        fields = self.get_fields()
        # 默认导入导出field的column_name为字段的名称
        # 这里修改为字段的verbose_name
        for field in fields:
            field_name = self.get_field_name(field)
            if field_name in self.verbose_name_dict.keys():
                field.column_name = self.verbose_name_dict[field_name]
                # 如果设置过verbose_name，则将column_name替换为verbose_name
                # 否则维持原有的字段名
        return fields

    class Meta:
        model = Buydb
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        # 在导入预览页面中显示跳过的记录
        import_id_fields = ('id')
        # 对象标识的默认字段是id，您可以选择在导入时设置哪些字段用作id  






class BuydbPriceMoreThan(admin.SimpleListFilter):

	title = _('Size')
	parameter_name = 'comparesize' # url最先要接的參數

	def lookups(self, request, model_admin):
		return (
			('>105',_('>105')), # 前方對應下方'>105'(也就是url的request)，第二個對應到admin顯示的文字
			('<=105',_('<=105')),
		)
    # 定義查詢時的過濾條件
	def queryset(self, request, queryset):
		if self.value() == '>105':
			return queryset.filter(Size__gt=105)
		if self.value() == '<=105':
			return queryset.filter(Size__lte=105)









class BuydbAdmin(ImportExportModelAdmin):
    # 要显示的字段列表
    list_display = [field.name for field in Buydb._meta.fields]
    #目的和下方程式碼相同
    #list_display = ('Title', 'MrtCode', 'MrtName', 'Address', 'FloorType', 'RoomNum', 'Price', 'Size', 'Floor', 'Parking', 'Link')
    ordering = ['Price'] #由小到大排序
    #ordering = ['-Price'] #由大到小排序
    search_fields = ['MrtName']
    # 要搜索的字段
    list_filter = [BuydbPriceMoreThan, 'MrtName', 'FloorType', 'RoomNum']
    # 要筛选的字段
    show_detail_fields = ['Title', 'MrtCode', 'MrtName', 'Address', 'FloorType', 'RoomNum', 'Price', 'Size', 'Floor', 'Parking', 'Link']
    # 要展示详情的字段
    list_per_page = 50
    # 分页
    fields = ['Price', 'Link']
    # 它的功用是限制 Admin 可以修改的欄位，如此一來可以避免發生不必要的修改，若是食物名稱及店家再登記之後都不會再做修改了，只有價錢(物價持續上漲)會進行變動，那麼我們要加上

    # model_icon = 'fa fa-laptop'
    # 配置模型图标，也可以在GlobalSetting里面配置

    import_export_args = {
        'import_resource_class': BuydbResource,
        # 'export_resource_class': BuydbResource,
    }
    # 配置导入按钮












class BuydbAdmin2(admin.ModelAdmin):
    list_display = ('Title', 'MrtCode', 'MrtName', 'Address', 'FloorType', 'RoomNum', 'Price', 'Size', 'Floor', 'Parking', 'Link')











class RentdbResource(resources.ModelResource):

    def get_export_fields(self):
        #fields:
        #用來基本客製化顯示的欄位的順序（編輯資料時）
        #預設的系統排列方式，是垂直的一個一個欄位顯示
        fields = self.get_fields()
        # 默认导入导出field的column_name为字段的名称
        # 这里修改为字段的verbose_name
        for field in fields:
            field_name = self.get_field_name(field)
            if field_name in self.verbose_name_dict.keys():
                field.column_name = self.verbose_name_dict[field_name]
                # 如果设置过verbose_name，则将column_name替换为verbose_name
                # 否则维持原有的字段名
        return fields

    class Meta:
        model = Rentdb
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        # 在导入预览页面中显示跳过的记录
        import_id_fields = ('id')
        # 对象标识的默认字段是id，您可以选择在导入时设置哪些字段用作id  






class RentdbPriceMoreThan(admin.SimpleListFilter):

	title = _('Price')
	parameter_name = 'compareprice' # url最先要接的參數

	def lookups(self, request, model_admin):
		return (
			('>8000',_('>8000')), # 前方對應下方'>105'(也就是url的request)，第二個對應到admin顯示的文字
			('<=8000',_('<=8000')),
		)
    # 定義查詢時的過濾條件
	def queryset(self, request, queryset):
		if self.value() == '>8000':
			return queryset.filter(Price__gt=8000)
		if self.value() == '<=8000':
			return queryset.filter(Price__lte=8000)








class RentdbAdmin(ImportExportModelAdmin):
    # 要显示的字段列表
    list_display = [field.name for field in Rentdb._meta.fields]
    #目的和下方程式碼相同
    #list_display = ('Title', 'MrtCode', 'MrtName', 'Address', 'FloorType', 'RoomNum', 'Price', 'Size', 'Floor', 'Parking', 'Link')
    ordering = ['id']
    search_fields = ['MrtName']
    # 要搜索的字段
    list_filter = [RentdbPriceMoreThan, 'MrtName', 'FloorType', 'RoomNum']
    # 要筛选的字段
    show_detail_fields = ['Title', 'MrtCode', 'MrtName', 'Address', 'FloorType', 'RoomNum', 'Price', 'Size', 'Floor', 'Parking', 'Link']
    # 要展示详情的字段
    list_per_page = 50
    # 分页
    fields = ['Price', 'Link']
    # 它的功用是限制 Admin 可以修改的欄位，如此一來可以避免發生不必要的修改，若是食物名稱及店家再登記之後都不會再做修改了，只有價錢(物價持續上漲)會進行變動，那麼我們要加上

    # model_icon = 'fa fa-laptop'
    # 配置模型图标，也可以在GlobalSetting里面配置

    import_export_args = {
        'import_resource_class': RentdbResource,
        # 'export_resource_class': BuydbResource,
    }
    # 配置导入按钮



class RentdbAdmin2(admin.ModelAdmin):
    list_display = ('Title', 'MrtCode', 'MrtName', 'Address', 'FloorType', 'RoomNum', 'Price', 'Size', 'Floor', 'Parking', 'Link')











class WhichMrtNameResource(resources.ModelResource):

    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            if field_name in self.verbose_name_dict.keys():
                field.column_name = self.verbose_name_dict[field_name]
        return fields

    class Meta:
        model = WhichMrtName
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        # 在导入预览页面中显示跳过的记录
        #import_id_fields = ('id',)
        # 对象标识的默认字段是id，您可以选择在导入时设置哪些字段用作id  
        #fields = ('Title', 'MrtCode', 'MrtName')
        # 白名单



@admin.register(WhichMrtName)
class WhichMrtNameAdmin(ImportExportModelAdmin):
    # 要显示的字段列表
    list_display = [field.name for field in WhichMrtName._meta.fields]
    #目的和下方程式碼相同
    #list_display = ('id', 'Title', 'MrtCode', 'MrtName')
    ordering = ['id']
    search_fields = ['id', 'Title', 'MrtCode', 'MrtName']
    # 要搜索的字段
    list_filter = ['MrtName']
    # 要筛选的字段
    show_detail_fields = ['id', 'Title', 'MrtCode', 'MrtName']
    # 要展示详情的字段
    list_per_page = 50
    # 分页

    # model_icon = 'fa fa-laptop'
    # 配置模型图标，也可以在GlobalSetting里面配置

    import_export_args = {
        'import_resource_class': WhichMrtName,
    }
    # 配置导入按钮






admin.site.register(Buydb, BuydbAdmin)
admin.site.register(Rentdb, RentdbAdmin)
#admin.site.register(WhichMrtName, WhichMrtNameAdmin)