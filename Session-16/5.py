def order_id_generator():
    for i in range(1001,2000):
        yield i

order_id=order_id_generator()
print(next(order_id))
print(next(order_id))
print(next(order_id))
print(next(order_id))

