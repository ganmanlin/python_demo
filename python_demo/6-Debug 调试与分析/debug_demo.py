import logging

logging.basicConfig(level=logging.INFO)

a = 1
b = 2
if a == 1:
    flag = True
    logging.info(f"a == {a} : flag ={flag}")

else:
    flag = False
    logging.info(f"a == {a} : flag ={flag}")

print(flag)