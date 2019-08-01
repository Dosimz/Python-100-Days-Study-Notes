## Permissions

权限可以用来给不同类型用户授予访问的许可。

## Custom permissions

自定义权限类，必须实现下面两个方法中的一下个：

- `.has_permission(self, request, view)`
- `.has_object_permission(self, request, view, obj)`

给予权限，则方法函数返回 `True`;没有访问权限，则返回 `False`。

1. 创建权限类

```python3
class Mypermission(object):
    def has_permission(self, request, view):
        if request.user.user_type != 2:
            return False
        return True
```
`has_permission` 方法控制 view 级别，
`has_object_permission` 控制对象级别

2. 在 `Permission_classes` 中定义

```python3
class VIPinfo(APIview):
    ...
    authentication_classes = [auth.Authtication, ]
	permission_classes = [permission.Mypermission, ]
	...
```
和 Authentication 组件一样，也可以在 setting.py 文件中全局配置权限
```python3
REST_FRAMEWORK = {
...
    "DEFAULT_PERMISSION_CLASSES": ['api.utils.permission.Mypermission']
...
}
```

