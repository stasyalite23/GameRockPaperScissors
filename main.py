import random

def play_rock_paper_scissors():
    print("Добро пожаловать в Камень-Ножницы-Бумага!")
    print("Правила игры:")
    print("Камень побеждает ножницы")
    print("Ножницы побеждают бумагу")
    print("Бумага побеждает камень")

    while True:
        user_choice = input("Введите свой выбор (камень, бумага, или ножницы): ")

        # Validate user's input
        choices = ['камень', 'бумага', 'ножницы']
        if user_choice not in choices:
            print("Некорректный ввод данных. Пожалуйста,попробуйте снова.")
            continue

        computer_choice = random.choice(choices)

        print(f"Выбор пользователя: {user_choice}")
        print(f"Выбор компьютера: {computer_choice}")

        if user_choice == computer_choice:
            result = "Это ничья!"
        elif (
            (user_choice == "камень" and computer_choice == "ножницы") or
            (user_choice == "ножницы" and computer_choice == "бумага") or
            (user_choice == "бумага" and computer_choice == "камень")
        ):
            result = "Вы победили!"
        else:
            result = "Выигрывает компьютер!"

        print(result)

        play_again = input("Играем снова? (да/нет): ")
        if play_again.lower() != "да":
            print("Спасибо за игру. До новых встреч!")
            break

play_rock_paper_scissors()
