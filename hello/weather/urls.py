from django.conf.urls.defaults import *
from hello.weather.views import *
from weather.cron import *
from weather.alarm_cron import *

urlpatterns = patterns('',
    (r'^$',index),
    (r'^update/$',update),
    (r'^dict/$',dict_iter),
    (r'announce/$',announce),
    (r'^verify/get_code/$',get_code),
    (r'verify/get_user_info/$',get_user_info),
    (r'^verify/(?P<action>\w+)/$',verify),    
    (r'^(?P<cid>\d{9}).js$', cid_js),
    (r'^cronweb/$',cronweb),
    (r'^alarmweb/$',alarmweb),
    (r'^shutdown/$',shutdown),

)
