class homework:
    def __init__(self, name, priority, completed=False):
        self.name = name
        self.priority = priority
        self.completed = completed

class homeworklist:
    def __init__(self):
        self.homework_list = []
    
    def add_item(self, homework):
        self.homework_list.append(homework)
    
    def all_completed(self):
        for homework in self.homework_list:
            if homework.completed == False:
                print(homework.name)
        if all(homework.completed for homework in self.homework_list):
            print("All finished!")

hw_list = homeworklist()
hw_list.add_item(homework("Lập trình App Producer", 3))
hw_list.add_item(homework("Làm văn", 2, True))
hw_list.add_item(homework("Lập trình GameMaker", 3))
hw_list.all_completed()