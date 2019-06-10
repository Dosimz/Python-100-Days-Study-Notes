import redis
client = redis.Redis(host='127.0.0.1', port=6379, password='1qaz2wsx')
client.set('username', 'admin')

client.hset('student', 'name', 'hao')

client.hset('student', 'age', 38)

client.keys('*')

print(client.get('username'))

print(client.hgetall('student'))