# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.flatpages import views

from .views import (PersonalInfoView,
                    )

urlpatterns = [
        url(r'^$', complete_resume.as_view(), name="complete_resume"),
        url(r'PersonalInfo$', PersonalInfoView.as_view(), name='Personal_Info'),

'''
        url(r'searcharea$', SearchAreaList.as_view(), name='searcharea_list'),
        url(r'searcharea/create/$', SearchAreaCreate.as_view(), name='searcharea_create'),
        url(r'searcharea/update/(?P<phase1>[\w\-]+)/(?P<name1>[\w\-]+)$', SearchAreaUpdate.as_view(), name='searcharea_update'),
        url(r'searcharea/(?P<phase1>[\w\-]+)/(?P<name1>[\w\-]+)/delete$', SearchAreaDelete.as_view(), name='searcharea_delete'),
        url(r'searcharea/(?P<phase1>[\w\-]+)/(?P<name1>[\w\-]+)$', SearchAreaView.as_view(), name='searcharea_detail')
        '''
	]
