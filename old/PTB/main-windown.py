import os
import sys

from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QMessageBox, QWidget

from database import AnimeDatabase, AnimeItem
from dialog import AddDialog, EditDialog

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PLACEHOLDER_IMAGE = os.path.join(BASE_DIR, "gui", "image", "pho.jpg")


def resolve_image_path(image_path):
    if not image_path:
        return PLACEHOLDER_IMAGE

    if image_path.startswith(("http://", "https://")):
        return PLACEHOLDER_IMAGE

    if os.path.isabs(image_path) and os.path.exists(image_path):
        return image_path

    relative_to_base = os.path.join(BASE_DIR, image_path)
    if os.path.exists(relative_to_base):
        return relative_to_base

    fallback_by_name = os.path.join(BASE_DIR, "gui", "image", os.path.basename(image_path))
    if os.path.exists(fallback_by_name):
        return fallback_by_name

    return PLACEHOLDER_IMAGE


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi(os.path.join(BASE_DIR, "gui", "hom.ui"), self)
        self.database = AnimeDatabase()
        self.database.load_data()

        self.ui.stackedWidget.setCurrentIndex(0)
        self.card_layout = QHBoxLayout(self.ui.scrollAreaWidgetContents)
        self.card_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.ui.scrollAreaWidgetContents.setLayout(self.card_layout)

        self.crud = AnimeCRUD(self)
        self.setup_page_crud()
        self.refresh_views()
        self.show()

    def setup_page_crud(self):
        self.ui.btnAdd.clicked.connect(self.crud.add)
        self.ui.btnEdit.clicked.connect(self.crud.edit)
        self.ui.btnDelete.clicked.connect(self.crud.delete)
        self.ui.btnNavHome.clicked.connect(lambda: self.handle_change_nav(0))
        self.ui.btnNavAdd.clicked.connect(lambda: self.handle_change_nav(1))
        self.ui.btnNavSetting.clicked.connect(lambda: self.handle_change_nav(2))
        self.ui.btnNavExit.clicked.connect(self.close)

    def handle_change_nav(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)

    def refresh_views(self, selected_title=None):
        current_title = selected_title
        if current_title is None:
            current_item = self.ui.listWidget.currentItem()
            current_title = current_item.text() if current_item else None

        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(self.database.anime_title_list)

        if self.database.anime_title_list:
            row_to_select = 0
            if current_title in self.database.anime_title_list:
                row_to_select = self.database.anime_title_list.index(current_title)
            self.ui.listWidget.setCurrentRow(row_to_select)

        self.refresh_card_layout()

    def refresh_card_layout(self):
        while self.card_layout.count():
            child = self.card_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        for anime in self.database.anime_item_list:
            self.card_layout.addWidget(AnimeItemWidget(anime))


class AnimeItemWidget(QWidget):
    def __init__(self, anime: AnimeItem):
        super().__init__()
        self.ui = uic.loadUi(os.path.join(BASE_DIR, "gui", "anime_column.ui"), self)
        self.anime = anime
        self.display_description()

    def display_description(self):
        description_text = f"{self.anime.date}\nRating: {self.anime.rating}/10"
        image_path = resolve_image_path(self.anime.image)
        img_pixmap = QPixmap(image_path)

        self.ui.animeTitle.setText(self.anime.title)
        self.ui.animeInfo.setText(description_text)
        self.ui.animeView.setText("" if not img_pixmap.isNull() else "No Image")
        self.ui.animeView.setPixmap(img_pixmap)


class AnimeCRUD:
    def __init__(self, window: MainWindow):
        self.window = window

    def add(self):
        add_dialog = AddDialog()
        if add_dialog.exec():
            inputs = add_dialog.return_input_fields()
            self.window.database.add_item_from_dict(inputs)
            self.window.refresh_views(selected_title=inputs["title"])

    def edit(self):
        item = self.window.ui.listWidget.currentItem()
        if item is None:
            QMessageBox.information(self.window, "Edit anime", "Please select an item to edit.")
            return

        item_title = item.text()
        edit_item = self.window.database.get_item_by_title(item_title)
        if edit_item is None:
            QMessageBox.warning(self.window, "Edit anime", "The selected item no longer exists.")
            self.window.refresh_views()
            return

        edit_dialog = EditDialog(edit_item)
        if edit_dialog.exec():
            inputs = edit_dialog.return_input_fields()
            self.window.database.edit_item_from_dict(item_title, inputs)
            self.window.refresh_views(selected_title=inputs["title"])

    def delete(self):
        item = self.window.ui.listWidget.currentItem()
        if item is None:
            QMessageBox.information(self.window, "Remove anime", "Please select an item to delete.")
            return

        item_title = item.text()
        question = QMessageBox.question(
            self.window,
            "Remove Anime",
            "Do you want to remove this anime?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if question == QMessageBox.StandardButton.Yes:
            self.window.database.delete_item(item_title)
            self.window.refresh_views()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
