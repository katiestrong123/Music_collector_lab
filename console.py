import pdb
from models.artist import Artist
import repositories.user_repository as artist_repository


# from models.task import Task
# from models.user import User
# import repositories.task_repository as task_repository


task_repository.delete_all()
user_repository.delete_all()

Artist1 = User('Depeche Mode')
artist_repository.save(Artist1)

Artist2 = User('Metallica')
artist_repository.save(Artist2)
# jack = User('Jack', 'Jarvis')
# user_repository.save(jack)

# victor = User('Victor', 'McDade')
# user_repository.save(victor)

# dishes = Task("So the dishes", jack, 4)
# task_repository.save(dishes)

# homework = Task("Do the homework", jack, 5)
# task_repository.save(homework)

pdb.set_trace()