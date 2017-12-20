# -*- coding=UTF-8 -*-
import re
from co_name import CoName
import filter_str
copyright=u"""淄博利华通风设备有限公司"""
year_str=r'(?:1|2)\d{3}(?:\s*\W\s*(?:1|2)\d{3})?'
re_rule =re.compile(ur'淄博', re.I)
# str = re.sub(r'^\s*\W\w', "", copyright)
# print str
# res = re.findall(r'(?:ООО|^\d{4})?\s*(?:"|«)(.*?)(?:"|»)', copyright, re.I)
# print filter_str.filter_co_name_after(copyright)
# print CoName.get_co_name(copyright)
print re_rule.findall(copyright)
# -*- coding: utf-8 -*-
# import re
