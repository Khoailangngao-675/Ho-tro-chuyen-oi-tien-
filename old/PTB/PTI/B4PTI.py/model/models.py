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
    def __str__(self): # để in ra đối tượng 
        return f"{self.title}({self.release_date}) {self.rating}"
    
