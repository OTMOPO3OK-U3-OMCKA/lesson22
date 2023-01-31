# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    """    def move(self, field, x_coord, y_coord, direction, is_fly, crawl, speed = 1):

        if is_fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
            if direction == 'UP':
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == 'RIGTH':
                new_y = y_coord
                new_x = x_coord + speed
        if crawl:
            speed *= 0.5
            if direction == 'UP':
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == 'RIGTH':
                new_y = y_coord
                new_x = x_coord + speed

            field.set_unit(x=new_x, y=new_y, unit=self)"""

    def __init__(self):
        self.speed = 0
        self.x = 0
        self.y = 0

    def move(self, field, direction):
        x_coord, y_coord = self.get_step(direction, self.x, self.y)
        field.set_unit(x=x_coord, y=y_coord, unit=self)

    def get_speed(self, speed=1, is_fly=None, crawl=None):
        if is_fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')
        elif is_fly:
            speed *= 1.2
        elif crawl:
            speed *= 0.6
        self.speed = speed

    def get_step(self, direction, x_coord, y_coord):
        if direction == 'UP':
            y_coord += self.speed
        elif direction == 'DOWN':
            y_coord -= self.speed
        elif direction == 'LEFT':
            x_coord -= self.speed
        elif direction == 'RIGHT':
            x_coord += self.speed
        return (x_coord, y_coord)
