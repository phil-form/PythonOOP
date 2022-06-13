from Entity.Circuit import Circuit
from Entity.Concurrent import Concurent 
from Entity.Voiture import Voiture
from Entity.Course import Course

spa = Circuit("spa", 7004, 20)

c = Course("technobel eaudooce", spa, 50, 5000)

vRiri = Voiture("Audi", "A3", 180, 260)
riri = Concurent("riri", 5, vRiri)
c.addConcurrent(riri)

vFifi = Voiture("Audi", "A3", 180, 260)
fifi = Concurent("fifi", 5, vFifi)
c.addConcurrent(fifi)

vLoulou = Voiture("Audi", "A3", 180, 260)
loulou = Concurent("loulou", 5, vLoulou)
c.addConcurrent(loulou)

c.startCourse()

print(c.getWinner().name)