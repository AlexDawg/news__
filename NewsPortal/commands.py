
#Подгружаю все модели в shell
from NewsPortal.models import *

#Создать двух пользователей
User.objects.create_user('User1')
User.objects.create_user('User2')

#Создать два объекта модели Author, связанные с пользователями.
author_1 = Author.objects.create(name = "author1", users = User.objects.get(id=1))
author_2 = Author.objects.create(name = "author2", users = User.objects.get(id=2))

#Добавить 4 категории в модель Category.
sport = Category.objects.create(name_category = 'Спорт')
politics = Category.objects.create(name_category = 'Политика')
economy = Category.objects.create(name_category = 'Экономика')
culture = Category.objects.create(name_category = 'Культура')

#Добавить 2 статьи и 1 новость.
news_1 = Post.objects.create(author = Author.objects.get(id=2), title = "Политика")
article_1 = Post.objects.create(author = Author.objects.get(id=1),type = article, title = "Спорт и Культура")
article_2 = Post.objects.create(author = Author.objects.get(id=2),type = article, title = "Экономика")
article_3 = Post.objects.create(author = Author.objects.get(id=1),type = article, title = "Олимпийские игры", text ='Наверное, трудно будет найти другую такую площадку, на которой спорт и культура переплетались бы так тесно, как на Олимпийских играх. Параллельно спортивным состязаниям проходят многочисленные культурные мероприятия. Олимпиада привлекает не только спортсменов и болельщиков. Сюда стекаются представители всех сфер культурной жизни страны. Театр, музыка, изобразительное искусство, фольклор, телевидение, всевозможные выставки и экспозиции - все это дополняет и разнообразит атмосферу спортивного праздника. Образуется некий синергетический эффект влияния на человека, недостижимый для спорта и культуры как отдельных факторов развития личности. И в этом смысле Олимпиада в Сочи является уникальным событием, обогащающим внутренний мир, душу каждого, кому посчастливилось побывать здесь в эти дни. Само по себе понятие культуры очень широкое. Оно имеет огромное количество значений в различных областях человеческой жизнедеятельности. В целом под культурой понимают совокупность ценностей, характеризующих развитие общества, и определяющих нормы его поведения. Рассуждая на тему культуры и спорта, целесообразно было бы выделить в общем культурном спектре сегмент культуры физической. Нам всем приятно иметь дело с культурными людьми. Это люди образованные, начитанные, интересные, воспитанные. Однако культура почти всегда воспринимается односторонне. Чтобы понять это, достаточно включить телевизор и среди множества каналов выбрать канал "Культура". Какие программы вы там увидите? О музыке, театре, живописи, литературе, науке. Вряд ли вы найдете там хоть что-нибудь о культуре физической. Интеллект, душа, эмоции, воображение – де-факто эти сферы стали канонической территорией современной культуры. А как же физическое развитие личности? Физическая культура у большинства из нас ассоциируется со школьными занятиями физкультурой, или же спортзалом, бицепсами, трицепсами. Мы перестали понимать, что такое человек физически культурный? В этом и однобокость.')

#Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
Cat_post1 = PostCategory.objects.create(post = Post.objects.get(id=9), category = Category.objects.get(pk=2))
Cat_post2 = PostCategory.objects.create(post = Post.objects.get(id=10), category = Category.objects.get(pk=1))
Cat_post2_1 = PostCategory.objects.create(post = Post.objects.get(id=10), category = Category.objects.get(pk=4))
Cat_post3 = PostCategory.objects.create(post = Post.objects.get(id=11), category = Category.objects.get(pk=3))

#Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
comment_1 = Comment.objects.create(post = Post.objects.get(id=9), user = User.objects.get(id=1), text = '10 Баллов')
comment_2 = Comment.objects.create(post = Post.objects.get(id=10), user = User.objects.get(id=2), text = 'Спорт в массы!')
comment_3 = Comment.objects.create(post = Post.objects.get(id=11), user = User.objects.get(id=1), text = 'Полезная статья')
comment_2_1 = Comment.objects.create(post = Post.objects.get(id=10), user = User.objects.get(id=1), text = 'Спасибо!')
comment_4 = Comment.objects.create(post = Post.objects.get(id=12), user = User.objects.get(id=2), text = 'Очень круто!')
#Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
Post.objects.get(id=9).dislike()
Post.objects.get(id=9).dislike()
Post.objects.get(id=9).like()
Post.objects.get(id=9).like()
Post.objects.get(id=9).like()
Post.objects.get(id=9).dislike()
Post.objects.get(id=10).like()
Post.objects.get(id=10).like()
Post.objects.get(id=10).like()
Post.objects.get(id=10).like()
Post.objects.get(id=11).like()
Post.objects.get(id=11).like()
Post.objects.get(id=11).like()
Post.objects.get(id=11).dislike()
Post.objects.get(id=11).dislike()
Post.objects.get(id=11).like()
Comment.objects.get(id=1).like()
Comment.objects.get(id=1).like()
Comment.objects.get(id=1).like()
Comment.objects.get(id=1).like()
Comment.objects.get(id=1).dislike()
Comment.objects.get(id=2).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).like()
Comment.objects.get(id=5).like()
Comment.objects.get(id=5).like()
Comment.objects.get(id=5).like()
Comment.objects.get(id=5).like()
Comment.objects.get(id=5).like()
Comment.objects.get(id=5).like()
Comment.objects.get(id=5).like()

#Обновить рейтинги пользователей.
Author.objects.get(id=1).update_rating()
Author.objects.get(id=2).update_rating()

#Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).

from django.db.models import Max
max_rating = Author.objects.aggregate(rating__max=Max('user_rating'))['rating__max']
best_id = Author.objects.get(user_rating=max_rating).id
info = Author.objects.filter(id=best_id).values_list('name', 'user_rating').first()
info

#Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
ar_max_rating = Post.objects.filter(type='AR').aggregate(rating__max=Max('rating'))['rating__max']
best_id_ar = Post.objects.get(rating=ar_max_rating).id
preview = Post.objects.get(id=best_id_ar).preview()
ar_info = Post.objects.filter(id=best_id_ar).values_list('time_in', 'author', 'rating', 'title').first(), preview
ar_info

#Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
r = Comment.objects.filter(post_id=best_id_ar).values_list('time_in', 'user_id__username', 'rating', 'text')
r