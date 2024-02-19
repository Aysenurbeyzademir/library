class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def kitapları_Listele(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        for book in books:
            title, author, release_date, number_of_page = book.split(',')
            print(f"Başlık: {title}, Yazar: {author}, Yayınlanma Tarihi: {release_date}, Sayfa Sayısı: {number_of_page}")

    def kitap_ekle(self):
        title = input("Kitap Adını Girin Lütfen: ")
        author = input("Yazar Adını Girin Lütfen: ")
        year = input("Yayınlanma Tarihini Girin Lütfen: ")
        pages = input("Sayfa Sayısını Girin Lütfen: ")
        self.file.write(f"{title},{author},{release_date},{number_of_page}\n")

    def kitap_kaldır(self):
        title_to_remove = input("Kaldırmak İstediğiniz Kitabın İsmini Yazın Lütfen: ")
        self.file.seek(0)
        books = self.file.read().splitlines()
        for i, book in enumerate(books):
            title, _, _, _ = book.split(',')
            if title == title_to_remove:
                del books[i]
                break
        self.file.truncate(0)
        self.file.writelines(books)

lib = Library()

while True:
    print("*** MENÜ ***")
    print("1) Kitapları Listele")
    print("2) Kitap Ekle")
    print("3) Kitap Kaldır")
    choice = input("İstediğiniz Seçeneği Girin: ")
    if choice == '1':
        lib.kitapları_Listele()
    elif choice == '2':
        lib.kitap_ekle()
    elif choice == '3':
        lib.kitap_kaldır()
    else:
        print("Hatalı Seçim. Lütfen Tekrar Deneyin.")
