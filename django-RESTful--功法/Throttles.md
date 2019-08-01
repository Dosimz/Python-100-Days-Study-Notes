## Throttling

节流，控制用户请求的访问频率。

## How throttling is determined

和 Permissions、Authentication 一样，REST framework 会在运行 views.py 中的视图类的主要函数前，会调用三个函数校验发送进来的请求。

![](/run/media/yuyi/068AE93F8AE92BBD/python/django-rest-framework/img/throttles_00.png)

REST framework 会从 `throttle_classes = [CustomThrottle, ]` 这样的 Throttle 类的列表中实例化对象，并调用其中的函数方法。



## Setting the throttling policy

设置节流同样可以使用全局或局部。

#### 全局设定

```python3
# setting.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    }
}
```

#### 局部设定

```python3
# views.py

class AccountView(APIView):
    '''用于展示用户界面'''

    authentication_classes = [auth.Authtication, ]
    throttle_classes = [throttling.RandomRateThrottle, ]
...
```



## Custom throttles

```python3
class RandomRateThrottle(throttling.BaseThrottle):

    def allow_request(self, request, view):
        return random.randint(1, 4) != 1
```

- 下面是 BaseThrottle 的部分源码

![](/run/media/yuyi/068AE93F8AE92BBD/python/django-rest-framework/img/throttles_01.png)

自定义 throttles 时，一定要实现 `allow_request` 方法，不然会报错。

- 下面是 BaseThrottle 的 `get_ident` 方法
![](/run/media/yuyi/068AE93F8AE92BBD/python/django-rest-framework/img/throttles_03.png)

从 `REMOTE_ADDR` 中获取 Ip 信息

## SimpleRateThrottle

SimpleRateThrottle 类是一个很好用的 REST-framework 的内置类。

```python3
class VisitThrottle(throttling.SimpleRateThrottle):
	# 用来映射 setting.py 中的配置
    scope = "reflact"

	# 通过内置的 `get_ident` 方法得到 ip 地址
    def get_cache_key(self, request, view):
        return self.get_ident(request)
```

- 下面是 SimpleRateThrottle 的部分源码

![](/run/media/yuyi/068AE93F8AE92BBD/python/django-rest-framework/img/throttles_02.png)

可以看出这个类必须实现 `get_cache_key` 方法,不然会 `raise` 一个错误。
在 SimpleRateThrottle 类的构造方法中，有通过 getattr 映射来判断 `rate` 属性是否存在，如不存在，则通过 `get_rate` 来获取。