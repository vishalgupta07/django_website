# -*- coding: utf-8 -*-
# @Author: vishalgupta07
# @Date:   2019-04-06 12:53:43
# @Last Modified by:   vishalgupta07
# @Last Modified time: 2019-04-06 12:55:00
from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    try:
        group =  Group.objects.get(name=group_name)
    except Group.DoesNotExist:
        return False

    return group in user.groups.all()