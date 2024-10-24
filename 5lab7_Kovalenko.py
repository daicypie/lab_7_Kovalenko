phone_book = {
    "Іван Іваненко": ["0671234567", "0937654321"],
    "Петро Петренко": ["0509876543", "0665432109"],
    "Марія Шевченко": ["0954321098", "0632109876"],
    "Олена Кравченко": ["0678901234", "0934567890"]
}

def add_phone_number(name, phone_number):
    if name in phone_book:
        phone_book[name].append(phone_number)
        print(f"Новий номер телефону {phone_number} додано до контакту {name}.")
    else:
        print(f"Контакту {name} не знайдено в телефонній книзі.")

add_phone_number("Іван Іваненко", "0998765432")
add_phone_number("Петро Петренко", "0632109876")
add_phone_number("Марія Шевченко", "0956789012")


print("\nСписок номерів телефонів для всіх контактів:")
for name, phones in phone_book.items():
    print(f"{name}: {', '.join(phones)}")