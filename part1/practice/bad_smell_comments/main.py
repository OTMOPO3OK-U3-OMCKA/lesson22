# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    def move(self, field, x_coord: int, y_coord: int, direction, is_fly: bool, crawl: bool, speed: int = 1):

        if is_fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')
        if is_fly:
            speed *= 1.2
        elif crawl:
            speed *= 0.6
        if direction == 'UP':
            y_coord += speed
        elif direction == 'DOWN':
            y_coord -= speed
        elif direction == 'LEFT':
            x_coord -= speed
        elif direction == 'RIGHT':
            x_coord += speed


        field.set_unit(x=x_coord, y=y_coord, unit=self)
