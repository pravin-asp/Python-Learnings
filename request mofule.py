Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import requests
res = requests.get('https://github.com')
res.status_code
200
len(res.text)
285891
pritn(res.text[:500])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    pritn(res.text[:500])
NameError: name 'pritn' is not defined. Did you mean: 'print'?
print(res.text[:500])








<!DOCTYPE html>
<html
  lang="en"
  data-color-mode="dark" data-dark-theme="dark"
  data-color-mode="light" data-light-theme="light" data-dark-theme="dark"
  data-a11y-animated-images="system" data-a11y-link-underlines="true"
  
  >



  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link
>>> res.raise_for_status()
>>> badRes = requests.get('http://github.com')
>>> badRes.raise_for_status()
>>> for chunk in res.iter_content(100000):
...     print(chunk)
... 
...     



