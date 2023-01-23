class Computer_Object:
    print('Access the Class')
    def __init__(self, x, y):
        self.x=x
        self.y=y
    
    def compute_z(self):
        z = self.x+self.y
        self.z=z

        return z
    
    def compute_zz(self):
        zz = (self.z**self.z)+(self.x*self.y)
        self.zz = zz

        return zz


call = Computer_Object(5, -5)
print(call)
print('======= Call part =======')
print(dir(call))
print('=========================')
print(call.x)
print(call.y)
print('=========================')

z = call.compute_z()
print(dir(z))
print('======== Z part =========')
print(dir(call))
print('=========================')
print(z)
print(call.z)
print('=========================')

zz = call.compute_zz()
print(dir(zz))
print('======== ZZ part ========')
print(dir(call))
print('=========================')
print(zz)
print(call.zz)
print('=========================')

