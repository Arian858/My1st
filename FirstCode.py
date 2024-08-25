# defining a function that takes any email as its parameter, and change its domain:

import re

def domain_change(email,dom):
  email = str(email).lower()
  dom = str(dom).lower()
  pattern = r"(.*)@(.+)(\.com)$"
  result = re.search(pattern,email)
  return f"{result[1]}@{dom}.com"

#new_email = domain_change("redeye@gmail.com", "yahoo")
