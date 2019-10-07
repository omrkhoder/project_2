from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('postgresql://catalog:password@localhost/catalog')
#engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="omrkhoder", email="omrkhoder77@gmail.com",
             picture='https://upload.wikimedia.org/wikipedia/ \
             commons/thumb/1/12/User_icon_2.svg/220px-User_icon_2.svg.png')
session.add(User1)
session.commit()

'''
#### SANDWICHES ####
'''

category1 = Category(user_id=1, name="SANDWICHES")

session.add(category1)
session.commit()

Item1 = Item(user_id=1, name="Smoked Turkey",
             description="Smoked turkey,lettuce,mayonnise,mustard "
                         "and cheddar cheese",
             price="$20",
             category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Roast Beef",
             description="Roast beef,lettuce,cream cheese,cheddar cheese, "
                         "pickles and tomatoes",
             price="$30", category=category1)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Duetto",
             description="Half smoked turkey and "
                         " half roast beaf club",
             price="$39", category=category1)

session.add(Item3)
session.commit()


'''
#### SALADS ####
'''


category2 = Category(user_id=1, name="SALADS")

session.add(category2)
session.commit()

Item1 = Item(user_id=1, name="Rocca",
             description="Rocca leaves, mushroom, parmesan cheese,"
                         " cherry tomatoes and balsamic dreesing. ",
             price="$25", category=category2)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Tuna Pasta",
             description="Fusilli pasta, tuna, bell pepper, black olives, "
                         "rocca leaves, cherry tomatoes and french dressing.",
             price="$35", category=category2)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Chicken Caesar",
             description="Grilled chicken breasts, lettuce, parmesan cheese,"
                         " croutons and caesar dressing",
             price="$40", category=category2)

session.add(Item3)
session.commit()

'''
#### DESSERTS ####
'''


category3 = Category(user_id=1, name="DESSERTS")

session.add(category3)
session.commit()

Item1 = Item(user_id=1, name="Cheesecake",
             description="With your choice of caramel, red berry, "
                         "blue berry, kiwi or chocolate souce.",
             price="$38", category=category3)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Chocolate Molten Cake With Ice Cream",
             description="Served warm with vanilla ice cream.",
             price="$42",
             category=category3)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Caramel Molten Cake With Ice Cream",
             description="Cinnamon apple filled . "
                         "Served warm with vanilla ice cream.",
             price="$45",
             category=category3)

session.add(Item3)
session.commit()

print('We created the data!')
