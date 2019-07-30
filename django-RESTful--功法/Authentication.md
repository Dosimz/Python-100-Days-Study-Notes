## Authentication

Authentication（身份认证）是 REST framework 提供用来验证请求的用户身份信息的组件。  


- 自定义 Authentication 类
- 内置 Authentication 类



### 使用

1. 创建一个类来实现验证
2. 全局或局部声明验证类





假设现在有一个页面需要登录才能访问。

```python3
	
	# urls.py
	# http://127.0.0.1:8000/api/v1/account/
    path('api/v1/account/', views.AccountView.as_view())
```
----
```python3
# views.py

class AccountView(APIView):
    '''用于展示用户中心'''
    
    def get(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None, 'data': None}
        try:
            ret['data'] = '个人账户信息'
        except Exception as e:
            pass
        return JsonResponse(ret)
```

 这里还没有加 Authentication 相关组件，所以可以直接得到请求内容。

![](/run/media/yuyi/068AE93F8AE92BBD/python/django-rest-framework/img/authentication_00.png)





1. 创建一个类来实现验证

这里自定义一个基于 token 的验证类。

```python3
class Accoutcation(BasicAuthentication):

    def authenticate(self, request):
    	# 在请求头获取 token
        token = request._request.GET.get('token')
        # 在数据库中查询
        token_obj = models.UserToken.objects.filter(token=token).first()
        # 如果数据库中没找到，用户验证失败;否则返回一个元组
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        return (token_obj.user, token_obj)
```
>  必须实现 authenticate 方法，否则会报错; 如果自定义的类有返回值，则返回值必须是元组。
>
>  返回的元组会在源码中用来设置 `request.user` 和 `request.auth`
>
>  如果不设置类来进行验证，源码中还是会执行部分相关代码，默认将 `request.user` 设置为 `AnonymousUser`、`request.auth` 设置为 `None`。






2. 全局或局部声明验证类




a. 局部设置验证类
	
```python3
   # views.py
   class AccountView(APIView):
   ...
       authentication_classes = [Accountcation, ]
   ...
```

在每个需要设定验证的视图类里给 authentication_classes 赋值即可。
	   
> 在 `AccountView` 继承的 `APIView` 类中会找到 authentication_classes 并实例化



b. 全局设置认证
   	

```python3
	  # setting.py
	  # 列表里填验证类的相对路径
	  REST_FRAMEWORK = {
	      'DEFAULT_AUTHENTICATION_CLASSES': [
	          'api.views.Accoutcation',
	      ]
	  }
```

> 全局设定后，每一个视图类都默认使用设定中的验证。 

可以通过给 `authentication_classes` 设定空列表来跳过认证 

```python3
authentication_classes = []
```



