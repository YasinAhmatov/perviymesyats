# 1
name = "Yasin"
print(name[ ::-1 ])

# 2

name = input("введите своё имя: ")
print(name[0], "это первая буква твоего имени")
print(name[-1], "это последняя буква твоего имени")
print(name[1:-1] ,"эти буквы между ними")

# 3

text = """dvertising companies say advertising is necessary and important. It informs people about
new products. Advertising hoardings in the street make our environment colourful. And
adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next
programme in the mini-drama. Advertising can educate, too. Adverts tell us about new,
healthy products. And adverts in magazines give us ideas for how to look prettier, be
fashionable and be successful. Without advertising, life is boring and colourless.
But some consumers argue that advertising is a bad thing. They say that advertising is bad
for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers
know we love our children and want to give them everything. So they use children’s ‘pester
power’ to sell their products. Finally, consumers say, if there is advertising there must be
rules. Some adverts advertise unhealthy things like cigarettes and make people waste their
money
"""
print(text.count("s"))
print(text.count("t"))

# 4

name_1 = "aidana"        
name_2 = "adilet"
print((name_1[0] + name_2[0]) + (name_1[1] + name_2[1]) + (name_1[2] + name_2[2]) + (name_1[3] + name_2[3]) + (name_1[4] + name_2[4]) + (name_1[5] + name_2[5]))