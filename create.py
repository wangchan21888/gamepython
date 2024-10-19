import os

# Cấu trúc thư mục và tệp
structure = {
    "rung_huyen_bi": {
        "assets": {
            "images": {
                "characters": [
                    "hero.png",
                    "enemy.png",
                    "boss.png"
                ],
                "backgrounds": [
                    "spring.png",
                    "summer.png",
                    "autumn.png",
                    "winter.png"
                ],
                "items": [
                    "health_potion.png",
                    "mana_potion.png"
                ]
            },
            "sounds": [
                "background_music.mp3",
                "attack_sound.wav",
                "boss_music.mp3"
            ],
            "fonts": [
                "game_font.ttf"
            ]
        },
        "src": [
            "main.py",                    # Tệp chính để chạy trò chơi
            "game.py",                    # Logic chính của trò chơi
            "player.py",                  # Định nghĩa lớp nhân vật
            "enemy.py",                   # Định nghĩa lớp kẻ thù
            "boss.py",                    # Định nghĩa lớp boss
            "world.py",                   # Quản lý thế giới và các mùa
            "item.py",                    # Định nghĩa lớp vật phẩm
            "scene.py",                   # Quản lý các cảnh (mùa, khu vực)
            "audio.py",                   # Xử lý âm thanh
            "utils.py"                    # Các hàm tiện ích
        ],
        "levels": [
            "level_spring.py",            # Định nghĩa cấp độ mùa xuân
            "level_summer.py",            # Định nghĩa cấp độ mùa hè
            "level_autumn.py",            # Định nghĩa cấp độ mùa thu
            "level_winter.py"             # Định nghĩa cấp độ mùa đông
        ],
        "README.md": "Thông tin về dự án."
    }
}

# Mã mẫu cho từng tệp
code_samples = {
    "main.py": """import pygame
from game import Game

def main():
    pygame.init()
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
""",
    "game.py": """class Game:
    def __init__(self):
        # Khởi tạo trò chơi
        pass

    def run(self):
        # Logic để chạy trò chơi
        pass
""",
    "player.py": """class Player:
    def __init__(self):
        # Khởi tạo nhân vật
        pass
""",
    "enemy.py": """class Enemy:
    def __init__(self):
        # Khởi tạo kẻ thù
        pass
""",
    "boss.py": """class Boss:
    def __init__(self):
        # Khởi tạo boss
        pass
""",
    "world.py": """class World:
    def __init__(self):
        # Quản lý thế giới
        pass
""",
    "item.py": """class Item:
    def __init__(self):
        # Định nghĩa lớp vật phẩm
        pass
""",
    "scene.py": """class Scene:
    def __init__(self):
        # Quản lý các cảnh
        pass
""",
    "audio.py": """class Audio:
    def __init__(self):
        # Xử lý âm thanh
        pass
""",
    "utils.py": """def utility_function():
    # Một số hàm tiện ích
    pass
""",
    "level_spring.py": """class LevelSpring:
    def __init__(self):
        # Định nghĩa cấp độ mùa xuân
        pass
""",
    "level_summer.py": """class LevelSummer:
    def __init__(self):
        # Định nghĩa cấp độ mùa hè
        pass
""",
    "level_autumn.py": """class LevelAutumn:
    def __init__(self):
        # Định nghĩa cấp độ mùa thu
        pass
""",
    "level_winter.py": """class LevelWinter:
    def __init__(self):
        # Định nghĩa cấp độ mùa đông
        pass
""",
    "README.md": "Thông tin về dự án."
}

# Tạo cấu trúc thư mục và tệp
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)  # Tạo thư mục nếu chưa tồn tại
            create_structure(path, content)
        elif isinstance(content, list):
            for file_name in content:
                # Tạo đường dẫn tệp
                file_path = os.path.join(path, file_name)

                # Tạo thư mục cho tệp (nếu cần thiết)
                os.makedirs(os.path.dirname(file_path), exist_ok=True)

                # Tạo tệp mã chỉ nếu có mã mẫu
                if file_name in code_samples:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(code_samples[file_name])
                else:
                    # Tạo tệp trống nếu không có mã mẫu
                    open(file_path, 'w', encoding='utf-8').close()
        else:
            with open(os.path.join(base_path, name), 'w', encoding='utf-8') as f:
                f.write(content)

# Bắt đầu tạo cấu trúc
create_structure(".", structure)

print("Cấu trúc thư mục và tệp đã được tạo thành công!")
