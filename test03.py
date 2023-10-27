# OOP

class IotSAU :
    #data/property/field/attribute
    major = "SAU"
    name = ''

    #method(มันคือ Function แต่เราไม่เรียกฟังก์ชั่น)
    def showHi(self) :
               print('Hi...')

    def introduceMySelf(self):
            print(f'My name is {self.name}')
            print(f'My major is {self.major}')

#------------------------
#สร้าง object
obA = IotSAU( ) #เป็นการเรียกใช้ constructor ของคลาสให้ทำงาน (ถ้ามี)
obB = IotSAU


#การใช้งาน Data ของ Object คือ เอาค่ามันมาใช้ หรือเปลี่ยนค่าให้มั่นใหม่
print( obA.major)
obA.major = "Wow"
obA.major = "ฟ้าร้อง"
obB.name = "ฝนตกแล้ว"

#การใช้งาน Data ของ Object คือ การสั่งเมธอดของ object นั้นๆ ทำงาน
obA.introduceMySelf()
obB.introduceMySelf()