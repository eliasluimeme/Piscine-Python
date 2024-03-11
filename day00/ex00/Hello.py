ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[-1] = "world!"

ft_tuple = list(ft_tuple)
ft_tuple[-1] = "morocco!"
ft_tuple = tuple(ft_tuple)

ft_set = list(ft_set)
if ft_set[-1] == "tutu!":
    ft_set[-1] = "benguerir!"
else: ft_set[0] = "benguerir!"
ft_set = set(ft_set)

ft_dict["Hello"] = "1337!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)