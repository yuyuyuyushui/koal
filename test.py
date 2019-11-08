import json
a = json.dumps([{"protocols":"ssh","port":22,"established":"true"}])
print(a, type(a))
b = {
    "a": [{"protocols":"ssh","port":22,"established":"true"}]
}
print(json.dumps(b), type(json.dumps(b)))