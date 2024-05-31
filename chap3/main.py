bicycles = [ 'trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].upper())

last_item = bicycles[-1]
second_to_last = bicycles[-2]

motorcycles = [ 'honda', 'yamaha', 'suzuki' ]
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('honda')
print(motorcycles)

motorcycles.insert(0, 'bmw')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped = motorcycles.pop()
print(popped)
print(motorcycles)

pop_from_front = motorcycles.pop(0)
print(pop_from_front)
print(motorcycles)