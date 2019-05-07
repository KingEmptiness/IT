# _*_ encoding:utf-8 _*_
import xadmin

from xadmin import views


# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True

# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView, BaseSetting)


# 全局修改，固定写法
class GlobalSettings(object):
    # 修改title
    site_title = 'TSL | 谢瑞麟'
    # 修改footer
    site_footer = 'TSL | 谢瑞麟'
    # 收起菜单
    menu_style = 'accordion'

# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView,GlobalSettings)