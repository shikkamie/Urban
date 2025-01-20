def introspection_info(obj):
    obj_type = type(obj)

    obj_module = getattr(obj, "__module__", "<builtin>")
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    result = {
        "type": obj_type.__name__,
        "attributes": attributes,
        "methods": methods,
        "module": obj_module,
    }
    return result

test = introspection_info({"44": 44})
print(test)