import urllib.robotparser as rb

bot = rb.RobotFileParser()

x = bot.set_url('https://www.geeksforgeeks.org/robot.txt')
print(x)

y = bot.read()
print(y)

z = bot.can_fetch('*', 'https://www.geeksforgeeks.org/')
print(z)

w = bot.can_fetch('*', 'https://www.geeksforgeeks.org/ wp-admin')
print(w)
