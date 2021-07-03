# Copyright © 2017 Semester.ly Technologies, LLC
#
# Semester.ly is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Semester.ly is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

from django.conf.urls import url
from django.contrib import admin

import exams.views
from helpers.mixins import FeatureFlowView

admin.autodiscover()

urlpatterns = [
    url(r'^final_exams/*$',
        FeatureFlowView.as_view(feature_name='FINAL_EXAMS')),

    url(r'^exams/?$', exams.views.ExamView.as_view()),
    url(r'^exams/links/?$', exams.views.ExamLink.as_view()),
    url(r'^exams/links/(?P<slug>.+)/$',
        exams.views.ExamLink.as_view())
]
