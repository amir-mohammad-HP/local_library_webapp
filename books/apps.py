from django.apps import AppConfig
import webbrowser

class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books'

    def ready(self) -> None:
        from books import model_signals
        # webbrowser.open_new('http://127.0.0.1:8000')
        return super().ready()
