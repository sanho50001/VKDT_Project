t = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]
# print(t)
e_t = []

for v in t:
    for i in v:
        if v in e_t:
            break
        else:
            e_t.append(v)





print(e_t)