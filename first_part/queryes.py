from models import Author, Quote
import connect


def main():
    while True:
        command = input("Enter command >>>  ")
        if command.startswith("name:"):
            words = command.split(": ")
            author_name = words[1]
            for author in Author.objects():
                if author_name == author.fullname:
                    quotes = Quote.objects(author=author.id)
                    for quote in quotes:
                        print(quote.quote)
                else:
                    print("No matches")
        elif command.startswith("tag:"):
            words = command.split(": ")
            tag = words[1]
            quotes = Quote.objects(tags=tag)
            if quotes:
                for quote in quotes:
                    print(quote.quote)
            else:
                print("No matches")
        elif command.startswith("tags:"):
            result = set()
            words = command.split(": ")
            tags = words[1]
            tag_list = tags.split(",")
            for tag in tag_list:
                quotes = Quote.objects(tags=tag)
                if quotes:
                    for quote in quotes:
                        print(quote.quote)
                else:
                    print("No matches")
        elif command == "exit":
            break
        else:
            print("No command")


if __name__ == '__main__':
    main()
