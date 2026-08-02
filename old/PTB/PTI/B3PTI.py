class AnimeItem :
    def __init__(self, anime_id, title,release_date,image=None ,rating=None,link=None) :
        self.id = anime_id
        self.title = title
        self.release_date = release_date
        self.image =image
        self.rating = float(rating) if rating else 0
        self.link = link 
    

    def update(self,new_data:dict) :
        # thuộc tính nào rống sẽ không cập nhật
        for attribute , value in new_data.items():
        # attribute thuoc tinh va value gia tri ; new_data.items() la danh sách rỗng
            if value :
                setattr(self,attribute,value)
               # dùng để kiểm tra thuộc tính có đủ hay ko VD ở đây là anime_id ; title ; release_date
anime1 = AnimeItem(1,"Jujutsu Kaisen","01/01/2022")
anime2 = AnimeItem(8,"Kimetsu no Yaiba","01/05/2022")
anime3 = AnimeItem(3,"Attack on TiTan","05/05/2019")

animes = [anime1,anime2,anime3]
# Duyệt
for anime in animes :
    print(anime.title)

# thêm
anime4 = AnimeItem(4,"One Piece","01/01/1999")
animes.append(anime4)
for anime  in animes:
    print(anime.title)

# Xóa 
remove_title = "Attrack on Titan"
for anime in animes :
    if anime.title == remove_title :
        animes.remove(anime)
for anime in animes :
    print(anime.title)

# Sửa
new_date = {"title":"Jujutsu Kaisen 2"}
anime1.update(new_date)
print(anime1.title)
print(anime1.release_date)