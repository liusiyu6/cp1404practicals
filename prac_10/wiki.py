import wikipedia


def main():
    while True:
        title = input("Enter page title: ").strip()
        if title == "":
            print("Thank you.")
            break

        try:
            page = wikipedia.page(title, auto_suggest=False)

            print(page.title)
            print(page.summary.split("\n")[0])  # 第一段 summary
            print(page.url)

        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following:")
            print(e.options)

        except wikipedia.exceptions.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')


if __name__ == "__main__":
    main()
